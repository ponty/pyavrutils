from easyprocess import Proc, extract_version
from entrypoint2 import entrypoint
from pyavrutils.avrsize import AvrSize
from pyavrutils.util import tmpdir, tmpfile, separate_sources, CompileError
from unipath.path import Path
import tempfile

class AvrGccCompileError(CompileError):
    pass

class AvrGcc(object):
    minprog = 'int main(){};'
    def __init__(self, mcu='atmega168'):
        self.cc = 'avr-gcc'
        self.proc = None
        self.options_extra = []
        self.use_only_extra_options = False
        self.defines = []
        self.includes = []
        self.output = None
        self.mcu = mcu
        self._targets = None

        # Hz
        self.f_cpu = 4000000

        self.std = 'gnu99'

        #http://www.network-theory.co.uk/docs/gccintro/gccintro_49.html
        # 0/1/2/3/s (s=for size)
        self.optimization = 0

        # Enables linker relaxations. This is a catch-all for optimisations
        # which occur during the link stage,
        # where the final code can be altered by the linker
        # to produce better code according to preset patterns.
        # It doesn't do much at the moment,
        # but one thing it does do is replace JMP instructions
        # with RJMP instructions where possible to save a byte or so.
        self.relax = False

        # "garbage collect" unused sections
        # Used with the -ffunction-sections and -fdata-sections compiler flags.
        # When set, the linker is free to discard unused sections
        # from the resulting binary.
        self.gc_sections = False

        # Force each function into it's own section
        self.ffunction_sections = False

        # Same as above, but for RAM globals.
        self.fdata_sections = False

        # stop the compiler from inlining repeated calls to tiny functions
        # which can blow up the total binary size
        # --param inline-call-cost=2  ??
        self.fno_inline_small_functions = False

        self.optimize_for_size()

    def optimize_for_size(self):
        '''
        http://www.avrfreaks.net/index.php?name=PNphpBB2&file=viewtopic&t=90752

        http://www.avrfreaks.net/index.php?name=PNphpBB2&file=viewtopic&t=69813
        '''
        self.optimization = 's'
        self.relax = True
        self.gc_sections = True
        self.ffunction_sections = True
        self.fdata_sections = True
        self.fno_inline_small_functions = True

    def optimize_no(self):
        ''' all options set to default
        '''
        self.optimization = 0
        self.relax = False
        self.gc_sections = False
        self.ffunction_sections = False
        self.fdata_sections = False
        self.fno_inline_small_functions = False
        

    @property
    def ok(self):
        if self.proc:
            return self.proc.return_code == 0

    @property
    def targets(self):
        if not self._targets:
            
#            cc = AvrGcc()
#            cc.optimize_no()
#            cc.mcu = 'xxxx'
#            try:
#                cc.build(self.minprog)
#            except AvrGccCompileError:
#                pass
#            lines = cc.error_text.splitlines()
#            lines = [x for x in lines if '/' not in x]
#            lines = [x for x in lines if ':' not in x]
#            lines = [x for x in lines if 'xxxx' not in x]
#            lines = [x for x in lines if '\\' not in x]
#            lines = [x.strip() for x in lines]
#            lines.sort()
#            self._targets = lines
            def filt1(lines):
                for i, x in enumerate(lines):
                    if 'known mcu names' in x.lower():
                        return lines[i+1:]
            def filt2(lines):
                for i, x in enumerate(lines):
                    if not x:
                        return lines[:i]
                    
            s = Proc([self.cc, '--target-help']).call().stdout
            lines = s.splitlines()
            lines=filt1(lines)        
            lines=filt2(lines)
            mcus=' '.join(lines).strip().split()
            self._targets=mcus        
        return self._targets

    @property
    def error_text(self):
        if self.proc:
            return self.proc.stderr

    def version(self):
        'avr-gcc version'
        return extract_version(Proc(self.cc + ' --version').call().stdout)

    def options_generated(self):
        return self.command_list([''], _opt=True)

    def command_list(self, sources, _opt=False):
        '''command line as list'''
        def abspath(x):
            x = Path(x).absolute()
            if not x.exists():
                raise ValueError('file not found! ' + x.absolute())
            return x

        self.f_cpu = int(self.f_cpu)

        self.mcu = str(self.mcu)
#        if not self.mcu  in self.targets:
#            raise ValueError('invalid mcu:' + self.mcu)

        if not _opt:
            sources = [ abspath(x) for  x in sources]
        includes = [ abspath(x) for  x in self.includes]

        if not self.output:
            self.output = tempfile.NamedTemporaryFile(prefix='pyavrutils_', suffix='.elf', delete=0).name

        defines = self.defines + ['f_cpu=' + str(self.f_cpu)]

        cmd = [self.cc]
        if not self.use_only_extra_options:
            if not _opt:
                cmd += sources
            cmd += ['-D' + x for x in defines]
            cmd += ['-I' + x for x in includes]
            if not _opt:
                cmd += ['-o' , self.output]
            cmd += ['-mmcu=' + self.mcu]
            cmd += ['--std=' + self.std]
            if self.relax:
                cmd += ['-Wl,--relax']
            if self.gc_sections:
                cmd += ['-Wl,--gc-sections']
            if self.ffunction_sections:
                cmd += ['-ffunction-sections']
            if self.fdata_sections:
                cmd += ['-fdata-sections']
            if self.fno_inline_small_functions:
                cmd += ['-fno-inline-small-functions']
            if self.optimization != 0:
                cmd += ['-O' + str(self.optimization)]

        cmd += self.options_extra
        return cmd

    def build(self, sources=None, headers=None):
        ''' sources can be file name or code:
        sources=['x.c','int main(){}']
        or
        sources='int main(){}'
        '''
        tempdir = None
        strings, files = separate_sources(sources)
        if len(strings) or headers:
            # TODO: remove tempdir
            tempdir = tmpdir()
        
        temp_list = [tmpfile(x, tempdir, '.c') for x in strings]


        if headers:
            for n, s in headers.items():
                Path(tempdir).child(n).write_file(s)
            
        
        cmd = self.command_list(files + temp_list)
        if tempdir:
            cmd += ['-I' + tempdir]
        self.proc = Proc(cmd).call()
#        for x in temp_list:
#            os.remove(x)

        if not self.ok:
            raise AvrGccCompileError(cmd, sources, self.error_text)

    def size(self):
        s = AvrSize()
        s.run(self.output, self.mcu)
        return s

@entrypoint
def _test():
    cc = AvrGcc()
    print 'version =', cc.version()
    code = 'int main(){return 0;}'
    print code
    cc.build([code])
    print 'size =', cc.size()

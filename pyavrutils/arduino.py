from confduino import boardlist,hwpacklist,mculist
from easyprocess import Proc
from path import path
from pyavrutils.avrsize import AvrSize
from pyavrutils.util import tmpdir, separate_sources, tmpfile, rename, \
    CompileError
import os

class ArduinoCompileError(CompileError):
    pass

class Arduino(object):
    '''
    wrapper for arscons_

    
    .. _arscons: http://code.google.com/p/arscons/
    '''
    minprog = 'void setup(){};void loop(){};'
    def __init__(self, board='pro', hwpack='arduino', mcu=None, f_cpu=None, extra_lib=None, ver=None , home='auto'):
        '''
        :param home:  'auto' -> ARDUINO_HOME env var
        '''
        assert board or mcu

        if home == 'auto':
            home = os.environ.get('ARDUINO_HOME', None)
        self.home = home        
        self.board = board        
        self.hwpack = hwpack        
        self.mcu = mcu        
        self.f_cpu = f_cpu        
        self.ver = ver        
        self.extra_lib = extra_lib     
           
        self.proc = None
        self.output = None
        
    def command_list(self):
        '''command line as list'''
        cmd = []
        cmd += ['scons']
        if self.home:
            cmd += ['ARDUINO_HOME=' + self.home]

        if self.board:
            cmd += ['ARDUINO_BOARD=' + self.board]
            
        if self.hwpack:
            cmd += ['ARDUINO_HARDWARE_PACKAGE=' + self.hwpack]
            
        if self.mcu:
            cmd += ['MCU=' + self.mcu]
        if self.f_cpu:
            cmd += ['F_CPU=' + str(self.f_cpu)]
        
        if self.ver:
            cmd += ['ARDUINO_VER=' + self.ver]
            
        if self.extra_lib:
            cmd += ['EXTRA_LIB=' + self.extra_lib]
            
        return cmd
    
    def build(self, sources=None):
        # TODO: remove tempdir
        tempdir = tmpdir(dir=tmpdir())
        
        SConstruct = path(__file__).parent / 'SConstruct'
        SConstruct.copy(tempdir / 'SConstruct')
        
        strings, files = separate_sources(sources)
        allfiles = []
        for x in strings:
            f = tmpfile(x, tempdir, '.pde')
            allfiles += [f]
            
        for x in files:
            f = tempdir / x.name
            if x.parent.name == x.namebase:
                # copy all files from pde directory
                for y in x.parent.files():
                    y.copy(tempdir / y.name)
            else:
                # copy only pde
                x.copy(f)
            allfiles += [f]
            
        for x in allfiles:
            if x.ext == '.pde' and 'setup' in x.text() and 'loop' in x.text() :
                projname = x.namebase
                break
        
        assert projname
        
        tempdir = rename(tempdir, tempdir.parent / projname)
        
        cmd = self.command_list()
        
        self.proc = Proc(cmd, cwd=tempdir).call()
        if not self.ok:
            raise ArduinoCompileError(cmd, sources, self.error_text)
        self.output = tempdir.files('*.elf')[0]
        
    def mcu_compiler(self):
        mcu = self.mcu
        if not mcu:
            assert self.board
            mcu = mculist.mcu(self.board, self.hwpack)
        assert mcu
        return mcu
        
    def size(self):
        s = AvrSize()
        mcu = self.mcu_compiler()
        assert mcu
        s.run(self.output, mcu)
        return s

    @property
    def error_text(self):
        if self.proc:
            return self.proc.stderr
        
    @property
    def stderr(self):
        if self.proc:
            return self.proc.stderr
        
    @property
    def warnings(self):
        if self.proc:
            return [line for line in self.stderr.splitlines() if 'warning:' in line]
    
    @property
    def ok(self):
        if self.proc:
            return self.proc.return_code == 0

def targets(filter=True):
    uniq_mcu=0
    ls = []
    oldmcus = []
    for h in hwpacklist.hwpack_names():
        for b in boardlist.board_names(h):
            mcu = mculist.mcu(b,h)
            # TODO: not working
            if b in 'atmega8u2 attiny861 sanguino'.split():
                continue
            if not uniq_mcu or mcu not in oldmcus:
                cc = Arduino(board=b, hwpack=h)
                cc.board_options=boardlist.boards(h)[b]
                ls += [cc]
                oldmcus += [mcu]
    return ls

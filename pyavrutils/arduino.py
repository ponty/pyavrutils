from confduino import version, mculist
from easyprocess import Proc
from path import Path
from pyavrutils.avrsize import AvrSize
from pyavrutils.util import tmpdir, separate_sources, tmpfile, rename, \
    CompileError
import logging
import os

log = logging.getLogger(__name__)


class ArduinoCompileError(CompileError):
    pass


class Arduino(object):
    '''
    wrapper for arscons_ and ino_


    .. _arscons: https://github.com/suapapa/arscons
    .. _ino: https://github.com/amperka/ino
    '''
    minprog = 'void setup(){};void loop(){};'

    def __init__(self,
                 mcu=None,
                 f_cpu=None,
                 board=None,
                 hwpack='arduino',
                 extra_lib=None,
                 ver=None,
                 backend='arscons',  # 'ino',
                 arduino_home=None,
                 avr_home=None,
                 ):
        '''
        :param home:  'auto' -> ARDUINO_HOME env var
        '''
#        assert board or mcu, (board,  mcu)
        assert not (board and mcu), (board, mcu)
        assert not (board and mcu), (board, mcu)

        if not board:
            if not mcu:
                mcu = 'atmega328p'
            if not f_cpu:
                f_cpu = 16000000

        if not arduino_home:
            arduino_home = os.environ.get('ARDUINO_HOME', None)
        self.arduino_home = arduino_home

        if not avr_home:
            avr_home = os.environ.get('AVR_HOME', None)
        if arduino_home and not avr_home:
            # serach for avr-gcc delivered by arduino
            avr_home = Path(
                arduino_home) / 'hardware' / 'tools' / 'avr' / 'bin'
            if not avr_home.exists():
                avr_home = None
        self.avr_home = avr_home

        self.board = board
        self.hwpack = hwpack
        self.mcu = mcu
        self.backend = backend
        self.f_cpu = f_cpu
        self.ver = ver
        self.extra_lib = extra_lib

        self.proc = None
        self.output = None

    def command_list(self):
        if self.backend == 'ino':
            return self.command_list_ino()
        if self.backend == 'arscons':
            return self.command_list_arscons()
        assert 0

    def command_list_ino(self):
        cmd = []
        cmd += ['ino', 'build']
#        if self.home:
#            cmd += ['-d' , self.home]

        if self.board:
            cmd += ['-m', self.board]

        if self.hwpack != 'arduino':
            raise NotImplementedError()

        if self.mcu:
            raise NotImplementedError()
        if self.f_cpu:
            raise NotImplementedError()

        if self.ver:
            raise NotImplementedError()

        if self.extra_lib:
            raise NotImplementedError()

        return cmd

    def command_list_arscons(self):
        '''command line as list'''
        cmd = []
        cmd += ['scons']

        if self.arduino_home:
            cmd += ['ARDUINO_HOME=' + self.arduino_home]
#        if os.environ.get('ARDUINO_HOME', None):
#            cmd += ['ARDUINO_HOME=' + os.environ.get('ARDUINO_HOME')]

        if self.avr_home:
            cmd += ['AVR_HOME=' + self.avr_home]

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

    def setup_sources(self, tempdir, sources):
        strings, files = separate_sources(sources)

        log.debug('version: %s', version.intversion())
        log.debug('''input sources:
  strings:
%s
  files:
%s
''' , ('\n----\n'.join(strings), '\n'.join(files)))

        allfiles = []
        for x in strings:
            f = tmpfile(x, tempdir, version.sketch_extension())
            allfiles += [f]

        for x in files:
            f = tempdir / x.namebase + version.sketch_extension()
            if x.parent.name == x.namebase:
                # copy other files from pde directory
                for y in x.parent.files():
                    if y != x:
                        y.copy(tempdir / y.name)

            # copy pde
            x.copy(f)

            allfiles += [f]
        log.debug('  converted to:\n%s', '\n'.join(allfiles))
        return allfiles

    def guess_projname(self, allfiles):
        for x in allfiles:
            if x.ext in version.all_sketch_extensions() and 'setup' in x.text() and 'loop' in x.text():
                projname = x.namebase
                break

        assert projname
        return projname

    def build(self, sources=None):
        if self.backend == 'ino':
            self.build_ino(sources=sources)
        elif self.backend == 'arscons':
            self.build_arscons(sources=sources)
        else:
            assert 0

    def build_ino(self, sources=None):
        # TODO: remove tempdir
        tempdir = tmpdir(dir=tmpdir())
        lib = tempdir / 'lib'
        src = tempdir / 'src'
        build = tempdir / '.build'
        lib.mkdir()
        src.mkdir()

        self.setup_sources(src, sources)
        cmd = self.command_list()

        self.proc = Proc(cmd, cwd=tempdir).call()
        if not self.ok:
            raise ArduinoCompileError(cmd, sources, self.error_text)
        self.output = build.walkfiles('*.elf')[0]

    def build_arscons(self, sources=None):
        # TODO: remove tempdir
        tempdir = tmpdir(dir=tmpdir())

        SConstruct = Path(__file__).parent / 'SConstruct'
        SConstruct.copy(tempdir / 'SConstruct')

        allfiles = self.setup_sources(tempdir, sources)
        projname = self.guess_projname(allfiles)
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
            return sorted([line for line in self.stderr.splitlines() if 'warning:' in line])

    @property
    def ok(self):
        if self.proc:
            return self.proc.return_code == 0

# atmega32u4
# USB_VID is not supported
TARGETS = '''
atmega168
atmega328p
atmega8
atmega88
atmega1280
atmega2560
'''


def targets():
    return sorted(TARGETS.strip().split())

# def targets(uniq_mcu=False):
# #    if home:
# #        set_arduino_path(home)
#    ls = []
#    oldmcus = []
#    for h in hwpacklist.hwpack_names():
#        for b in boardlist.board_names(h):
#            mcu = mculist.mcu(b, h)
#            # TODO: not working
#            if b in 'atmega8u2 attiny861 sanguino'.split():
#                continue
#            if not uniq_mcu or mcu not in oldmcus:
#                print mcu
#                cc = Arduino(board=b,
#                             hwpack=h,
#                             mcu=mcu,
#                             #                             home=home,
#                             )
#                cc.board_options = boardlist.boards(h)[b]
#                ls += [cc]
#                oldmcus += [mcu]
#    return ls

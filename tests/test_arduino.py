from nose.tools import eq_, ok_, raises
from path import path
from pyavrutils.arduino import Arduino, ArduinoCompileError, targets
from pyavrutils.util import tmpdir
import os


# avr-gcc 4.7 compile error with old arduino versions
ARDUINO_VERSIONS = [
    # '0022',
    #                  '0023',
    # '1.0',
    '1.0.3',
]

def set_arduino_home(version):
    h = path('~/opt/arduino-{0}'.format(version)).expanduser()
    os.environ['ARDUINO_HOME'] = h
    
def setup():
    "set up test fixtures"
    set_arduino_home(ARDUINO_VERSIONS[-1])  # latest
    
def test():
    cc = Arduino()
    cc.build(cc.minprog)
    size = cc.size()
    assert size.program_bytes > 0
    assert size.program_percentage > 0
    assert size.data_bytes > 0
    assert size.data_percentage > 0

def test_targets_list():
    ok_(len(targets()))

def test_targets():
    boards = 'lilypad mega2560 mega'.split()
    for ver in ARDUINO_VERSIONS:
        set_arduino_home(ver)
        for b in boards:

            cc = Arduino(
                board=b,
                #                             home=h,
            )

            try:
                cc.build(path(__file__).parent / 'min.pde')
                print '    program size =', cc.size().program_bytes
                cc.build(cc.minprog)
                print '    program size =', cc.size().program_bytes
            except ArduinoCompileError, e:
                print '    compile error:', cc.error_text.splitlines()
                raise e

def test_bad_dir():
    d = tmpdir() / 'Bad'
    d.makedirs()
    f = d / 'Foo.pde'
    f.write_text(Arduino.minprog)
    Arduino().build(f)

def test_file():
    d = tmpdir() / 'Foo'
    d.makedirs()
    f = d / 'Foo.pde'
    f.write_text(Arduino.minprog)
    Arduino().build(f)

def test_more_files():
    d = tmpdir() / 'Foo'
    d.makedirs()
    f = d / 'Foo.pde'
    f.write_text('#include "x.h" \n int x=foo; \n' + Arduino.minprog)
    (d / 'x.h').write_text('#define foo 3')
    Arduino().build(f)


def test_params():
    Arduino(mcu='atmega88', f_cpu=1000000)
    Arduino(mcu='atmega88')
    Arduino(board='mega')
    Arduino(f_cpu=1000000)
    Arduino(board='mega', f_cpu=1000000)


@raises(Exception)
def test_exc():
    Arduino(board='mega', mcu='atmega88')

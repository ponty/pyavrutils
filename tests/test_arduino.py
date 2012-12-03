from nose.tools import eq_, ok_
from path import path
from pyavrutils.arduino import Arduino, ArduinoCompileError, targets
from pyavrutils.util import tmpdir
from unittest import TestCase
import os

ARDUINO_VERSIONS = [
    '0022',
    #                  '0023',
    '1.0',
]


class Test(TestCase):
    def test(self):
        cc = Arduino()
        cc.build(cc.minprog)
        size = cc.size()
        assert size.program_bytes > 0
        assert size.program_percentage > 0
        assert size.data_bytes > 0
        assert size.data_percentage > 0

    def test_targets_list(self):
        ok_(len(targets()))

    def test_targets(self):
        boards = 'lilypad mega2560 mega'.split()
        for ver in ARDUINO_VERSIONS:
            h = path('~/opt/arduino-{0}'.format(ver)).expanduser()
            os.environ['ARDUINO_HOME'] = h
#            for cc in targets(home=h):
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

    def test_bad_dir(self):
        d = tmpdir() / 'Bad'
        d.makedirs()
        f = d / 'Foo.pde'
        f.write_text(Arduino.minprog)
        Arduino().build(f)

    def test_file(self):
        d = tmpdir() / 'Foo'
        d.makedirs()
        f = d / 'Foo.pde'
        f.write_text(Arduino.minprog)
        Arduino().build(f)

    def test_more_files(self):
        d = tmpdir() / 'Foo'
        d.makedirs()
        f = d / 'Foo.pde'
        f.write_text('#include "x.h" \n int x=foo; \n' + Arduino.minprog)
        (d / 'x.h').write_text('#define foo 3')
        Arduino().build(f)

#    def test_more_pde(self):
#        d = tmpdir() / 'Foo'
#        d.makedirs()
#        f = d / 'Foo.pde'
#        f.write_text('''
#        #include "x.h"
#        int x=foo;
#        ''' + Arduino.minprog)
#        (d / 'x.h').write_text('''
#        #define foo 3
#
#        class X
#        {
#        void fun();
#        };
#        ''')
#        (d / 'x.pde').write_text('''
#        //#include "x.h"
#
#        void X::fun()
#        {
#            int x=foo;
#        }
#        ''')
#        Arduino().build(f)

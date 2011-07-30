from nose.tools import eq_
from pyavrutils.arduino import Arduino, ArduinoCompileError
from pyavrutils.util import tmpdir
from unittest import TestCase


class Test(TestCase):
    def test(self):
        cc = Arduino()
        cc.build(cc.minprog)
        size = cc.size()
        assert size.program_bytes > 0
        assert size.program_percentage > 0
        assert size.data_bytes > 0
        assert size.data_percentage > 0


    def test_targets(self):
        cc = Arduino()
        for mcu in cc.targets:
            cc.mcu = mcu
            try:
                cc.build(cc.minprog)
                print '    program size =', cc.size().program_bytes
            except ArduinoCompileError:
                print '    compile error:', cc.error_text.splitlines()
                raise ArduinoCompileError
    
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

    def test_more_pde(self):
        d = tmpdir() / 'Foo'
        d.makedirs()
        f = d / 'Foo.pde'
        f.write_text('''
#include "x.h" 
int x=foo; 
''' + Arduino.minprog)
        (d / 'x.h').write_text('''
#define foo 3

class X
{
void fun();
};
        ''')
        (d / 'x.pde').write_text('''
//#include "x.h" 

void X::fun()
{
    int x=foo;
}
        ''')
        Arduino().build(f)

        

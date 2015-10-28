from nose.tools import eq_
from pyavrutils import AvrGcc
from pyavrutils.avrgcc import AvrGccCompileError
from unittest import TestCase


class Test(TestCase):
    def test(self):
        cc = AvrGcc()
        assert len(cc.version()) > 0

        cc.build(cc.minprog)
        size = cc.size()
        assert size.program_bytes > 0
        assert size.program_percentage > 0

        eq_(size.data_bytes, 0)
        eq_(size.data_percentage, 0)

        cc.build('volatile int x=5; int main(){return x;}')
        size = cc.size()
        assert size.data_bytes > 0
        assert size.data_percentage > 0

    def test_targets(self):
        cc = AvrGcc()
        assert len(cc.targets)
        for mcu in cc.targets:
            cc.mcu = mcu
            try:
                cc.build(cc.minprog)
                print( '    program size = %s' % cc.size().program_bytes )
            except AvrGccCompileError:
                print( '    compile error: %s' % cc.error_text.splitlines()[0] )

    def test_headers(self):
        cc = AvrGcc()
        cc.build('''
        #include "x.h"
        int main()
        {
        return DEF;
        }
        ''',
                 {'x.h':
                  '#define DEF 3'
                  })

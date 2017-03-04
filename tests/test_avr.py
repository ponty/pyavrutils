from nose.tools import eq_
from pyavrutils import AvrGcc
from pyavrutils.avrgcc import AvrGccCompileError


def test():
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


def test_targets():
    cc = AvrGcc()
    assert len(cc.targets)
    for mcu in cc.targets:
        cc.mcu = mcu
        try:
            cc.build(cc.minprog)
            print('    program size = %s' % cc.size().program_bytes)
        except AvrGccCompileError:
            print('    compile error: %s' % cc.error_text.splitlines()[0])


def test_headers():
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


def test_fcpu():
    cc = AvrGcc()
    cc.f_cpu = 1111
    cc.build('''
#include <util/delay.h>
#if( F_CPU != 1111)
#error F_CPU
#endif
int main ()
{
    long f = F_CPU;
}
    ''')

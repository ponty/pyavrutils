from pyavrutils.avrgcc import AvrGcc
from entrypoint2 import entrypoint

templ = '''
#include <avr/io.h>
#include <util/delay.h>
int main()
{
    %s;
    return 0;
}
'''

cc = AvrGcc()
cc.optimize_no()
print  'compiler version:', cc.version()
print

def test(code_snippet, option=''):
    print  code_snippet.ljust(33) , 
    cc.options_extra = option.split()
    print  'compiler option:', option, '\t',
    try:
        cc.build([templ % code_snippet])
        size = cc.size()
        print 'program, data =', str(size.program_bytes).rjust(8) , ',', str(size.data_bytes).rjust(8)
    except:
        print  'compile error'

@entrypoint
def main():
    cc.optimization = 0

    test('_delay_ms(4)', '-O0')
    test('_delay_ms(4)', '-O1')
    test('_delay_ms(4)', '-O2')
    test('_delay_ms(4)', '-O3')
    test('_delay_ms(4)', '-Os')

    test('volatile double x=3;_delay_ms(x)', '-Os')

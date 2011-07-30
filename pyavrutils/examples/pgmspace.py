from pyavrutils.avrgcc import AvrGcc
from entrypoint2 import entrypoint

templ = '''
#include <avr/io.h>
#include <avr/pgmspace.h>
int main()
{
    %s;
    return 0;
}
'''

cc = AvrGcc()
cc.optimization=0
print  'compiler version:', cc.version()
print  'compiler options:', ' '.join(cc.options_generated())
print

def test(snippet):
    print  snippet ,'\t\t',
    try:
        cc.build([templ % snippet])
        size = cc.size()
        print 'program, data =', str(size.program_bytes).rjust(8) , ',', str(size.data_bytes).rjust(8)
    except:
        print  'compile error'


def test_comb(s):
    words='static const PROGMEM'.split()
    def choice(i):
        return [words[i],' '*len(words[i])]
    
    for s0 in choice(0):
        for s1 in choice(1):
            for s2 in choice(2):
#                    for s3 in choice(3):
                        test('%s %s char s[] %s = "%s"' % (s0,s1,s2,s))
@entrypoint
def main():
    test_comb("12345")
    test_comb("1234512345")




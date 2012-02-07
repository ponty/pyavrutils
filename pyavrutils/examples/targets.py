'''
print all available MCUs
'''

from entrypoint2 import entrypoint
from pyavrutils.avrgcc import AvrGcc

@entrypoint
def main():
    cc = AvrGcc()
    print '--------------'
    print 'avr-gcc'
    print '--------------'
    
    print 'compiler version:', cc.version()
    cc.optimize_for_size()
    print
    for mcu in cc.targets:
        print mcu


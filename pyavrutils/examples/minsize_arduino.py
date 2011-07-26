'''
test minimum program size with all MCUs
'''

from entrypoint2 import entrypoint
from pyavrutils.arduino import Arduino

def test(cc, mcu):
    print 'MCU =', mcu.ljust(20),
    cc.mcu = mcu
    cc.build(cc.minprog)
    print '    program/data size =', cc.size().program_bytes, ',', cc.size().data_bytes

@entrypoint
def main():
    cc = Arduino()
#    print 'compiler version:', cc.version()
    print 'code:', cc.minprog
    print
    for mcu in cc.targets:
        test(cc, mcu)

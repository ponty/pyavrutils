'''
test minimum program size with all MCUs
'''

from entrypoint2 import entrypoint
from pyavrutils.arduino import Arduino, targets

def test(cc):
    print 'MCU =', cc.mcu.ljust(20),
    cc.build(cc.minprog)
    print '    program/data size =', cc.size().program_bytes, ',', cc.size().data_bytes

@entrypoint
def main():
    cc = Arduino()
#    print 'compiler version:', cc.version()
    print 'code:', cc.minprog
    print
    for cc in targets(uniq_mcu=True):
        test(cc)

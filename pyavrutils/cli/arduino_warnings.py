
from entrypoint2 import entrypoint
from pyavrutils.arduino import Arduino


@entrypoint    
def warnings(filename):
    '''
    display compiler warnings
    '''
    cc = Arduino()
    cc.build(filename)
    print( '\n'.join(cc.warnings))



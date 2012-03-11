
from entrypoint2 import entrypoint
from pyavrutils.arduino import Arduino


@entrypoint    
def warnings(filename, 
                 board='pro',
                 hwpack='arduino',
                 mcu='',
                 f_cpu='',
                 extra_lib='',
                 ver='' ,
#                 home='auto',
                 backend='arscons',
             ):
    '''
    build Arduino sketch and display compiler warnings
    '''
    cc = Arduino(
                 board=board,
                 hwpack=hwpack,
                 mcu=mcu,
                 f_cpu=f_cpu,
                 extra_lib=extra_lib,
                 ver=ver ,
#                 home=home,
                 backend=backend,
                 )
    cc.build(filename)
    print( '\n'.join(cc.warnings))



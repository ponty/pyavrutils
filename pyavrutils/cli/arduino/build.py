
from entrypoint2 import entrypoint
from pyavrutils.arduino import Arduino


@entrypoint
def warnings(filename,
             board='pro',
             hwpack='arduino',
             mcu='',
                 f_cpu='',
                 extra_lib='',
                 ver='',
             #                 home='auto',
                 backend='arscons',
             ):
    '''
    build Arduino sketch and display results
    '''
    cc = Arduino(
        board=board,
        hwpack=hwpack,
        mcu=mcu,
        f_cpu=f_cpu,
        extra_lib=extra_lib,
        ver=ver,
        #                 home=home,
        backend=backend,
    )
    cc.build(filename)

    print 'backend:', cc.backend
    print 'MCU:', cc.mcu_compiler()
#    print 'avr-gcc:', AvrGcc().version()

    print
    print('=============================================')
    print('SIZE')
    print('=============================================')
    print 'program:', cc.size().program_bytes
    print 'data:', cc.size().data_bytes

    core_warnings = [x for x in cc.warnings if 'gcc' in x] + [
        x for x in cc.warnings if 'core' in x]
    lib_warnings = [x for x in cc.warnings if 'lib_' in x]
    notsketch_warnings = core_warnings + lib_warnings
    sketch_warnings = [x for x in cc.warnings if x not in notsketch_warnings]

    print
    print('=============================================')
    print('WARNINGS')
    print('=============================================')
    print
    print('core')
    print('-------------------')
    print('\n'.join(core_warnings))
    print
    print('lib')
    print('-------------------')
    print('\n'.join(lib_warnings))
    print
    print('sketch')
    print('-------------------')
    print('\n'.join(sketch_warnings))

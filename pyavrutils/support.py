from confduino import version
from path import path
from pyavrutils import arduino
from pyavrutils.arduino import Arduino, ArduinoCompileError
import confduino
import csv

def find_examples(root):
    root = path(root)
    examples=[]
    for e in version.all_sketch_extensions():
        examples += [x for x in root.walkfiles('*'+e) if x.parent.name == x.namebase]
    return examples

def build2csv(sources, csv_path, logdir, extra_lib=None, logger=None):
    csv_path = path(csv_path).abspath()
    if not logger:
        logger = (lambda x:x)
        
#    if not logdir:
#        logdir = csv_path.parent
    logdir = path(logdir).abspath()
    if not logdir.exists():
        logdir.makedirs()
    
#    cc = Arduino(extra_lib=extra_lib)
    targets = arduino.targets()
    
    fx = open(csv_path, 'wb')
    writer = csv.writer(fx)
    logger('generating ' + csv_path)

#    writer.writerow([
#                     'source',
#                     ] + range(len(targets)))
    writer.writerow([
                     'index',
                     'board',
                     ] + [ex.namebase for ex in sources])

    if not hasattr(build2csv,'index'):
        build2csv.index = 0
    for cc in targets:
        build2csv.index += 1
        index=build2csv.index
        
        logger('building target: ' + cc.board)
        outs = []
        for ex in sources:
            cc.extra_lib = extra_lib
            ok = False
            try:
                cc.build(ex)
                ok = True
            except ArduinoCompileError:
                pass
            logfile = logdir / ('generated_buildlog_%s_%s.txt' % (ex.namebase, index)) 
            logfile.write_text('----------\nstdout\n----------\n%s\n\n----------\nstderr\n----------\n%s'% (cc.proc.stdout,cc.error_text))

            if ok:
                avr_size=cc.size()
                if avr_size.ok:
                    label='OK'
                else:
                    label='BIG'
                label+=' (P:%s D:%s)' % ( avr_size.program_bytes, avr_size.data_bytes)
            else:
                label='ERR'
            # anonymous link: __
            outs += ['`%s <%s>`__' % (label,logfile.name)]
    

        writer.writerow([
                         index,
#                         ex.namebase,
                        cc.board,
                         ] + outs)
    
    
def boards2csv(csv_path, logger=None):
    csv_path = path(csv_path).abspath()
    if not logger:
        logger = (lambda x:x)
        
    targets = arduino.targets()
    
    fx = open(csv_path, 'wb')
    writer = csv.writer(fx)
    logger('generating ' + csv_path)

    writer.writerow('index package id name MCU F_CPU'.split())

    if not hasattr(boards2csv,'index'):
        boards2csv.index = 0
    for cc in targets:
        boards2csv.index += 1
        index=boards2csv.index
        
        writer.writerow([
                         index,
                         cc.hwpack,
                         cc.board,
                         cc.board_options.name,
                         cc.board_options.build.mcu,
                         cc.board_options.build.f_cpu,
                         ])
    
def set_arduino_path(directory):
    confduino.set_arduino_path(directory)

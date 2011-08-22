from path import path
from pyavrutils import arduino
from pyavrutils.arduino import Arduino, ArduinoCompileError
import csv

def find_examples(root):
    root = path(root)
    examples = [x for x in root.walkfiles('*.pde') if x.parent.name == x.namebase]
    return examples

def build2csv(sources, csv_path, logdir, extra_lib=None, logger=None, filter=True):
    csv_path = path(csv_path).abspath()
    if not logger:
        logger = (lambda x:x)
        
#    if not logdir:
#        logdir = csv_path.parent
    logdir = path(logdir).abspath()
    if not logdir.exists():
        logdir.makedirs()
    
#    cc = Arduino(extra_lib=extra_lib)
    targets = arduino.targets(filter=filter)
    
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

    index = 0
    for cc in targets:
        index += 1
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
                label='OK'
#                TODO: fix arduino size first
#                if cc.size().ok:
#                    label='OK'
#                else:
#                    label='BIG'
            else:
                label='ERR'
            # anonymous link: __
            outs += ['`%s <%s>`__' % (label,logfile.name)]
    

        writer.writerow([
                         index,
#                         ex.namebase,
                        cc.board,
                         ] + outs)
    
    
def boards2csv(csv_path, logger=None,filter=False):
    csv_path = path(csv_path).abspath()
    if not logger:
        logger = (lambda x:x)
        
    targets = arduino.targets(filter=filter)
    
    fx = open(csv_path, 'wb')
    writer = csv.writer(fx)
    logger('generating ' + csv_path)

    writer.writerow('index package id name MCU F_CPU'.split())

    index = 0
    for cc in targets:
        index += 1
        writer.writerow([
                         index,
                         cc.hwpack,
                         cc.board,
                         cc.board_options.name,
                         cc.board_options.build.mcu,
                         cc.board_options.build.f_cpu,
                         ])
    

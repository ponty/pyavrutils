from pyavrutils.arduino import Arduino, ArduinoCompileError
import csv
from path import path

def find_examples(root):
    root = path(root)
    examples = [x for x in root.walkfiles('*.pde') if x.parent.name == x.namebase]
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
    
    cc = Arduino(extra_lib=extra_lib)
    
    fx = open(csv_path, 'wb')
    writer = csv.writer(fx)
    logger('generating ' + csv_path)

    writer.writerow([
                     'source',
                     ] + cc.targets)

    for ex in sources:
        logger('building file: ' + ex.name)
        outs = []
        for mcu in cc.targets:
            cc.mcu = mcu
            ok = False
            try:
                cc.build(ex)
                ok = True
            except ArduinoCompileError:
                pass
            logfile = logdir / ('generated_buildlog_%s_%s.txt' % (ex.namebase, mcu))
            logfile.write_text(cc.error_text)
            # anonymous link: __
            outs += ['`OK <%s>`__' % logfile.name if ok else '`ERROR <%s>`__' % logfile.name]
    

        writer.writerow([
                         ex.name,
                         ] + outs)
    

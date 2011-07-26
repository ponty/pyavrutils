from easyprocess import Proc
from unipath.path import Path

class AvrSizeError(Exception):
    pass

class AvrSize(object):
    '''
    wrapper for avr-size
    '''
    def __init__(self):
        self.program_bytes = 0
        self.data_bytes = 0
        self.program_percentage = 0
        self.data_percentage = 0
        
    def __repr__(self):
        return 'AvrSize <prog:%s bytes %s%% mem:%s bytes %s%% >' % (self.program_bytes, self.program_percentage, self.data_bytes, self.data_percentage)
        
    def parse_output(self, s):
        '''
        Example output:
    
        AVR Memory Usage
        ----------------
        Device: atmega2561
    
        Program:    4168 bytes (1.6% Full)
        (.text + .data + .bootloader)
    
        Data:         72 bytes (0.9% Full)
        (.data + .bss + .noinit)
        '''

        for x in s.splitlines():
            if '%' in x:
                name = x.split(':')[0].strip().lower()
                bytes = x.split(':')[1].split('b')[0].strip()
                bytes = int(bytes)
                perc = x.split('(')[1].split('%')[0].strip()
                perc = float(perc)
                if name == 'program':
                    self.program_bytes = bytes
                    self.program_percentage = perc
                else:
                    self.data_bytes = bytes
                    self.data_percentage = perc
    
    
    def run(self, objfile, mcu):
    
        objfile = Path(objfile).absolute()
        if not objfile.exists():
            raise AvrSizeError('no hex file! ' + objfile.absolute())
        cmd = 'avr-size --format=avr --mcu={mcu} {objfile}'.format(objfile=objfile, mcu=mcu)
        p = Proc(cmd).call()
        self.parse_output(p.stdout)

    @property
    def ok(self):
        return self.program_bytes > 0 and self.program_percentage <= 100 and self.data_percentage <= 100

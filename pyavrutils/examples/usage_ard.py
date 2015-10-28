from entrypoint2 import entrypoint


code = '''
from pyavrutils import Arduino
cc = Arduino(board='mini')
cc.build('void setup(){};void loop(){}')
cc.output
cc.size()
cc.size().program_bytes
cc.board='pro'
cc.build('void setup(){};void loop(){}')
cc.output
cc.size().program_bytes
cc.warnings
'''

@entrypoint
def main():
    for line in code.strip().splitlines():
        print('>>> %s' % line)
        try:
            s = eval(line)
            if s:
                print(s)
        except SyntaxError:
            exec(line)
            
        
                

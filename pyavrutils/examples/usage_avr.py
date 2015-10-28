from entrypoint2 import entrypoint


code = '''
from pyavrutils import AvrGcc
cc = AvrGcc(mcu='atmega48')
cc.targets
cc.options_generated()
cc.build('int main(){}')
cc.output
cc.size()
cc.size().program_bytes
cc.mcu='atmega168'
cc.options_generated()
cc.build('int main(){}')
cc.output
cc.size().program_bytes
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
            
        
                

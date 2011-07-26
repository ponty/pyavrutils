from nose.tools import eq_
from pyavrutils.arduino import Arduino, ArduinoCompileError
from unittest import TestCase


class Test(TestCase):
    def test(self):
        cc = Arduino()
        cc.build(cc.minprog)
        size = cc.size()
        assert size.program_bytes > 0
        assert size.program_percentage > 0
        assert size.data_bytes > 0
        assert size.data_percentage > 0


    def test_targets(self):
        cc = Arduino()
        for mcu in cc.targets:
            cc.mcu = mcu
            try:
                cc.build(cc.minprog)
                print '    program size =', cc.size().program_bytes
            except ArduinoCompileError:
                print '    compile error:', cc.error_text.splitlines()
                raise ArduinoCompileError

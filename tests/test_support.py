from nose.tools import eq_
from path import path
from pyavrutils import support

def test(): 
    root = path(__file__).parent.parent.abspath()
    examples = support.find_examples(root)
    eq_(len(examples),0)

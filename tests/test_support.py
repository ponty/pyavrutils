from nose.tools import eq_
from path import Path
from pyavrutils import support


def test():
    root = Path(__file__).parent.parent.abspath()
    examples = support.find_examples(root)
    eq_(len(examples), 0)

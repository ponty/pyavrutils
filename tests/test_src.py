from nose.tools import eq_
from pyavrutils.util import separate_sources


def test_separate_sources():
    eq_(separate_sources('int main(){}'), (['int main(){}'],[]))
    eq_(separate_sources(['int main(){}']), (['int main(){}'],[]))
    eq_(separate_sources(['int main(){}','int main(){}']), (['int main(){}','int main(){}'],[]))

    eq_(separate_sources('main.c'), ([],['main.c']))
    eq_(separate_sources(['main.c']), ([],['main.c']))
    eq_(separate_sources(['main.c','main2.c']), ([],['main.c','main2.c']))
    
from path import path
import tempfile

PREFIX = 'pyavrutils_'
def tmpdir (dir=None, suffix=''):
    x = tempfile.mkdtemp(suffix=suffix, prefix=PREFIX, dir=dir)
    return path(x)

def tmpfile(text, dir, ext):
    f = tempfile.NamedTemporaryFile(prefix=PREFIX, suffix=ext, delete=0, dir=dir)
    f.write(text)
    f.close()
    return path(f.name)

def rename(old, new):
    old.rename(new)
    return new 
    
def normalize_list(ls):
    if not ls:
        ls = []
         
    if hasattr(ls, '__iter__'):
        # list
        pass
    else:
        # string
        ls = [ls]

    ls = [x for x in  ls if x]
    ls = [x.strip() for x in  ls ]
    ls = [x for x in  ls if len(x)]
    return ls

def separate_sources(sources):
    sources = normalize_list(sources)

    def is_code(s):
        if '\n' in s:
            return 1
        if '{' in s:
            return 1
        return 0
    strings = [x for x in  sources if is_code(x)]
    files = [path(x) for x in  sources if not is_code(x)]
    return strings, files

class CompileError(Exception):
    def __init__(self, cmd, sources, error_text):
        msg = 'compile error! ' 
        msg += '\n cmd =' + str(cmd) 
        msg += '\n sources= ' + str(sources) 
        msg += '\n error_text=' 
        msg += '\n   ' + '\n   '.join( ([x for x in error_text.splitlines() if 'error:' in x or 'undefined reference' in x ]))
#        msg += '\n error_text=' + str(error_text)
        Exception.__init__(self, msg)

from paved import *
from paved.dist import *
from paved.docs import *
from paved.pkg import *
from paved.pycheck import *
from paved.util import *
from paver.easy import *
from paver.setuputils import setup
from pyavrutils import support
from setuptools import find_packages
from sphinxcontrib import paverutils
import logging
import os
import paver.doctools
import paver.misctasks


#logging.basicConfig(
#                level=logging.DEBUG,
#                format='%(asctime)-6s: %(name)s - %(levelname)s - %(message)s',
#                )

# get info from setup.py
setup_py=''.join([x for x in path('setup.py').lines() if 'setuptools' not in x])
exec(setup_py)


options(
    sphinx=Bunch(
        docroot='docs',
        builddir="_build",
        ),
    pdf=Bunch(
        builddir='_build',
        builder='latex',
    ),
    )

options.paved.clean.rmdirs +=   ['.tox',
                                 'dist',
                                 'build' ,
                                 ]
options.paved.clean.patterns += ['*.pickle',
                                 '*.doctree',
                                 '*.gz' ,
                                 'nosetests.xml',
                                 'sloccount.sc',
                                 '*.pdf', '*.tex',
                                 '*.png',
                                 'generated*',
                                 '*.zip',   
                                 'distribute_setup.py',
                                 ]

options.paved.dist.manifest.include.remove('distribute_setup.py')
options.paved.dist.manifest.include.remove('paver-minilib.zip')
options.paved.dist.manifest.recursive_include.add('pyavrutils SConstruct*')
options.paved.dist.manifest.include.add('requirements.txt')

docroot = path(options.sphinx.docroot)


@task
@needs(
#           'clean',
       'sloccount', 
       'boards', 
       'build_test', 
       'html', 
       'pdf', 
       'pdf', 
       'sdist', 
       'nose',   'tox',
       )
def alltest():
    'all tasks to check'
    pass

@task
@needs('sphinxcontrib.paverutils.html')
def html():
    pass

@task
@needs('sphinxcontrib.paverutils.pdf')
def pdf():
    fpdf = list(path('docs/_build/latex').walkfiles('*.pdf'))[0]
    d = path('docs/_build/html')
    d.makedirs()
    fpdf.copy(d)

ARDUINO_VERSIONS=[
                  '0022', 
                  '0023', 
                  '1.0',
                  ]

@task
def build_test():
    for ver in ARDUINO_VERSIONS:
#            support.set_arduino_path('~/opt/arduino-{0}'.format(ver))
        os.environ['ARDUINO_HOME'] = path('~/opt/arduino-{0}'.format(ver)).expanduser()
        csv = docroot / 'generated_build_test_{0}.csv'.format(ver)
        support.build2csv(
                          [path('tests/min.pde')], 
                          csv, 
                          logdir=docroot / '_build' / 'html', 
                          logger=info, 
                          )

@task
def boards():
    for ver in ARDUINO_VERSIONS:
        os.environ['ARDUINO_HOME'] = path('~/opt/arduino-{0}'.format(ver)).expanduser()
        csv = docroot / 'generated_boards_{0}.csv'.format(ver)
        support.boards2csv(csv, logger=info)

    
@task
def tox():
    '''Run tox.'''
    sh('tox')
    
@task
@needs('manifest', 'setuptools.command.sdist')
def sdist():
    """Overrides sdist to make sure that our MANIFEST.in is generated.
    """
    pass

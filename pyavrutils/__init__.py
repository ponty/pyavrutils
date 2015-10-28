import logging
from pyavrutils.about import __version__


log = logging.getLogger(__name__)
# log=logging

log.debug('version=' + __version__)

from avrgcc import *
from avrsize import *
from arduino import *

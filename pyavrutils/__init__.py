import logging

__version__ = '0.1.0'

log = logging.getLogger(__name__)
#log=logging

log.debug('version=' + __version__)

from avrgcc import *
from avrsize import *
from arduino import *

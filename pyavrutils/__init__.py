import logging

__version__ = '0.0.7'

log = logging.getLogger(__name__)
#log=logging

log.debug('version=' + __version__)

from avrgcc import *
from avrsize import *
from arduino import *

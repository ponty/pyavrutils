pyavrutils can build AVR_ and arduino_ code from python_

Links:
 * home: https://github.com/ponty/pyavrutils
 * documentation: http://ponty.github.com/pyavrutils

Features:
 - python wrapper for avr-gcc, avr-size, arscons_
 - build files or strings (strings are saved as temp files)
 - MCU list 
 - get code size using avr-size
 - avr-gcc default is optimized for size

Known problems:
 - Python 3 is not supported
 - temp files are not removed
 - arscons_ has some problems:
     - it builds bigger programs
     - compile error in some cases
 
Possible usage:
 - experimenting with flags
 - building from paver_
 - unit tests
 - building arduino_ code without GUI
  
Basic usage
============

    >>> from pyavrutils import AvrGcc
    >>> cc = AvrGcc()
    >>> cc.build('int main(){}')
    >>> cc.size().program_bytes
    66
    
    >>> from pyavrutils import Arduino
    >>> cc = Arduino()
    >>> cc.mcu = 'atmega8'
    >>> cc.build('void setup(){};void loop(){}')
    >>> cc.size().program_bytes
    1612

Installation
============

General
--------

 * arscons_ is already included in the library  
 * install pip_
 * install gcc-avr
 * install scons_ (only for arscons_)
 * install arduino_ (only for arscons_)
 * install the program:

if you have setuptools_ installed::

    # as root
    pip install pyavrutils

Ubuntu
----------
::

    sudo apt-get install python-pip
    sudo apt-get install binutils-avr
    sudo apt-get install gcc-avr
    sudo apt-get install scons
    sudo apt-get install arduino
    sudo pip install pyavrutils

Uninstall
----------

using pip_::

    # as root
    pip uninstall pyavrutils


.. _setuptools: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _pip: http://pip.openplans.org/
.. _arscons: http://code.google.com/p/arscons/
.. _arduino: http://arduino.cc/
.. _python: http://www.python.org/
.. _avr: http://en.wikipedia.org/wiki/Atmel_AVR
.. _paver: http://paver.github.com/paver/
.. _scons: http://www.scons.org

pyavrutils is a Python library that can build AVR_ and arduino_ code at runtime.

Links:
 * home: https://github.com/ponty/pyavrutils
 * documentation: http://pyavrutils.readthedocs.org
 * PYPI: https://pypi.python.org/pypi/pyavrutils

|Travis| |Coveralls| |Latest Version| |Supported Python versions| |License| |Code Health| |Documentation|

Features:
 - python wrapper for avr-gcc, avr-size, arscons_
 - build files or strings (strings are saved as temp files)
 - MCU list 
 - get code size using avr-size
 - avr-gcc default is optimized for size
 - supported python versions: 2.6, 2.7, 3.3, 3.4, 3.5

Known problems:
 - temp files are not removed
 - arscons_ does not perfectly matches the Arduino build process
 
Possible usage:
 - experimenting with flags
 - unit tests
 - building arduino_ code without GUI
  
Basic usage
===========

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
-------

 * arscons_ is already included in the library  
 * install pip_
 * install gcc-avr
 * install scons_ (only for arscons_)
 * install arduino_ (only for arscons_)
 * install the program:

if you have setuptools_ installed::

    # as root
    pip install pyavrutils

Ubuntu 14.04
------------
::

    sudo apt-get install python-pip
    sudo apt-get install binutils-avr gcc-avr scons arduino
    sudo pip install pyavrutils
    # optional for examples:
    sudo pip install entrypoint2

Uninstall
---------

using pip_::

    # as root
    pip uninstall pyavrutils

Usage
=====

AVR::

  #-- sh('python -m pyavrutils.examples.usage_avr ')--#
  >>> from pyavrutils import AvrGcc
  >>> cc = AvrGcc(mcu='atmega48')
  >>> cc.targets
  [u'at43usb320', u'at43usb355', u'at76c711', u'at86rf401', u'at90c8534', u'at90can128', u'at90can32', u'at90can64', u'at90pwm1', u'at90pwm161', u'at90pwm2', u'at90pwm216', u'at90pwm2b', u'at90pwm3', u'at90pwm316', u'at90pwm3b', u'at90pwm81', u'at90s1200', u'at90s2313', u'at90s2323', u'at90s2333', u'at90s2343', u'at90s4414', u'at90s4433', u'at90s4434', u'at90s8515', u'at90s8535', u'at90scr100', u'at90usb1286', u'at90usb1287', u'at90usb162', u'at90usb646', u'at90usb647', u'at90usb82', u'at94k', u'ata5272', u'ata5505', u'ata5790', u'ata5790n', u'ata5795', u'ata6285', u'ata6286', u'ata6289', u'atmega103', u'atmega128', u'atmega1280', u'atmega1281', u'atmega1284', u'atmega1284p', u'atmega128a', u'atmega128rfa1', u'atmega16', u'atmega161', u'atmega162', u'atmega163', u'atmega164a', u'atmega164p', u'atmega164pa', u'atmega165', u'atmega165a', u'atmega165p', u'atmega165pa', u'atmega168', u'atmega168a', u'atmega168p', u'atmega168pa', u'atmega169', u'atmega169a', u'atmega169p', u'atmega169pa', u'atmega16a', u'atmega16hva', u'atmega16hva2', u'atmega16hvb', u'atmega16hvbrevb', u'atmega16m1', u'atmega16u2', u'atmega16u4', u'atmega2560', u'atmega2561', u'atmega26hvg', u'atmega32', u'atmega323', u'atmega324a', u'atmega324p', u'atmega324pa', u'atmega325', u'atmega3250', u'atmega3250a', u'atmega3250p', u'atmega3250pa', u'atmega325a', u'atmega325p', u'atmega328', u'atmega328p', u'atmega329', u'atmega3290', u'atmega3290a', u'atmega3290p', u'atmega3290pa', u'atmega329a', u'atmega329p', u'atmega329pa', u'atmega32a', u'atmega32c1', u'atmega32hvb', u'atmega32hvbrevb', u'atmega32m1', u'atmega32u2', u'atmega32u4', u'atmega32u6', u'atmega406', u'atmega48', u'atmega48a', u'atmega48hvf', u'atmega48p', u'atmega48pa', u'atmega64', u'atmega640', u'atmega644', u'atmega644a', u'atmega644p', u'atmega644pa', u'atmega645', u'atmega6450', u'atmega6450a', u'atmega6450p', u'atmega645a', u'atmega645p', u'atmega649', u'atmega6490', u'atmega6490a', u'atmega6490p', u'atmega649a', u'atmega649p', u'atmega64a', u'atmega64c1', u'atmega64hve', u'atmega64m1', u'atmega64rfa2', u'atmega64rfr2', u'atmega8', u'atmega8515', u'atmega8535', u'atmega88', u'atmega88a', u'atmega88p', u'atmega88pa', u'atmega8a', u'atmega8hva', u'atmega8u2', u'atmxt112sl', u'atmxt224', u'atmxt224e', u'atmxt336s', u'atmxt540s', u'atmxt540sreva', u'attiny11', u'attiny12', u'attiny13', u'attiny13a', u'attiny15', u'attiny1634', u'attiny167', u'attiny22', u'attiny2313', u'attiny2313a', u'attiny24', u'attiny24a', u'attiny25', u'attiny26', u'attiny261', u'attiny261a', u'attiny28', u'attiny4313', u'attiny43u', u'attiny44', u'attiny44a', u'attiny45', u'attiny461', u'attiny461a', u'attiny48', u'attiny84', u'attiny84a', u'attiny85', u'attiny861', u'attiny861a', u'attiny87', u'attiny88', u'atxmega128a1', u'atxmega128a1u', u'atxmega128a3', u'atxmega128a3u', u'atxmega128a4u', u'atxmega128b1', u'atxmega128b3', u'atxmega128c3', u'atxmega128d3', u'atxmega128d4', u'atxmega16a4', u'atxmega16a4u', u'atxmega16c4', u'atxmega16d4', u'atxmega16x1', u'atxmega192a3', u'atxmega192a3u', u'atxmega192c3', u'atxmega192d3', u'atxmega256a3', u'atxmega256a3b', u'atxmega256a3bu', u'atxmega256a3u', u'atxmega256c3', u'atxmega256d3', u'atxmega32a4', u'atxmega32a4u', u'atxmega32c4', u'atxmega32d4', u'atxmega32e5', u'atxmega32x1', u'atxmega384c3', u'atxmega384d3', u'atxmega64a1', u'atxmega64a1u', u'atxmega64a3', u'atxmega64a3u', u'atxmega64a4u', u'atxmega64b1', u'atxmega64b3', u'atxmega64c3', u'atxmega64d3', u'atxmega64d4', u'avr1', u'avr2', u'avr25', u'avr3', u'avr31', u'avr35', u'avr4', u'avr5', u'avr51', u'avr6', u'avrxmega2', u'avrxmega4', u'avrxmega5', u'avrxmega6', u'avrxmega7', u'm3000']
  >>> cc.options_generated()
  ['avr-gcc', '-Df_cpu=4000000', '-mmcu=atmega48', '--std=gnu99', '-Wl,--relax', '-Wl,--gc-sections', '-ffunction-sections', '-fdata-sections', '-fno-inline-small-functions', '-Os']
  >>> cc.build('int main(){}')
  >>> cc.output
  /tmp/pyavrutils_MM2AL6.elf
  >>> cc.size()
  AvrSize <prog:80 bytes 2.0% mem:0 bytes 0.0% >
  >>> cc.size().program_bytes
  80
  >>> cc.mcu='atmega168'
  >>> cc.options_generated()
  ['avr-gcc', '-Df_cpu=4000000', '-mmcu=atmega168', '--std=gnu99', '-Wl,--relax', '-Wl,--gc-sections', '-ffunction-sections', '-fdata-sections', '-fno-inline-small-functions', '-Os']
  >>> cc.build('int main(){}')
  >>> cc.output
  /tmp/pyavrutils_MM2AL6.elf
  >>> cc.size().program_bytes
  132
  #-#
    

arduino::

  #-- sh('python -m pyavrutils.examples.usage_ard ')--#
  >>> from pyavrutils import Arduino
  >>> cc = Arduino(board='mini')
  >>> cc.build('void setup(){};void loop(){}')
  >>> cc.output
  /tmp/pyavrutils_6rOALC/pyavrutils_yhNZYl/pyavrutils_yhNZYl.elf
  >>> cc.size()
  AvrSize <prog:440 bytes 2.7% mem:9 bytes 0.9% >
  >>> cc.size().program_bytes
  440
  >>> cc.board='pro'
  >>> cc.build('void setup(){};void loop(){}')
  >>> cc.output
  /tmp/pyavrutils_pDz6aH/pyavrutils_pnu8A3/pyavrutils_pnu8A3.elf
  >>> cc.size().program_bytes
  440
  >>> cc.warnings
  [u'build/core/HardwareSerial.cpp:100:20: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]', u"build/core/HardwareSerial.cpp:129:21: warning: unused variable 'c' [-Wunused-variable]", u"build/core/HardwareSerial.cpp:370:11: warning: unused variable 'current_config' [-Wunused-variable]", u'build/core/HardwareSerial.cpp:469:27: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]']
  #-#

Examples
========

Simple example
--------------

Example program::

  #-- include('examples/simple.py')--#
  '''
  test minimum program size with different optimizations
  '''

  from pyavrutils import AvrGcc
  from entrypoint2 import entrypoint

  cc = AvrGcc()
  code = 'int main(){}'


  def test():
      print '    compiler option:', ' '.join(cc.options_generated())
      cc.build(code)
      print '    program size =', cc.size().program_bytes


  @entrypoint
  def main():
      print 'compiler version:', cc.version()
      print 'code:', code
      print
      print 'no optimizations::'
      print
      cc.optimize_no()
      test()
      print
      print 'optimize for size::'
      print
      cc.optimize_for_size()
      test()
  #-#

Output::

  #-- sh('python -m pyavrutils.examples.simple ')--#
  compiler version: 4.8.2
  code: int main(){}

  no optimizations::

      compiler option: avr-gcc -Df_cpu=4000000 -mmcu=atmega168 --std=gnu99
      program size = 150

  optimize for size::

      compiler option: avr-gcc -Df_cpu=4000000 -mmcu=atmega168 --std=gnu99 -Wl,--relax -Wl,--gc-sections -ffunction-sections -fdata-sections -fno-inline-small-functions -Os
      program size = 132
  #-#

Test size with unused code
--------------------------

Example program::

  #-- include('examples/deadcode.py')--#
  from pyavrutils.avrgcc import AvrGcc
  from entrypoint2 import entrypoint

  cc = AvrGcc()


  def test_option(sources, optimization, gc_sections=0, ffunction_sections=0):
      print 'optimization =', optimization,
      print 'gc_sections =', gc_sections,
      print 'ffunction_sections =', ffunction_sections,
      print

      cc.optimization = optimization
      cc.gc_sections = gc_sections
      cc.ffunction_sections = ffunction_sections
      try:
          cc.build(sources)
          size = cc.size()
          print 'program, data =', str(size.program_bytes).rjust(8), ',', str(size.data_bytes).rjust(8)
      except:
          print  'compile error'


  def test(sources):
      print 'sources:', sources
      test_option(sources, 0)
      test_option(sources, 's', 0)
      test_option(sources, 's', 1)
      test_option(sources, 's', 1, 1)


  @entrypoint
  def main():
      cc.optimize_no()
      print  'compiler version:', cc.version()
      print  'compiler options:', ' '.join(cc.options_generated())
      print
      print 'minimum size'
      print 20 * '='
      test(['int main(){}'])

      print
      print 'unused function in separate file'
      print 40 * '='
      test(['int main(){}', 'int f(){return 2;}'])

      print
      print 'unused function in the same file'
      print 40 * '='
      test(['int main(){}; int f(){return 2;}'])
  #-#

Output::

  #-- sh('python -m pyavrutils.examples.deadcode ')--#
  compiler version: 4.8.2
  compiler options: avr-gcc -Df_cpu=4000000 -mmcu=atmega168 --std=gnu99

  minimum size
  ====================
  sources: ['int main(){}']
  optimization = 0 gc_sections = 0 ffunction_sections = 0
  program, data =      150 ,        0
  optimization = s gc_sections = 0 ffunction_sections = 0
  program, data =      138 ,        0
  optimization = s gc_sections = 1 ffunction_sections = 0
  program, data =      138 ,        0
  optimization = s gc_sections = 1 ffunction_sections = 1
  program, data =      138 ,        0

  unused function in separate file
  ========================================
  sources: ['int main(){}', 'int f(){return 2;}']
  optimization = 0 gc_sections = 0 ffunction_sections = 0
  program, data =      168 ,        0
  optimization = s gc_sections = 0 ffunction_sections = 0
  program, data =      144 ,        0
  optimization = s gc_sections = 1 ffunction_sections = 0
  program, data =      138 ,        0
  optimization = s gc_sections = 1 ffunction_sections = 1
  program, data =      138 ,        0

  unused function in the same file
  ========================================
  sources: ['int main(){}; int f(){return 2;}']
  optimization = 0 gc_sections = 0 ffunction_sections = 0
  program, data =      168 ,        0
  optimization = s gc_sections = 0 ffunction_sections = 0
  program, data =      144 ,        0
  optimization = s gc_sections = 1 ffunction_sections = 0
  program, data =      138 ,        0
  optimization = s gc_sections = 1 ffunction_sections = 1
  program, data =      138 ,        0
  #-#


Test size with delay.h
----------------------

Example program::

  #-- include('examples/delaysize.py')--#
  from entrypoint2 import entrypoint
  from pyavrutils.avrgcc import AvrGcc, AvrGccCompileError

  templ = '''
  #include <avr/io.h>
  #include <util/delay.h>
  int main()
  {
      %s;
      return 0;
  }
  '''

  cc = AvrGcc()
  cc.optimize_no()
  print  'compiler version:', cc.version()
  print


  def test(snippet, option=''):
      print  snippet.ljust(33),
      cc.options_extra = option.split()
      print  'compiler option:', option, '\t',
      try:
          cc.build([templ % snippet])
          size = cc.size()
          print 'program, data =', str(size.program_bytes).rjust(8), ',', str(size.data_bytes).rjust(8)
      except AvrGccCompileError as e:
          print  'compile error'


  @entrypoint
  def main():
      cc.optimization = 0

      test('_delay_ms(4)', '-O0')
      test('_delay_ms(4)', '-O1')
      test('_delay_ms(4)', '-O2')
      test('_delay_ms(4)', '-O3')
      test('_delay_ms(4)', '-Os')
  #-#

Output::

  #-- sh('python -m pyavrutils.examples.delaysize ')--#
  compiler version: 4.8.2

  _delay_ms(4)                      compiler option: -O0 	program, data =      938 ,        0
  _delay_ms(4)                      compiler option: -O1 	program, data =      150 ,        0
  _delay_ms(4)                      compiler option: -O2 	program, data =      150 ,        0
  _delay_ms(4)                      compiler option: -O3 	program, data =      150 ,        0
  _delay_ms(4)                      compiler option: -Os 	program, data =      150 ,        0
  #-#
    

Test size with program space
----------------------------

Example program::

  #-- include('examples/pgmspace.py')--#
  from pyavrutils.avrgcc import AvrGcc
  from entrypoint2 import entrypoint

  templ = '''
  #include <avr/io.h>
  #include <avr/pgmspace.h>
  int main()
  {
      %s;
      return 0;
  }
  '''

  cc = AvrGcc()
  cc.optimization = 0
  print  'compiler version:', cc.version()
  print  'compiler options:', ' '.join(cc.options_generated())
  print


  def test(snippet):
      print  snippet, '\t\t',
      try:
          cc.build([templ % snippet])
          size = cc.size()
          print 'program, data =', str(size.program_bytes).rjust(8), ',', str(size.data_bytes).rjust(8)
      except:
          print  'compile error'


  def test_comb(s):
      words = 'static const PROGMEM'.split()

      def choice(i):
          return [words[i], ' ' * len(words[i])]

      for s0 in choice(0):
          for s1 in choice(1):
              for s2 in choice(2):
  #                    for s3 in choice(3):
                          test('%s %s char s[] %s = "%s"' % (s0, s1, s2, s))


  @entrypoint
  def main():
      test_comb("12345")
      test_comb("1234512345")
  #-#

Output::

  #-- sh('python -m pyavrutils.examples.pgmspace ')--#
  compiler version: 4.8.2
  compiler options: avr-gcc -Df_cpu=4000000 -mmcu=atmega168 --std=gnu99 -Wl,--relax -Wl,--gc-sections -ffunction-sections -fdata-sections -fno-inline-small-functions

  static const char s[] PROGMEM = "12345" 		program, data =      144 ,        0
  static const char s[]         = "12345" 		program, data =      166 ,        0
  static       char s[] PROGMEM = "12345" 		compile error
  static       char s[]         = "12345" 		program, data =      166 ,        0
         const char s[] PROGMEM = "12345" 		program, data =      210 ,        6
         const char s[]         = "12345" 		program, data =      210 ,        6
               char s[] PROGMEM = "12345" 		program, data =      210 ,        6
               char s[]         = "12345" 		program, data =      210 ,        6
  static const char s[] PROGMEM = "1234512345" 		program, data =      144 ,        0
  static const char s[]         = "1234512345" 		program, data =      166 ,        0
  static       char s[] PROGMEM = "1234512345" 		compile error
  static       char s[]         = "1234512345" 		program, data =      166 ,        0
         const char s[] PROGMEM = "1234512345" 		program, data =      222 ,       12
         const char s[]         = "1234512345" 		program, data =      222 ,       12
               char s[] PROGMEM = "1234512345" 		program, data =      222 ,       12
               char s[]         = "1234512345" 		program, data =      222 ,       12
  #-#

Conclusions:
 - constant string should be static or global
 - ``const`` has no effect on size
 - PROGMEM should be used

Test minimum size
-----------------

Example program::

  #-- include('examples/minsize.py')--#
  '''
  test minimum program size with all MCUs
  '''

  from entrypoint2 import entrypoint
  from pyavrutils.avrgcc import AvrGcc, AvrGccCompileError


  def test(cc, mcu):
      print 'MCU =', mcu.ljust(20),
      cc.mcu = mcu
      try:
          cc.build(cc.minprog)
          print '    program/data size =', cc.size().program_bytes, ',', cc.size().data_bytes
      except AvrGccCompileError:
          print '    compile error'


  @entrypoint
  def main():
      cc = AvrGcc()
      print '--------------'
      print 'avr-gcc'
      print '--------------'

      print 'compiler version:', cc.version()
      cc.optimize_for_size()
      print 'compiler options:', ' '.join(cc.options_generated())
      print 'code:', cc.minprog
      print
      for mcu in cc.targets:
          test(cc, mcu)
  #-#

Output::

  #-- sh('python -m pyavrutils.examples.minsize')--#
  --------------
  avr-gcc
  --------------
  compiler version: 4.8.2
  compiler options: avr-gcc -Df_cpu=4000000 -mmcu=atmega168 --std=gnu99 -Wl,--relax -Wl,--gc-sections -ffunction-sections -fdata-sections -fno-inline-small-functions -Os
  code: int main(){};

  MCU = at43usb320               program/data size = 80 , 0
  MCU = at43usb355               program/data size = 80 , 0
  MCU = at76c711                 program/data size = 88 , 0
  MCU = at86rf401                program/data size = 40 , 0
  MCU = at90c8534                program/data size = 42 , 0
  MCU = at90can128               program/data size = 176 , 0
  MCU = at90can32                program/data size = 176 , 0
  MCU = at90can64                program/data size = 176 , 0
  MCU = at90pwm1                 program/data size = 92 , 0
  MCU = at90pwm161               compile error
  MCU = at90pwm2                 program/data size = 92 , 0
  MCU = at90pwm216               program/data size = 156 , 0
  MCU = at90pwm2b                program/data size = 92 , 0
  MCU = at90pwm3                 program/data size = 92 , 0
  MCU = at90pwm316               program/data size = 156 , 0
  MCU = at90pwm3b                program/data size = 92 , 0
  MCU = at90pwm81                program/data size = 68 , 0
  MCU = at90s1200                compile error
  MCU = at90s2313                program/data size = 46 , 0
  MCU = at90s2323                program/data size = 30 , 0
  MCU = at90s2333                program/data size = 52 , 0
  MCU = at90s2343                program/data size = 30 , 0
  MCU = at90s4414                program/data size = 54 , 0
  MCU = at90s4433                program/data size = 52 , 0
  MCU = at90s4434                program/data size = 62 , 0
  MCU = at90s8515                program/data size = 54 , 0
  MCU = at90s8535                program/data size = 62 , 0
  MCU = at90scr100               program/data size = 180 , 0
  MCU = at90usb1286              program/data size = 180 , 0
  MCU = at90usb1287              program/data size = 180 , 0
  MCU = at90usb162               program/data size = 144 , 0
  MCU = at90usb646               program/data size = 180 , 0
  MCU = at90usb647               program/data size = 180 , 0
  MCU = at90usb82                program/data size = 144 , 0
  MCU = at94k                    program/data size = 172 , 0
  MCU = ata5272                  compile error
  MCU = ata5505                  compile error
  MCU = ata5790                  compile error
  MCU = ata5790n                 compile error
  MCU = ata5795                  compile error
  MCU = ata6285                  compile error
  MCU = ata6286                  compile error
  MCU = ata6289                  program/data size = 82 , 0
  MCU = atmega103                program/data size = 124 , 0
  MCU = atmega128                program/data size = 168 , 0
  MCU = atmega1280               program/data size = 256 , 0
  MCU = atmega1281               program/data size = 232 , 0
  MCU = atmega1284               compile error
  MCU = atmega1284p              program/data size = 168 , 0
  MCU = atmega128a               compile error
  MCU = atmega128rfa1            program/data size = 316 , 0
  MCU = atmega16                 program/data size = 112 , 0
  MCU = atmega161                program/data size = 112 , 0
  MCU = atmega162                program/data size = 140 , 0
  MCU = atmega163                program/data size = 100 , 0
  MCU = atmega164a               program/data size = 152 , 0
  MCU = atmega164p               program/data size = 152 , 0
  MCU = atmega164pa              compile error
  MCU = atmega165                program/data size = 116 , 0
  MCU = atmega165a               program/data size = 116 , 0
  MCU = atmega165p               program/data size = 116 , 0
  MCU = atmega165pa              compile error
  MCU = atmega168                program/data size = 132 , 0
  MCU = atmega168a               program/data size = 132 , 0
  MCU = atmega168p               program/data size = 132 , 0
  MCU = atmega168pa              compile error
  MCU = atmega169                program/data size = 120 , 0
  MCU = atmega169a               program/data size = 120 , 0
  MCU = atmega169p               program/data size = 120 , 0
  MCU = atmega169pa              program/data size = 120 , 0
  MCU = atmega16a                program/data size = 112 , 0
  MCU = atmega16hva              program/data size = 112 , 0
  MCU = atmega16hva2             program/data size = 116 , 0
  MCU = atmega16hvb              program/data size = 144 , 0
  MCU = atmega16hvbrevb          program/data size = 144 , 0
  MCU = atmega16m1               program/data size = 152 , 0
  MCU = atmega16u2               program/data size = 144 , 0
  MCU = atmega16u4               program/data size = 200 , 0
  MCU = atmega2560               program/data size = 260 , 0
  MCU = atmega2561               program/data size = 236 , 0
  MCU = atmega26hvg              compile error
  MCU = atmega32                 program/data size = 112 , 0
  MCU = atmega323                program/data size = 108 , 0
  MCU = atmega324a               program/data size = 152 , 0
  MCU = atmega324p               program/data size = 152 , 0
  MCU = atmega324pa              program/data size = 152 , 0
  MCU = atmega325                program/data size = 120 , 0
  MCU = atmega3250               program/data size = 128 , 0
  MCU = atmega3250a              program/data size = 128 , 0
  MCU = atmega3250p              program/data size = 128 , 0
  MCU = atmega3250pa             compile error
  MCU = atmega325a               program/data size = 120 , 0
  MCU = atmega325p               program/data size = 120 , 0
  MCU = atmega328                program/data size = 132 , 0
  MCU = atmega328p               program/data size = 132 , 0
  MCU = atmega329                program/data size = 120 , 0
  MCU = atmega3290               program/data size = 128 , 0
  MCU = atmega3290a              program/data size = 128 , 0
  MCU = atmega3290p              program/data size = 128 , 0
  MCU = atmega3290pa             compile error
  MCU = atmega329a               program/data size = 120 , 0
  MCU = atmega329p               program/data size = 120 , 0
  MCU = atmega329pa              program/data size = 120 , 0
  MCU = atmega32a                compile error
  MCU = atmega32c1               program/data size = 152 , 0
  MCU = atmega32hvb              program/data size = 144 , 0
  MCU = atmega32hvbrevb          program/data size = 144 , 0
  MCU = atmega32m1               program/data size = 152 , 0
  MCU = atmega32u2               program/data size = 144 , 0
  MCU = atmega32u4               program/data size = 200 , 0
  MCU = atmega32u6               program/data size = 180 , 0
  MCU = atmega406                program/data size = 120 , 0
  MCU = atmega48                 program/data size = 80 , 0
  MCU = atmega48a                program/data size = 80 , 0
  MCU = atmega48hvf              compile error
  MCU = atmega48p                program/data size = 80 , 0
  MCU = atmega48pa               compile error
  MCU = atmega64                 program/data size = 168 , 0
  MCU = atmega640                program/data size = 256 , 0
  MCU = atmega644                program/data size = 140 , 0
  MCU = atmega644a               program/data size = 152 , 0
  MCU = atmega644p               program/data size = 152 , 0
  MCU = atmega644pa              program/data size = 152 , 0
  MCU = atmega645                program/data size = 120 , 0
  MCU = atmega6450               program/data size = 128 , 0
  MCU = atmega6450a              program/data size = 128 , 0
  MCU = atmega6450p              program/data size = 128 , 0
  MCU = atmega645a               program/data size = 120 , 0
  MCU = atmega645p               program/data size = 120 , 0
  MCU = atmega649                program/data size = 120 , 0
  MCU = atmega6490               program/data size = 128 , 0
  MCU = atmega6490a              program/data size = 128 , 0
  MCU = atmega6490p              program/data size = 128 , 0
  MCU = atmega649a               program/data size = 120 , 0
  MCU = atmega649p               program/data size = 120 , 0
  MCU = atmega64a                compile error
  MCU = atmega64c1               program/data size = 152 , 0
  MCU = atmega64hve              program/data size = 128 , 0
  MCU = atmega64m1               program/data size = 152 , 0
  MCU = atmega64rfa2             compile error
  MCU = atmega64rfr2             compile error
  MCU = atmega8                  program/data size = 66 , 0
  MCU = atmega8515               program/data size = 62 , 0
  MCU = atmega8535               program/data size = 70 , 0
  MCU = atmega88                 program/data size = 80 , 0
  MCU = atmega88a                program/data size = 80 , 0
  MCU = atmega88p                program/data size = 80 , 0
  MCU = atmega88pa               program/data size = 80 , 0
  MCU = atmega8a                 compile error
  MCU = atmega8hva               program/data size = 70 , 0
  MCU = atmega8u2                program/data size = 144 , 0
  MCU = atmxt112sl               compile error
  MCU = atmxt224                 compile error
  MCU = atmxt224e                compile error
  MCU = atmxt336s                compile error
  MCU = atmxt540s                compile error
  MCU = atmxt540sreva            compile error
  MCU = attiny11                 compile error
  MCU = attiny12                 compile error
  MCU = attiny13                 program/data size = 44 , 0
  MCU = attiny13a                compile error
  MCU = attiny15                 compile error
  MCU = attiny1634               compile error
  MCU = attiny167                program/data size = 108 , 0
  MCU = attiny22                 program/data size = 30 , 0
  MCU = attiny2313               program/data size = 62 , 0
  MCU = attiny2313a              compile error
  MCU = attiny24                 program/data size = 58 , 0
  MCU = attiny24a                compile error
  MCU = attiny25                 program/data size = 54 , 0
  MCU = attiny26                 program/data size = 48 , 0
  MCU = attiny261                program/data size = 62 , 0
  MCU = attiny261a               compile error
  MCU = attiny28                 compile error
  MCU = attiny4313               program/data size = 70 , 0
  MCU = attiny43u                program/data size = 60 , 0
  MCU = attiny44                 program/data size = 62 , 0
  MCU = attiny44a                program/data size = 62 , 0
  MCU = attiny45                 program/data size = 58 , 0
  MCU = attiny461                program/data size = 66 , 0
  MCU = attiny461a               program/data size = 66 , 0
  MCU = attiny48                 program/data size = 68 , 0
  MCU = attiny84                 program/data size = 62 , 0
  MCU = attiny84a                program/data size = 62 , 0
  MCU = attiny85                 program/data size = 58 , 0
  MCU = attiny861                program/data size = 66 , 0
  MCU = attiny861a               program/data size = 66 , 0
  MCU = attiny87                 program/data size = 68 , 0
  MCU = attiny88                 program/data size = 68 , 0
  MCU = atxmega128a1             program/data size = 540 , 0
  MCU = atxmega128a1u            program/data size = 552 , 0
  MCU = atxmega128a3             program/data size = 520 , 0
  MCU = atxmega128a3u            compile error
  MCU = atxmega128a4u            compile error
  MCU = atxmega128b1             compile error
  MCU = atxmega128b3             compile error
  MCU = atxmega128c3             compile error
  MCU = atxmega128d3             program/data size = 488 , 0
  MCU = atxmega128d4             compile error
  MCU = atxmega16a4              program/data size = 404 , 0
  MCU = atxmega16a4u             compile error
  MCU = atxmega16c4              compile error
  MCU = atxmega16d4              program/data size = 392 , 0
  MCU = atxmega16x1              compile error
  MCU = atxmega192a3             program/data size = 520 , 0
  MCU = atxmega192a3u            compile error
  MCU = atxmega192c3             compile error
  MCU = atxmega192d3             program/data size = 488 , 0
  MCU = atxmega256a3             program/data size = 520 , 0
  MCU = atxmega256a3b            program/data size = 520 , 0
  MCU = atxmega256a3bu           compile error
  MCU = atxmega256a3u            compile error
  MCU = atxmega256c3             compile error
  MCU = atxmega256d3             program/data size = 488 , 0
  MCU = atxmega32a4              program/data size = 404 , 0
  MCU = atxmega32a4u             compile error
  MCU = atxmega32c4              compile error
  MCU = atxmega32d4              program/data size = 392 , 0
  MCU = atxmega32e5              compile error
  MCU = atxmega32x1              compile error
  MCU = atxmega384c3             compile error
  MCU = atxmega384d3             compile error
  MCU = atxmega64a1              program/data size = 536 , 0
  MCU = atxmega64a1u             program/data size = 548 , 0
  MCU = atxmega64a3              program/data size = 516 , 0
  MCU = atxmega64a3u             compile error
  MCU = atxmega64a4u             compile error
  MCU = atxmega64b1              compile error
  MCU = atxmega64b3              compile error
  MCU = atxmega64c3              compile error
  MCU = atxmega64d3              program/data size = 484 , 0
  MCU = atxmega64d4              compile error
  MCU = avr1                     compile error
  MCU = avr2                     program/data size = 0 , 0
  MCU = avr25                    program/data size = 0 , 0
  MCU = avr3                     program/data size = 0 , 0
  MCU = avr31                    program/data size = 0 , 0
  MCU = avr35                    program/data size = 0 , 0
  MCU = avr4                     program/data size = 0 , 0
  MCU = avr5                     program/data size = 0 , 0
  MCU = avr51                    program/data size = 0 , 0
  MCU = avr6                     program/data size = 0 , 0
  MCU = avrxmega2                program/data size = 0 , 0
  MCU = avrxmega4                compile error
  MCU = avrxmega5                program/data size = 0 , 0
  MCU = avrxmega6                program/data size = 0 , 0
  MCU = avrxmega7                program/data size = 0 , 0
  MCU = m3000                    program/data size = 26 , 0
  #-#

Arduino build tests
===================

.. highlight:: c

Code::

   void setup()
   {
   }
   
   void loop()
   {
   }

Results:

..  #-- from cogtask import buildcsv; buildcsv() --#
..  #-#

.. csv-table::
    :file: docs/generated_build_test.csv
    :header-rows: 1

        
.. _pip: https://pypi.python.org/pypi/pip
.. _arscons: https://github.com/suapapa/arscons
.. _arduino: http://arduino.cc/
.. _python: http://www.python.org/
.. _avr: http://en.wikipedia.org/wiki/Atmel_AVR
.. _scons: http://www.scons.org

.. |Travis| image:: http://img.shields.io/travis/ponty/pyavrutils.svg
   :target: https://travis-ci.org/ponty/pyavrutils/
.. |Coveralls| image:: http://img.shields.io/coveralls/ponty/pyavrutils/master.svg
   :target: https://coveralls.io/r/ponty/pyavrutils/
.. |Latest Version| image:: https://img.shields.io/pypi/v/pyavrutils.svg
   :target: https://pypi.python.org/pypi/pyavrutils/
.. |Supported Python versions| image:: https://img.shields.io/pypi/pyversions/pyavrutils.svg
   :target: https://pypi.python.org/pypi/pyavrutils/
.. |License| image:: https://img.shields.io/pypi/l/pyavrutils.svg
   :target: https://pypi.python.org/pypi/pyavrutils/
.. |Code Health| image:: https://landscape.io/github/ponty/pyavrutils/master/landscape.svg?style=flat
   :target: https://landscape.io/github/ponty/pyavrutils/master
.. |Documentation| image:: https://readthedocs.org/projects/pyavrutils/badge/?version=latest
   :target: http://pyavrutils.readthedocs.org

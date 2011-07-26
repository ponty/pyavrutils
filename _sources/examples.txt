Examples
==========

Simple example
----------------

Example program:

.. literalinclude:: ../pyavrutils/examples/simple.py

Output:

.. program-output:: python -m pyavrutils.examples.simple
    :prompt:

Test size with unused code
----------------------------

Example program:

.. literalinclude:: ../pyavrutils/examples/deadcode.py

Output:

.. program-output:: python -m pyavrutils.examples.deadcode
    :prompt:

Conclusions:
 - both ``gc_sections`` and ``ffunction_sections`` should be used

Test size with delay.h
-------------------------

Example program:

.. literalinclude:: ../pyavrutils/examples/delaysize.py

Output:

.. program-output:: python -m pyavrutils.examples.delaysize
    :prompt:
    
Conclusions:
 - parameter should be constant
 - optimization should be 1, 2, 3 or s
   

Test size with program space
------------------------------

Example program:

.. literalinclude:: ../pyavrutils/examples/pgmspace.py

Output:

.. program-output:: python -m pyavrutils.examples.pgmspace
    :prompt:

Conclusions:
 - constant string should be static or global
 - ``const`` has no effect on size
 - PROGMEM should be used

Test minimum size
-----------------

Example program:

.. literalinclude:: ../pyavrutils/examples/minsize.py

Output:

.. program-output:: python -m pyavrutils.examples.minsize
    :prompt:

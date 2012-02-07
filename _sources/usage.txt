Usage
==================

AVR
-----

.. runblock:: pycon

    >>> from pyavrutils import AvrGcc
    >>> cc = AvrGcc(mcu='atmega48')
    >>> cc.targets
    >>> cc.options_generated()
    >>> cc.build('int main(){}')
    >>> cc.output
    >>> cc.size()
    >>> cc.size().program_bytes
    >>> cc.mcu='atmega168'
    >>> cc.options_generated()
    >>> cc.build('int main(){}')
    >>> cc.output
    >>> cc.size().program_bytes
    

arduino
----------

.. runblock:: pycon

    >>> from pyavrutils import Arduino
    >>> cc = Arduino(board='mini')
    >>> cc.build('void setup(){};void loop(){}')
    >>> cc.output
    >>> cc.size()
    >>> cc.size().program_bytes
    >>> cc.board='pro'
    >>> cc.build('void setup(){};void loop(){}')
    >>> cc.output
    >>> cc.size().program_bytes
    >>> cc.warnings

display warnings on console:

.. program-output:: python -m pyavrutils.cli.arduino_warnings /usr/share/arduino/examples/4.Communication/Dimmer/Dimmer.pde
    :prompt:
        
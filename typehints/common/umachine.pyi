# Copyright (c) 2019, Digi International, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import Any, Collection, List, Optional

PWRON_RESET = ...  # type: int
HARD_RESET = ...  # type: int
WDT_RESET = ...  # type: int
DEEPSLEEP_RESET = ...  # type: int
SOFT_RESET = ...  # type: int
BROWNOUT_RESET = ...  # type: int
LOCKUP_RESET = ...  # type: int
CLEAN_SHUTDOWN = ...  # type: int

PIN_WAKE = ...  # type: int
RTC_WAKE = ...  # type: int


def unique_id() -> bytes:
    """
    Returns a 64-bit bytes object with a unique identifier for the XBee device.

    :return: A 64-bit bytes object with a unique identifier for the XBee
        device.
    """
    ...


def reset() -> None:
    """
    Resets the device in a manner similar to pushing the external RESET button.
    """
    ...


def soft_reset() -> None:
    """
    Performs a soft-reset the REPL.
    """
    ...


def rng() -> int:
    """
    Returns a 30-bit random number that is generated by the software.

    :return: A 30-bit random number that is generated by the software.
    """
    ...


def reset_cause() -> int:
    """
    Returns the cause of a reset. These are possible return values:

    * ``PWRON_RESET``
    * ``HARD_RESET``
    * ``WDT_RESET``
    * ``DEEPSLEEP_RESET``
    * ``SOFT_RESET``
    * ``BROWNOUT_RESET``
    * ``LOCKUP_RESET``

    :return: The reset cause.
    """
    ...


class Pin(object):
    """
    A pin is the basic object to control I/O pins. It has methods to set the
    mode of the pin (input, output, etc) and methods to get and set the digital
    logic level. For analog control of a pin, see the ``ADC`` class.
    """

    ALT = ...  # type: int
    ALT_OPEN_DRAIN = ...  # type: int
    ANALOG = ...  # type: int
    DISABLED = ...  # type: int
    IN = ...  # type: int
    OPEN_DRAIN = ...  # type: int
    OUT = ...  # type: int

    PULL_UP = ...  # type: int
    PULL_DOWN = ...  # type: int

    AF0_COMMISSION = ...  # type: int
    AF1_I2C_SCL = ...  # type: int
    AF1_SPI_ATTN = ...  # type: int
    AF2_SPI_CLK = ...  # type: int
    AF2_UART1_RTS = ...  # type: int
    AF3_SPI_SS = ...  # type: int
    AF3_UART1_CTS = ...  # type: int
    AF4_SPI_MOSI = ...  # type: int
    AF4_UART1_TX = ...  # type: int
    AF5_ASSOC_IND = ...  # type: int
    AF6_RTS = ...  # type: int
    AF7_CTS = ...  # type: int
    AF7_RS485_ENABLE_HIGH = ...  # type: int
    AF7_RS485_ENABLE_LOW = ...  # type: int
    AF8_SLEEP_REQ = ...  # type: int
    AF9_ON_SLEEP = ...  # type: int
    AF10_RSSI = ...  # type: int
    AF11_I2C_SDA = ...  # type: int
    AF11_TEMP_FAN = ...  # type: int
    AF11_USB_DIRECT = ...  # type: int
    AF12_SPI_MISO = ...  # type: int
    AF12_UART1_RX = ...  # type: int

    def __init__(self, id: Any, mode: int = -1, pull: int = -1, *,
                 value: Optional[int] = None, alt: Optional[int] = None) \
            -> None:
        """
        Class constructor. Instantiates a new ``Pin`` object with the provided
        parameters. This class represents a pin peripheral (GPIO pin)
        associated with the given ``id``.

        :param id: Object within the ``machine.Pin.board`` module or a string
            that matches one of these objects.
        :param mode: Specifies the pin mode, which can be one of:

            * ``Pin.IN`` - Pin is configured for input. If viewed as an output
              the pin is in high-impedance state.
            * ``Pin.OUT` - Pin is configured for (normal) output.
            * ``Pin.OPEN_DRAIN`` - Pin is configured for open-drain output.
              Open-drain output works in the following way: if the output value
              is set to **0** the pin is active at a low level; if the output
              value is **1** the pin is in a high-impedance state. Not all
              ports implement this mode, or some might only on certain pins.
            * ``Pin.ALT`` - Pin is configured to perform an alternative
              function, which is port specific. For a pin configured in such a
              way any other Pin methods (except ``Pin.init()``) are not
              applicable (calling them will lead to undefined, or a
              hardware-specific, result). Not all ports implement this mode.
            * ``Pin.ALT_OPEN_DRAIN`` - The Same as ``Pin.ALT``, but the pin is
              configured as open-drain. Not all ports implement this
              mode.
        :param pull: Specifies whether the pin is configured with an internal
            (weak) pull resistor attached. One of:

            * ``None`` - No pull up or down resistor.
            * ``Pin.PULL_UP`` - Pull up resistor enabled.
            * ``Pin.PULL_DOWN`` - Pull down resistor enabled.
        :param value: Valid only for ``Pin.OUT`` and ``Pin.OPEN_DRAIN`` modes
            and specifies initial output pin value if given, otherwise the
            state of the pin peripheral remains unchanged.
        :param alt: Specifies an alternate function for the pin and the values
            it can take are product dependent. This argument is valid only for
            ``Pin.ALT`` and ``Pin.ALT_OPEN_DRAIN`` modes. It may be used when a
            pin supports more than one alternate function. If only one pin
            alternate function is supported this argument is not required. Not
            all ports implement this argument.
        """
        ...

    def __call__(self, value: Optional[int] = None) -> Optional[int]:
        """
        Pin objects are callable. The call method provides a (fast) shortcut
        to set and get the value of the pin. It is equivalent to
        ``Pin.value([x])``. See ``Pin.value()`` for more details.

        :param value: Value to set on the pin.

        :return: When reading the pin, the method returns its value. When
            setting the value this method returns ``None``.
        """
        ...

    def init(self, mode: int, pull: int = -1, *,
             value: Optional[int] = None, alt: Optional[int] = None) -> None:
        """
        Re-initializes the pin using the given parameters. Only those arguments
        that are specified will be set. The rest of the pin peripheral state
        will remain unchanged. See the constructor documentation for details
        of the arguments.

        :param mode: Pin mode.
        :param pull: Flag that specifies if the pin is configured with an
            internal (weak) pull resistor attached.
        :param value: Initial output pin value.
        :param alt: Alternate function for the pin.
        """
        ...

    def value(self, value: Optional[int] = None) -> Optional[int]:
        """
        Gets or sets the value of the pin, depending on whether the argument
        ``value`` is supplied or not.

        If the argument is omitted then this method gets the digital logic
        level of the pin, returning **0** or **1** corresponding to low and
        high voltage signals respectively. The behaviour of this method depends
        on the mode of the pin:

        * ``Pin.IN``- The method returns the actual input value currently
          present on the pin.
        * ``Pin.OUT`` - The behaviour and return value of the method is
          undefined.
        * ``Pin.OPEN_DRAIN`` - If the pin is in state **0** then the behaviour
          and return value of the method is undefined. Otherwise, if the pin is
          in state **1**, the method returns the actual input value currently
          present on the pin.

        :param value: Value to set on the pin.

        :return: When reading the pin, the method returns its value. When
            setting the value this method returns ``None``.
        """
        ...

    def off(self) -> None:
        """
        Sets pin to **0** output level.
        """
        ...

    def on(self) -> None:
        """
        Sets pin to **1** output level.
        """
        ...

    def toggle(self) -> None:
        """
        Toggles the value of the pin. From **0** to **1** or from **1** to
        **0**.
        """
        ...

    def name(self) -> str:
        """
        Returns the name of the pin.

        :return: The name of the pin.
        """
        ...

    def names(self) -> List:
        """
        Returns a list with the CPU and board names for the pin.

        :return: A list with the CPU and board names for the pin.
        """
        ...

    def af_list(self) -> List:
        """
        Returns a list of alternate functions available for this pin.

        :return: A list of alternate functions available for this pin.
        """
        ...

    def mode(self, mode: Optional[int] = None) -> Optional[int]:
        """
        Gets or sets the pin mode.

        When called without a parameter, returns an integer matching one of the
        allowed constants for the mode argument to the init function. Returns
        ``None`` when setting the mode.

        :param mode: Mode to be set on a pin, which can be one of the following
            values:

            * ``Pin.IN`` - Pin is configured for input. If viewed as an output
              the pin is in high-impedance state.
            * ``Pin.OUT`` - Pin is configured for (normal) output.
            * ``Pin.OPEN_DRAIN`` - Pin is configured for open-drain output.
              Open-drain output works in the following way: if the output value
              is set to `0` the pin is active at a low level; if the output
              value is `1` the pin is in a high-impedance state. Not all ports
              implement this mode, or some might only on certain pins.
            * ``Pin.ALT`` - Pin is configured to perform an alternative
              function, which is port specific. For a pin configured in such a
              way any other Pin methods (except ``Pin.init()``) are not
              applicable (calling them will lead to undefined, or a
              hardware-specific, result). Not all ports implement this mode.
            * ``Pin.ALT_OPEN_DRAIN`` - The Same as ``Pin.ALT``, but the pin is
              configured as open-drain. Not all ports implement this mode.

        :return: Current mode on the pin or ``None`` when setting the mode.
        """
        ...

    def pull(self, pull: Optional[int] = None) -> Optional[int]:
        """
        Gets or sets the pin pull state.

        When called without a parameter, returns an integer matching one of the
        allowed constants for the mode argument to the init function. Returns
        ``None`` when setting the pull.

        :param pull: Specifies if the pin has a (weak) pull resistor attached,
            and can be one of:

            * ``None`` - No pull up or down resistor.
            * ``Pin.PULL_UP`` - Pull up resistor enabled.
            * ``Pin.PULL_DOWN`` - Pull down resistor enabled.

        :return: Current pin pull state or ``None`` when setting the pull.
        """
        ...

    def af(self) -> int:
        """
        Returns the currently configured alternate-function of the pin. The
        integer returned will match one of the allowed constants for the af
        argument to the init function.

        :return: The currently configured alternate-function of the pin.
        """
        ...

    class board:
        """
        The board class contains the list of pre-defined pins.
        """

        D0 = ...  # type: Pin
        D1 = ...  # type: Pin
        D2 = ...  # type: Pin
        D3 = ...  # type: Pin
        D4 = ...  # type: Pin
        D5 = ...  # type: Pin
        D6 = ...  # type: Pin
        D7 = ...  # type: Pin
        D8 = ...  # type: Pin
        D9 = ...  # type: Pin
        D10 = ...  # type: Pin
        D11 = ...  # type: Pin
        D12 = ...  # type: Pin
        P0 = ...  # type: Pin
        P1 = ...  # type: Pin
        P2 = ...  # type: Pin


class ADC(object):
    """
    This class represents an ADC (Analog to Digital Conversion) associated to
    a physical pin on the XBee device. It can be used to read analog values
    from sensors connected to that pin.

    The ADC reading value has a resolution of 12 bits with a range of 0 - 4095.
    """

    def __init__(self, id: str) -> None:
        """
        Class constructor. Instantiates a new ``ADC`` object associated with
        the given pin.

        :param id: Pin identifier for the ADC. String that matches one of the
            ``Pin.board`` objects.
        """
        ...

    def read(self) -> int:
        """
        Reads and returns a raw ADC sample with a range of 12 bits
        (0 to 4095).

        Use the following equation to convert this value to mV::

            sample mV = (A/D reading * Vref mV) / 4095

        :return: A raw ADC sample in 12-bit range
        """
        ...

    def read_u16(self) -> int:
        """
        Reads and returns a raw ADC sample with a range of 16 bits
        (0 to 65535). This method is provided for compatibility with
        other MicroPython implementations.

        Since XBee devices only support 12-bit ADC readings,
        readings from ``read_u16()`` will match those from ``read()``,
        only scaled to a 16-bit range.

        Use the following equation to convert this value to mV::

            sample mV = (A/D reading * Vref mV) / 65535

        **Note:**

        The ``read_u16`` method is available on XBee Cellular and
        XBee 3 Cellular products with version ending in 16 and newer,
        and XBee 3 RF products with version ending in 0B and newer.

        :return: A raw ADC sample in 16-bit range
        """
        ...


class PWM(object):
    """
    This class represents a PWM (Pulse Width Modulation) associated to a
    physical pin on the XBee device. PWM generates a square wave (signal
    switched between on and off) that can be used to control the average
    power delivered to a load. The square wave is configured with the
    **frequency** and **duty cycle** parameters.

    **Note**: It is not possible to change fixed frequency on XBee's ``P0``
    and ``P1`` pins.

    Most of XBee devices have PWM functionality on pins ``P0`` and ``P1``. See
    the documentation of your XBee device for more information about PWM
    support.
    """

    def __init__(self, pin: str) -> None:
        """
        Class constructor. Instantiates a new ``PWM`` object associated with
        the given pin.

        :param pin: Pin identifier for the PWM. String that matches one of the
            ``Pin.board`` objects.
        """
        ...

    def init(self) -> None:
        """
        Turns on PWM functionality on the associated pin.
        """
        ...

    def deinit(self) -> None:
        """
        Turns off PWM functionality on the associated pin.
        """
        ...

    def freq(self, freq: Optional[int] = None) -> Optional[int]:
        """
        Sets or gets the PWM frequency. Frequency determines how fast the PWM
        completes a cycle and therefore how fast it switches between high and
        low states.

        **Note**: It is not possible to change fixed frequency on XBee's ``P0``
        and ``P1`` pins.

        :param freq: The new frequency for the PWM.

        :return: Current frequency on the PWM or ``None`` when setting the
            frequency.
        """
        ...

    def duty(self, duty: Optional[int] = None) -> Optional[int]:
        """
        Sets or gets the PWM duty cycle. Duty cycle describes the amount of
        time the signal is in a high (on) state as a percentage of the total
        time of it takes to complete one cycle

        The duty cycle is between 0 (0%) and 1023 (100%), inclusive of the
        end points.

        :param duty: The new duty cycle for the PWM.

        :return: Current duty cycle on the PWM or ``None`` when setting the
            duty cycle.
        """
        ...


class I2C(object):
    """
    This class represents an I2C object associated with a specific two wire
    bus. I2C is a two-wire protocol for communicating between devices. At the
    physical level it consists of two wires: SCL and SDA, the clock and data
    lines respectively.

    I2C objects can be initialized when created, or initialized later on.
    Printing the I2C object gives you information about its configuration.

    The XBee device can function as an I2C master controlled by MicroPython.
    This allows you to perform basic sensing and actuation with I2C devices
    such as sensors and actuators via MicroPython without an additional
    micro-controller.
    """

    def __init__(self, id: int, *, freq: int = 400000) -> None:
        """
        Class constructor. Instantiates a new ``I2C`` object with the provided
        parameters.

        :param id: Identifies a particular I2C peripheral. This version of
            MicroPython supports a single peripheral with id **1** using
            ``DIO1`` for SCL and ``DIO11`` for SDA.
        :param freq: Maximum frequency for SCL.
        """
        ...

    def init(self, scl: Pin, sda: Pin, *, freq: int = 400000) -> None:
        """
        Initializes the I2C bus with the given arguments.

        :param scl: Pin object specifying the pin to use for SCL.
        :param sda: Pin object specifying the pin to use for SDA.
        :param freq: Maximum frequency for SCL.
        """
        ...

    def scan(self) -> Collection[int]:
        """
        Scans all I2C addresses between **0x08** and **0x77** inclusive and
        returns a list of those that respond. A device responds if it pulls the
        SDA line low after its address (including a write bit) is sent on the
        bus.
        """
        ...

    def start(self) -> None:
        """
        Generates a **START** condition on the bus (SDA transitions to low
        while SCL is high).
        """
        ...

    def stop(self) -> None:
        """
        Generates a **STOP** condition on the bus (SDA transitions to high
        while SCL is high).
        """
        ...

    def readinto(self, buf: bytearray, nack: bool = True) -> None:
        """
        Reads bytes from the bus and stores them into ``buf``. The number of
        bytes read is the length of ``buf``. An **ACK** will be sent on the bus
        after receiving all but the last byte. After the last byte is received,
        if ``nack`` is true then a **NACK** will be sent, otherwise an **ACK**
        will be sent (and in this case the slave assumes more bytes are going
        to be read in a later call).

        :param buf: Buffer to read bytes into.
        :param nack: If ``True``, then NACK will be sent after reading last
            bytes.
        """
        ...

    def write(self, buf: bytearray) -> int:
        """
        Writes the bytes from ``buf`` to the bus. Checks that an **ACK** is
        received after each byte and stops transmitting the remaining bytes if
        a **NACK** is received.

        :param buf: Buffer to write bytes from.

        :return: The number of ACKs that were received.
        """
        ...

    def readfrom(self, addr: int, nbytes: int, stop: bool = True) -> bytes:
        """
        Reads ``nbytes`` from the slave specified by ``addr``.

        :param addr: Address of slave device.
        :param nbytes: Maximum amount of bytes to be read.
        :param stop: If ``True``, then **STOP** condition is generated at the
            end of the transfer.

        :return: Data that has been read.
        """
        ...

    def readfrom_into(self, addr: int, buf: bytearray,
                      stop: bool = True) -> None:
        """
        Reads into ``buf`` from the slave specified by ``addr``. The number of
        bytes read will be the length of buf. If ``stop`` is true then a
        **STOP** condition is generated at the end of the transfer.

        :param addr: Address of slave device.
        :param buf: Buffer for storing read data.
        :param stop: If ``True``, then **STOP** condition is generated at the
            end of the transfer.
        """
        ...

    def writeto(self, addr: int, buf: bytearray,
                stop: bool = True) -> int:
        """
        Writes the bytes from ``buf`` to the slave specified by ``addr``. If a
        NACK is received following the write of a byte from ``buf`` then the
        remaining bytes are not sent. If ``stop`` is true then a **STOP**
        condition is generated at the end of the transfer, even if a **NACK**
        is received.

        :param addr: Address of slave device.
        :param buf: Buffer to write data from.
        :param stop: If ``True``, then **STOP** condition is generated at the
            end of the transfer.

        :return: The number of ACKs that were received.
        """
        ...

    def readfrom_mem(self, addr: int, memaddr: int, *,
                     addrsize: int = 8) -> bytes:
        """
        Reads ``nbytes`` from the slave specified by ``addr`` starting from the
        memory address specified by ``memaddr``. The argument ``addrsize``
        specifies the address size in bits.

        :param addr: Address of slave device.
        :param memaddr: Memory address location on a slave device to read from.
        :param addrsize: Address size in bit

        :return: Data that has been read.
        """
        ...

    def readfrom_mem_into(self, addr: int, memaddr: int, buf: bytearray, *,
                          addrsize: int = 8) -> None:
        """
        Reads into ``buf`` from the slave specified by ``addr`` starting from
        the memory address specified by ``memaddr``. The number of bytes read
        is the length of buf. The argument ``addrsize`` specifies the address
        size in bits.

        :param addr: Address of slave device.
        :param memaddr: Memory address location on a slave device to write
            into.
        :param buf: Buffer to store read data.
        :param addrsize: Address size in bits.
        """
        ...

    def writeto_mem(self, addr: int, memaddr: int, buf: bytearray, *,
                    addrsize: int = 8) -> None:
        """
        Writes ``buf`` to the slave specified by ``addr`` starting from the
        memory address specified by ``memaddr``. The argument ``addrsize``
        specifies the address size in bits.

        :param addr: Address of slave device.
        :param memaddr: Memory address location on a slave device to write
            into.
        :param buf: Buffer containing data to write.
        :param addrsize: Address size in bits.
        """
        ...


class UART(object):
    """
    This class represents a UART (Universal Asynchronous Receiver/Transmitter)
    port on the XBee device that can be used to transmit and receive serial
    data.

    **Note**: This class only applies to XBee modules that support the
    **Secondary UART** feature such as the XBee Cellular modules. See
    the documentation of your XBee device for more information about UART
    support.
    """

    RTS: ...  # type: int
    CTS: ...  # type: int

    def __init__(self, id: int,  baudrate: int, bits: int = 8,
                 parity: Optional[int] = None, stop: int = 1, *, flow: int = 0,
                 timeout: int = 0, timeout_char: int = 0) -> None:
        """
        Class constructor. Instantiates a new ``UART`` object with the given
        parameters.

        :param id: ID of UART object. **1** for those XBee modules that support
            the **Secondary UART** feature.
        :param bits: Bits per character, a value from 5 to 8.
        :param parity: An additional parity bit added to each byte, either
            ``None``, **0** (even) or **1** (odd).
        :param stop: Number of stop bits after the optional parity bit, either
            **1** or **2**.
        :param flow: Hardware flow control; either **0** for none, ``UART.RTS``
            for RTS-only, ``UART.CTS`` for CTS-only or ``UART.RTS|UART.CTS``
            for both.
        :param timeout: Number of milliseconds to wait for reading the first
            character.
        :param timeout_char: Number of milliseconds to wait between characters
            when reading.
        """
        ...

    def init(self, baudrate: int, bits: int = 8, parity: Optional[int] = None,
             stop: int = 1, *, flow: int = 0, timeout: int = 0,
             timeout_char: int = 0) -> None:
        """
        Reconfigures the UART with the given parameters.

        :param baudrate: Baud rate, that specifies how fast data is sent over
            serial line.
        :param bits: Bits per character, a value from 5 to 8.
        :param parity: An additional parity bit added to each byte, either
            ``None``, **0** (even) or **1** (odd).
        :param stop: Number of stop bits after the optional parity bit, either
            **1** or **2**.
        :param flow: Hardware flow control; either **0** for none, ``UART.RTS``
            for RTS-only, ``UART.CTS`` for CTS-only or ``UART.RTS|UART.CTS``
            for both.
        :param timeout: Number of milliseconds to wait for reading the first
            character.
        :param timeout_char: Number of milliseconds to wait between characters
            when reading.
        """
        ...

    def deinit(self) -> None:
        """
        Turns off the UART bus. After calling ``deinit()``, attempts to write
        to the UART result in an ``OSError(EPERM)`` exception but reads
        continue to pull buffered bytes.
        """
        ...

    def any(self) -> int:
        """
        Returns an integer counting the number of characters in the read
        buffer, or **0** if no bytes are available.

        :return: Number of characters in the read buffer, or **0** if no bytes
            are available.
        """
        ...

    def read(self, nbytes: Optional[int] = None) -> Optional[bytes]:
        """
        Reads characters. If ``nbytes`` is specified then reads at most that
        many bytes, otherwise reads as much data as possible.

        :param nbytes: Upper limit on number of read characters.

        :return: Bytes read in or ``None`` on timeout.
        """
        ...

    def readinto(self, buf: bytearray, nbytes: Optional[int] = None) \
            -> Optional[int]:
        """
        Reads bytes into the ``buf``. If ``nbytes`` is specified then reads at
        most that many bytes. Otherwise, reads at most ``len(buf)`` bytes.

        :param buf: Buffer for holding read data.
        :param nbytes: Upper limit on number of read characters.

        :return: Number of bytes read in or ``None`` on timeout.
        """
        ...

    def readline(self) -> Optional[bytes]:
        """
        Reads a line, ending in a newline character.

        :return: The line read or ``None`` on timeout.
        """
        ...

    def write(self, buf: bytearray) -> Optional[int]:
        """
        Writes the buffer of bytes to the bus.

        :param buf: Data that needs to be written.

        :return: Number of bytes written or ``None`` on timeout.
        """
        ...

class WDT:
    """Restarts the application when it does not indicate proper operation.

    Once started it cannot be stopped or reconfigured in any
    way. After enabling, the application must "feed" the watchdog
    periodically to prevent it from expiring and resetting the
    system.

    **Note**: Added and only supported as of the following product versions:
      * XBee3 Cellular LTE-M/NB-IoT: version 11415
      * XBee3 Cellular LTE Cat 1: version x15
    """

    def __init__(self,
                    id: int = 0,
                    timeout: int = 60000,
                    response: int = SOFT_RESET) -> None:
        """Create a WDT object and start it.

        :param id: Must be zero

        :param timeout: Time in milliseconds in which the watchdog
        must be fed before it will fire.

        :param response: Choices include:
            * ``SOFT_RESET``: Reset only the MicroPython interpretor.
            * ``HARD_RESET``: Reset the entire XBee.
            * ``CLEAN_SHUTDOWN``: On the XBee3 Cellular products,
                perform a clean shutdown of the cellular component and
                then reset the entire XBee.

        """
        ...

    def feed() -> None:
        """Resets the expiration timer to indicate proper operation."""
        ...

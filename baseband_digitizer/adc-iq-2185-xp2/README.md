adc-iq-2185-xp2
===============

A baseband digitizer board that can capture quadrature signals at 80MHz or
more, process them in an FPGA, and transmit the sample stream to a host
computer over high-speed USB (480Mbps).

This design consists of a Linear Technology LT2141-12 (80MHz, two-channel
ADC), a Lattice XP2 FPGA, and an FTDI FT2232H FIFO-to-USB interface IC. [One
prototype](http://www.sharebrained.com/2012/05/10/progress-on-my-sdr/) device
has been built from this hardware, and is working very well when interfaced
with my ADRF6850 front-end board.

I did have to modify the adrf6850-breakout to allow setting the baseband
output DC offset to a level appropriate for the LT2141's inputs. I also
placed 100 Ohm resistors in front of the ADC input filters, to set the
impedance seen by the ADRF6850 baseband outputs. The ADRF6850 board was
configured with four-pole Butterworth low-pass filters.

The ADC can be scaled considerably, because the LTC2141-12 is pin-compatible
with a wide range of converters. Linear's range goes down to 12 bits at 25MSps
(LTC2140-12) and up to 125MSps at 16 bits (LTC2185).

Status
======

This board has been fabricated and assembled. It was used to receive these
signals:

* POCSAG and FLEX pager broadcasts
* 315 MHz and 433 MHz automotive tire pressure monitors
* Aviation voice transmissions
* ATSC television
* Broadcast FM (88 - 108 MHz)

The FPGA is configured as a 2:1 "F5" half-band filter followed by a 49-tap,
5:1 decimation FIR filter. Output samples are at 8MHz, complex, 16-bit. USB
data rate is 32 million bytes per second. The libftdi-1.0 library's
asynchronous support was used to support this high data rate.

I faked GNU Radio support by creating a UNIX FIFO file and piping the sample
output of my libftdi program into the pipe. Then, I used a GNU Radio file
source to read from the pipe. It's pretty reliable, except for occasionally
unpredictable I/Q phase, which I think is caused by extra, unread data sitting
in the FIFO between runs of the GNU Radio graph.

Bill of Materials
=================

See the included adc-iq-2185-xp2-bom.csv. I believe it's up-to-date with the
components and values I used in my last build of this board. But do re-check
against the appropriate datasheets.

Requirements
============

* [EAGLE 5.11 Hobbyist, Standard, or Professional]
  (http://www.cadsoftusa.com/shop/pricing/)

Because this design uses four PCB layers, EAGLE "freeware" version
will not be useful for editing this design.

Files
=====

* adc-iq-2185-xp2.sch:

    Schematic for circuit board, drawn in EAGLE 5.11.

* adc-iq-2185-xp2-sch.pdf:

    Schematic for circuit board, in Adobe PDF format.

* adc-iq-2185-xp2-bom.csv:

    List of components used in the circuit board, including recommended vendors
    and prices.

* adc-iq-2185-xp2.brd:

    Circuit board layout, drawn in EAGLE 5.11.

* adc-iq-2185-xp2.dru:

    TODO: MISSING, need to recreate and add to repository
    
    EAGLE design rules used to validate schematic and PCB.

* adc-iq-2185-xp2-laen4.cam:

    EAGLE CAM file used to generate Gerber RS-274X files for
    circuit board production via
    [Laen's four-layer PCB Order]
    (http://dorkbotpdx.org/wiki/pcb_order).
    
License
=======

This hardware design is licensed under a
[Creative Commons Attribution-ShareAlike 3.0 Unported License]
(http://creativecommons.org/licenses/by-sa/3.0/).

The associated software is provided under a BSD two-clause license:

Copyright (c) 2011, ShareBrained Technology, Inc.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

o Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

o Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.

Contact
=======

ShareBrained Technology, Inc.

<http://www.sharebrained.com/>
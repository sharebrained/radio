adrf6850-breakout
================

A breakout board for the [Analog Devices ADRF6850 receiver front-end]
(http://www.analog.com/en/rfif-components/rfif-transceivers/adrf6850/products/product.html).
This spiffy IC uses its internal VCO+PLL to downconvert signals between 100 MHz
and 1 GHz, turning them into a wideband quadrature output that you can sample
with your stereo sound card, or feed into a high-bandwidth two-channel ADC.

The PLL/VCO is controlled via the I2C port. The input variable gain amplifier is
controlled by voltage applied to the ADRF_VGAIN input. The quadrature outputs
are exposed as two differential pairs, and have component footprints for you to
add your own fourth-order low-pass filters. The local oscillator output is
exposed, if you want to do something interesting with that signal.

Status
======

This board has been fabricated and assembled. It was used to receive these
signals:

* POCSAG and FLEX pager broadcasts
* Marine AIS reports from nearby boats
* NOAA POES APT satellite weather images
* 315 MHz and 433 MHz automotive tire pressure monitors
* Aviation voice transmissions

I have not done thorough testing of the board, since I don't have any true RF
test equipment. Sensitivity appears good. The front-end is easily
overloaded when you turn up the VGA gain, or when you use a good wideband
antenna. I would recommend using a band selection filter so that you can use
the VGA gain instead of having to use baseband gain (which is arguably too late
to preserve signal quality). I have some band filter breakout board designs in
the same GitHub repository as this file.

I used my [mailing label solder paste stencil technique]
(http://www.sharebrained.com/2011/01/11/pcb-stencils-on-the-cheap-kinda/)
with great success. Give it a try if you have access to a laser cutter.

Bill of Materials
=================

See the included adrf6850-breakout-bom.csv. I believe it's up-to-date with the
components and values I used in my last build of this board. But do re-check
against the ARDF6850 datasheet, and be sure to use ADsimPLL to verify that the
loop filter is to your liking, and is compatible with the reference oscillator
frequency you choose.

The BOM lists a few components with no values. These components are only
necessary if you want to use the local oscillator output. I have not tested
the LO output myself, and will probably remove it from the next iteration of
the board design.

Requirements
============

* [EAGLE 5.11 Hobbyist, Standard, or Professional]
  (http://www.cadsoftusa.com/shop/pricing/)

Because this design uses four PCB layers, EAGLE "freeware" version
will not be useful for editing this design.

Files
=====

* adrf6850-breakout.sch:

    Schematic for circuit board, drawn in EAGLE 5.11.

* adrf6850-breakout-sch.pdf:

    Schematic for circuit board, in Adobe PDF format.

* adrf6850-breakout-bom.csv:

    List of components used in the circuit board, including recommended vendors
    and prices.

* adrf6850-breakout.brd:

    Circuit board layout, drawn in EAGLE 5.11.

* adrf6850-breakout.dru:

    EAGLE design rules used to validate schematic and PCB.

* adrf6850-breakout-laen4.cam:

    EAGLE CAM file used to generate Gerber RS-274X files for
    circuit board production via
    [Laen's four-layer PCB Order]
    (http://dorkbotpdx.org/wiki/pcb_order).
    
* adrf6850.py

    Example code for configuring the ADRF6850 via the I2C port. Code is for
    Python 2.6, using pyBusPirateLite to wiggle I2C via my
    [Bus Pirate 3.5](http://code.google.com/p/the-bus-pirate/).

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
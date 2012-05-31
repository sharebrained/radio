adf4350-breakout
================

A breakout board for the Analog Devices ADF4350 wideband VCO+PLL. This baby
tunes between 2,200 and 4,400 MHz. It also has a divider that extends the output
frequency range down to 137.5 MHz.

Only one output on the ADF4350 is exposed, to simplify trace routing and keep
the board small and inexpensive.

Status
======

This board has been fabricated and assembled a couple of times. It appears to
work well, but I have not done thorough testing of the board, since I don't have
any true RF test equipment. Use this design at your own risk.

I used my [mailing label solder paste stencil technique]
(http://www.sharebrained.com/2011/01/11/pcb-stencils-on-the-cheap-kinda/)
with great success. Give it a try if you have access to a laser cutter.

Bill of Materials
=================

See the included adf4350-breakout-bom.csv. I believe it's up-to-date with the
components and values I used in my last build of this board. But do re-check
against the ADF4350 datasheet, and be sure to use ADsimPLL to verify that the
loop filter is to your liking, and is compatible with the reference oscillator
frequency you choose.

Requirements
============

* [EAGLE 5.11 Hobbyist, Standard, or Professional]
  (http://www.cadsoftusa.com/shop/pricing/)

Because this design uses four PCB layers, EAGLE "freeware" version
will not be useful for editing this design.

Files
=====

* adf4350-breakout.sch:

    Schematic for circuit board, drawn in EAGLE 5.11.

* adf4350-breakout-sch.pdf:

    Schematic for circuit board, in Adobe PDF format.

* adf4350-breakout-bom.csv:

    List of components used in the circuit board, including recommended vendors
    and prices.

* adf4350-breakout.brd:

    Circuit board layout, drawn in EAGLE 5.11.

* adf4350-breakout.dru:

    EAGLE design rules used to validate schematic and PCB.

* adf4350-breakout-laen4.cam:

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
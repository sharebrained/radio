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

This design is licensed under a
[Creative Commons Attribution-ShareAlike 3.0 Unported License]
(http://creativecommons.org/licenses/by-sa/3.0/).

Contact
=======

ShareBrained Technology, Inc.

<http://www.sharebrained.com/>
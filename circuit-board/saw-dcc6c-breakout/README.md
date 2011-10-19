saw-dcc6c-breakout
==================

A breakout board for EPCOS DCC6C package SAW filters. The filter's input and
output are both used in an unbalanced configuration.

Status
======

This board has NOT been fabricated, so its functionality is not verified. Use
this design at your own risk.

Bill of Materials
=================

This board was designed with the EPCOS B39921B3588U410 (915 MHz) SAW filter in
mind. It should support any < 3 GHz SAW filter compatible with the EPCOS DCC6C
package and pin-out. See the corresponding SAW filter component datasheet for
further details.

For 915 MHz
-----------

The EPCOS B39921B3588U410 band-pass SAW filter -3dB pass-band is between 902
and 928 MHz (26 MHz). Attenuation is better than 45dB at 10% from the center
frequency.

* X1: [EPCOS B39921B3588U410](http://www.epcos.com/inf/40/ds/ae/B3588.pdf)
* C1,2: do not insert
* L1,2: inductors not needed, insert 0603 0 Ohm resistor (jumper)
* J1,2: SMA jack, [Emerson 142-0701-801]
  (http://www.emersonconnectivity.com/OA_MEDIA/drawings/dr-1420701801.pdf)

Requirements
============

* [EAGLE 5.11 Hobbyist, Standard, or Professional]
  (http://www.cadsoftusa.com/shop/pricing/)

Because this design uses four PCB layers, EAGLE "freeware" version will not be
useful for editing this design.

Files
=====

* saw-dcc6c-breakout.sch:

    Schematic for circuit board, drawn in EAGLE 5.11.

* saw-dcc6c-breakout.brd:

    Circuit board layout, drawn in EAGLE 5.11.

* saw-dcc6c-breakout.dru:

    EAGLE design rules used to validate schematic and PCB.

* saw-dcc6c-breakout-laen4.cam:

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
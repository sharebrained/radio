bpf-0805-4pc-breakout
=====================

A breakout board for TDK DEA202450BT-1213C1 and Johanson
(JTI) 2450BP15B100 2.4 GHz SAW filters in a peculiar four-pin
0805 package. The filter's input and output are unbalanced.

Status
======

This board has been fabricated but not yet assembled and
tested, so its functionality is not verified. Use this
design at your own risk.

Bill of Materials
=================

This board was designed using the TDK footprint, and then
adapted to support the Johanson component. It should support
any < 3 GHz SAW filter compatible with the TDK/JTI 0805
package and pin-out. See the corresponding SAW filter
component datasheets for further details.

For Johanson 2450BP15B100
-------------------------

The Johanson 2450BP15B100 SAW filter pass-band is between
2400 and 2500 MHz (100 MHz). Attenuation is better than 35dB
over most of the stop region.

* X1: [Johanson B39321B3741H110]
  (http://www.johansontechnology.com/images/stories/ip/band-pass-filters/BP_Filter_2450BP15B100.pdf)
* J1,2: SMA jack, [Emerson 142-0701-801]
  (http://www.emersonconnectivity.com/OA_MEDIA/drawings/dr-1420701801.pdf)

For TDK DEA202450BT-1213C1
--------------------------

The TDK DEA202450BT-1213C1 SAW filter pass-band is between
2400 and 2500 MHz (100 MHz). Attenuation is better than 35dB
over most of the stop region.

* X1: [TDK DEA202450BT-1213C1]
  (http://www.tdk.co.jp/tefe02/e8bpf_dea.pdf)
* J1,2: SMA jack, [Emerson 142-0701-801]
  (http://www.emersonconnectivity.com/OA_MEDIA/drawings/dr-1420701801.pdf)

Requirements
============

* [EAGLE 5.11 Hobbyist, Standard, or Professional]
  (http://www.cadsoftusa.com/shop/pricing/)

Because this design uses four PCB layers, EAGLE "freeware" version
will not be useful for editing this design.

Files
=====

* bpf-0805-4pc-breakout.sch:

    Schematic for circuit board, drawn in EAGLE 5.11.

* bpf-0805-4pc-breakout.brd:

    Circuit board layout, drawn in EAGLE 5.11.

* bpf-0805-4pc-breakout.dru:

    EAGLE design rules used to validate schematic and PCB.

* bpf-0805-4pc-breakout-laen4.cam:

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
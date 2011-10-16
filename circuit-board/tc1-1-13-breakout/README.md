tc1-1-13-breakout
=================

A breakout board for Mini-Circuits TC1-1-13 transformer in
a bal-un configuration. One side of the balun is configured
for an unbalanced signal, and the other is configured for a
balanced signal.

Status
======

This board has been fabricated but not yet assembled and
tested, so its functionality is not verified. Use this
design at your own risk.

Bill of Materials
=================

This board was designed using the Mini-Circuits AT224-1
footprint. It should support any < 3 GHz transformer with
the same footprint and pinout. See the corresponding
component datasheets for further details.

For Mini-Circuits TC1-1-13
--------------------------

The Mini-Circuits TC1-1-13 family of transformers operate
between 4.5 MHz and 3 GHz.

* T1: [Mini-Circuits TC1-1-13M+]
  (http://www.minicircuits.com/pdfs/TC1-1-13M+.pdf)
* C1,2,3,4: DC blocking capacitors, 0402, C0G, value to
  suit application (typical value 100nF).
* R1,2: Terminating resistors (optional), 0402, 1% or
  better, value to suit application.
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

* tc1-1-13-breakout-breakout.sch:

    Schematic for circuit board, drawn in EAGLE 5.11.

* tc1-1-13-breakout-breakout.brd:

    Circuit board layout, drawn in EAGLE 5.11.

* tc1-1-13-breakout-breakout.dru:

    EAGLE design rules used to validate schematic and PCB.

* tc1-1-13-breakout-breakout-laen4.cam:

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
saw-dcc6e-breakout
==================

A breakout board for EPCOS DCC6E package SAW filters. The
filter's input and output are both used in an unbalanced
configuration.

Status
======

This board has been fabricated but not yet assembled and
tested, so its functionality is not verified. Use this
design at your own risk.

Bill of Materials
=================

This board was designed with the EPCOS B39321B3741H110
(315 MHz) and EPCOS B39431B3743H110 (433 MHz) SAW filters
in mind. It should support any < 3 GHz SAW filter
compatible with the EPCOS DCC6E package and pin-out. See
the corresponding SAW filter component datasheet for
further details.

For 315 MHz
-----------

The EPCOS B39321B3741H110 band-pass SAW filter -3dB
pass-band is between 314.82 and 315.18 MHz (360 kHz).
Attenuation is better than 50dB at 10% from the center
frequency.

* X1: [EPCOS B39321B3741H110]
  (http://www.epcos.com/inf/40/ds/ae/B3741.pdf)
* C1,2: 1.8pF, 0402, C0G
* L1,2: 68nH, 0603
* J1,2: SMA jack, Emerson 142-0701-801

For 433 MHz
-----------

The EPCOS B39431B3743H110 band-pass SAW filter -3dB
pass-band is between 433.75 and 434.09 MHz (340 kHz).
Attenuation is better than 50dB at 10% from the center
frequency.

* X1: [EPCOS B39431B3743H110]
  (http://www.epcos.com/inf/40/ds/ae/B3743.pdf)
* C1,2: do not insert
* L1,2: 39nH, 0603
* J1,2: SMA jack,
  [Emerson 142-0701-801]
  (http://www.emersonconnectivity.com/OA_MEDIA/drawings/dr-1420701801.pdf)

Requirements
============

* [EAGLE 5.11 Hobbyist, Standard, or Professional]
  (http://www.cadsoftusa.com/shop/pricing/)

Because this design uses four PCB layers, EAGLE "freeware" version
will not be useful for editing this design.

License
=======

This design is licensed under a
[Creative Commons Attribution-ShareAlike 3.0 Unported License]
(http://creativecommons.org/licenses/by-sa/3.0/).

Contact
=======

ShareBrained Technology, Inc.

[http://www.sharebrained.com/]
(http://www.sharebrained.com/)
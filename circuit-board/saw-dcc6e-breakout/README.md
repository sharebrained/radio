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
in mind.

For 315 MHz
-----------

Use EPCOS B39321B3741H110 band-pass SAW filter, 314.82
to 315.18 MHz (360 kHz bandwidth), in package DCC6E
(3.0 x 3.0 x 1.0 mm).

* X1: [EPCOS B39321B3741H110]
  (http://www.epcos.com/inf/40/ds/ae/B3741.pdf)
* C1,2: 1.8pF, 0402, C0G
* L1,2: 68nH, 0603
* J1,2: SMA jack, Emerson 142-0701-801

For 433 MHz
-----------

Use EPCOS B39431B3743H110 band-pass SAW filter, 433.75
to 434.09 MHz (340 kHz bandwidth), in package DCC6E
(3.0 x 3.0 x 1.0 mm).

* X1: [EPCOS B39431B3743H110]
  (http://www.epcos.com/inf/40/ds/ae/B3743.pdf)
* C1,2: do not insert
* L1,2: 39nH, 0603
* J1,2: SMA jack, Emerson 142-0701-801

See the corresponding SAW filter component datasheet for
further details.

Requirements
============

* [EAGLE 5.11 Hobbyist, Standard, or Professional]
  (http://www.cadsoftusa.com/shop/pricing/)

Because this design uses four PCB layers, EAGLE "freeware" version
will not be useful for editing this design.

License
=======

This design is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/).

Contact
=======

[ShareBrained Technology, Inc.]
(http://www.sharebrained.com/)

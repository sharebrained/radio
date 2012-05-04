#!/usr/bin/env python

# Copyright (c) 2011, ShareBrained Technology, Inc.
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# o Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# o Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import sys
import math
import time
import numpy

#from pyBusPirate.BinaryMode.I2C import *
from pyBusPirateLite.I2C import *

def write_data(write_list, i2c):
    for register, value in write_list:
        #print('[0xF0 %s 0x%02x]' % (register, value))
        data = (0xF0, register, value)
        i2c.send_start_bit()
        i2c.bulk_trans(len(data), data)
        i2c.send_stop_bit()

f_refin = 25e6

def pfd(d, r, t):
    global f_refin
    return f_refin * ((1.0 + d) / (r * (1.0 + t)))

print('Reference frequency: %s' % f_refin)

refin_doubler = 0
refin_divider = 1
refin_div_2 = 0
pfd = f_refin * ((1.0 + refin_doubler) / (refin_divider * (1.0 + refin_div_2)))
print('PFD frequency: %s' % pfd)

autocalibration_time = 100e-6
bscdiv = int(math.floor(autocalibration_time * pfd / 24.0))
print('target autocalibration time: %s' % autocalibration_time)
print('\tBSCDIV: 0x%x' % bscdiv)

lo = float(sys.argv[1])

def set_lo(lo):
    global pfd

    if lo < 100e6:
        raise Exception('LO frequency below 100MHz')
    if lo < 125e6:
        rfdiv = 0b011
    elif lo < 250e6:
        rfdiv = 0b010
    elif lo < 500e6:
        rfdiv = 0b001
    elif lo <= 1000e6:
        rfdiv = 0b000
    else:
        raise Exception('LO frequency above 1GHz')
    #print('RFDIV: %d' % rfdiv)
    
    n = ((1 << rfdiv) * 2.0 * lo) / pfd
    #print('N: %s' % n)
    n_int = int(math.floor(n))
    n_frac = int(round((n - n_int) * float(1 << 25)))
    #print('\tINT: %s' % n_int)
    #print('\t\tINT[11:8]: 0x%02x' % ((n_int >> 8) & 0xF))
    #print('\t\tINT[ 7:0]: 0x%02x' % ((n_int >> 0) & 0xFF))
    #print('\tFRAC: %s' % n_frac)
    #print('\t\tFRAC[24   ]: 0x%02x' % ((n_frac >> 24) & 0x01))
    #print('\t\tFRAC[23:16]: 0x%02x' % ((n_frac >> 16) & 0xFF))
    #print('\t\tFRAC[15: 8]: 0x%02x' % ((n_frac >>  8) & 0xFF))
    #print('\t\tFRAC[ 7: 0]: 0x%02x' % ((n_frac >>  0) & 0xFF))

    write_list = (
        # TODO: Do not rewrite rfdiv unless necessary. It's not double-buffered.
        (28, 0x08 | rfdiv),
        #(10, (0x40 * refin_div_2) | (0x20 * refin_doubler) | refin_divider),
        ( 7, (n_int  >>  8) & 0x0F),
        ( 6, (n_int  >>  0) & 0xFF),
        ( 3, (n_frac >> 24) & 0x01),
        ( 2, (n_frac >> 16) & 0xFF),
        ( 1, (n_frac >>  8) & 0xFF),
        ( 0, (n_frac >>  0) & 0xFF),
    )

    return write_list

init_list = (
    (30, 0x00), # VGA positive gain slope, VGA power-down
    #(29, 0x71), # internal Vocm, 30MHz cut-off, narrow-band, demod power-up
    (29, 0x31), # external Vocm, 30MHz cut-off, narrow-band, demod power-up
    (28, 0x0B), # (LO divide by 8: 100MHz to 125MHz
    (27, 0x00), # monitor output: power down, output -24dBm
    (26, 0x00),
    (25, 0x68), # autocalibration: equation 3 @ 25Mhz refin: bscdiv=104
    (24, 0x38), # enable calibration
    (23, 0x70), # lock detector enabled, 3072 up/down pulses, low/coarse precision
    (22, 0x00),
    (21, 0x00),
    (20, 0x00),
    (19, 0x00),
    (18, 0x00),
    (17, 0x00),
    (16, 0x00),
    (15, 0x00),
    (14, 0x00), # 2048/3072 up/down pulses
    (13, 0x08),
    (12, 0x18), # power up PLL
    (11, 0x00),
    (10, 0x01), # bypass ref divide by 2, disable doubler, divide by 1
    ( 9, 0x70), # 2.5mA charge pump current
    ( 8, 0x00),
    ( 7, 0x00), # muxout: tristate, N[11:8] = 0
    ( 6, 0x43), # N[7:0] = 67
    ( 5, 0x00), # R-divider disabled
    ( 4, 0x01),
    ( 3, 0x00), # FRAC[24] = 0
    ( 2, 0x87), # FRAC[23:16] = 0x87
    ( 1, 0x2b), # FRAC[15:8] = 0x2b
    ( 0, 0x02), # FRAC[7:0] = 0x02
)

enable_vga = (
    (30, 0x01),
)

i2c = I2C('/dev/tty.usbserial-A5005CUQ', 115200)
i2c.resetBP()

if not i2c.BBmode():
    print('BBmode() failed')
    sys.exit()

#i2c.reset()

if not i2c.enter_I2C():
    print('enter_I2C() failed')
    sys.exit()

if not i2c.set_speed(I2CSpeed._400KHZ):
    print('set_speed() failed')
    sys.exit()

i2c.timeout(0.2)

write_data(init_list, i2c)
write_data(enable_vga, i2c)

if len(sys.argv) == 3:
    start_mhz = float(sys.argv[1])
    end_mhz = float(sys.argv[2])

    print('3...')
    time.sleep(1.0)
    print('2...')
    time.sleep(1.0)
    print('1...')
    time.sleep(1.0)

    for lo_mhz in numpy.arange(start_mhz, end_mhz, 0.1):
        lo = lo_mhz * 1e6
        write_data(set_lo(lo), i2c)
        print('%5.1f' % (lo / 1e6))
        #time.sleep(0.1)
elif len(sys.argv) == 2:
    lo = float(sys.argv[1]) * 1e6
    write_data(set_lo(lo), i2c)
    
print

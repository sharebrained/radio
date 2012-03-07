#!/usr/bin/env python

import sys
#import math
import time
import struct

from pyBusPirateLite.SPI import *

spi = SPI('/dev/tty.usbserial-A5005CUQ', 115200)
spi.resetBP()

if not spi.BBmode():
    print('BBmode() failed')
    sys.exit()

if not spi.enter_SPI():
    print('enter_SPI() failed')
    sys.exit()

# speed = 30kHz
# polarity = idle low (default)
# output clock edge = active to idle (default)
# input sample phase = middle (default)
# CS = /CS (default)
# output type = normal

if not spi.cfg_pins(PinCfg.POWER | PinCfg.CS | PinCfg.AUX):
    print('cfg_pins() failed')
    sys.exit()

if not spi.set_speed(SPISpeed._30KHZ):
#if not spi.set_speed(SPISpeed._2_6MHZ):
    print('set_speed() failed')
    sys.exit()

if not spi.cfg_spi(SPICfg.CLK_EDGE | SPICfg.OUT_TYPE):
    print('cfg_spi() failed')
    sys.exit()

def write_data(data):
    data = struct.pack('>I', data)
    data = map(ord, data)
    print(['%02x' % d for d in data])
    spi.CS_Low()
    spi.bulk_trans(len(data), data)
    spi.CS_High()

# Design constants
refin = 25e6

# Reference configuration
reference_doubler = 0
rdiv2 = 0
r_counter = 1

f_pfd = refin * ((1.0 + reference_doubler) / (r_counter * (1.0 + rdiv2)))
print('PFD: %f' % (f_pfd,))

if f_pfd > 32e6:
    raise Exception('PFD frequency %f exceeds 32 MHz maximum' % (f_pfd,))

band_select_clock_divider_value = 200

band_selection_time = 10.0 * band_select_clock_divider_value / f_pfd
print('Band selection time: %f' % band_selection_time)
if band_selection_time < 80e-6:
    raise Exception('band selection time %f is less than 80 usec' % (band_selection_time,))

prescaler = 1
integer_value = 160
fractional_value = 0
modulus_value = 8

divider_select = 1

if prescaler == 0:
    # Prescaler 4/5
    if integer_value < 23:
        raise Exception('integer value %d must be >= 23 for prescaler=0' % (integer_value,))
elif prescaler == 1:
    # Prescaler 8/9
    if integer_value < 75:
        raise Exception('integer value %d must be >= 75 for prescaler=1' % (integer_value,))
else:
    raise Exception('prescaler %d out of bounds' % (prescaler,))
if integer_value > 65535:
    raise Exception('integer value %d must be <= 65535' % (integer_value,))
    
if (modulus_value < 2) or (modulus_value > 4095):
    raise Exception('modulus value %d out of bounds' % (modulus_value,))
if fractional_value >= modulus_value:
    raise Exception('fractional value %d must be less than modulus value %d' % (fractional_value, modulus_value))

f_vco = f_pfd * (float(integer_value) + (float(fractional_value) / float(modulus_value)))
print('VCO: %f MHz' % (f_vco / 1e6,))

if (f_vco > 3e9) and (prescaler == 0):
    raise Exception('%f exceeds maximum RF frequency for prescaler=0' % (f_vco,))

f_out = f_vco / float(1 << divider_select)
print('Out: %f MHz' % (f_out / 1e6,))

#########################
# Register calculations #
#########################

r0 = (integer_value << 15) | (fractional_value << 3) | 0

phase_value = 1
r1 = (prescaler << 27) | (phase_value << 15) | (modulus_value << 3) | 1

low_modes = 0
muxout = 0
double_buff = 0
charge_pump_current = 7
ldf = 0
ldp = 1
pd_polarity = 1
pd = 0
cp_three_state = 0
counter_reset = 0
r2 = (low_modes << 29) | (muxout << 26) | (reference_doubler << 25) | \
     (rdiv2 << 24) | (r_counter << 14) | (double_buff << 13) | \
     (charge_pump_current << 9) | (ldf << 8) | (ldp << 7) | \
     (pd_polarity << 6) | (pd << 5) | (cp_three_state << 4) | \
     (counter_reset << 3) | 2

csr = 0
clk_div_mode = 0
clock_divider_value = 200
r3 = (csr << 18) | (clk_div_mode << 15) | (clock_divider_value << 3) | 3

feedback_select = 1
vco_power_down = 0
mtld = 0
aux_output_select = 0
aux_output_enable = 0
aux_output_power = 0
rf_output_enable = 1
output_power = 0
r4 = (feedback_select << 23) | (divider_select << 20) | \
     (band_select_clock_divider_value << 12) | (vco_power_down << 11) | \
     (mtld << 10) | (aux_output_select << 9) | (aux_output_enable << 8) | \
     (aux_output_power << 6) | (rf_output_enable << 5) | \
     (output_power << 3) | 4

ld_pin_mode = 1
r5 = (ld_pin_mode << 22) | 5

print('Register values:')
print('R0: %08x' % (r0,))
print('R1: %08x' % (r1,))
print('R2: %08x' % (r2,))
print('R3: %08x' % (r3,))
print('R4: %08x' % (r4,))
print('R5: %08x' % (r5,))
print

write_data(r5)
write_data(r4)
write_data(r3)
write_data(r2)
write_data(r1)
write_data(r0)

#def tune_1000():
#    write_data(0x00500000)
#
#def tune_1001():
#    write_data(0x00500C80)
#
#def alternate():
#    while True:
#        time.sleep(1.0)
#        tune_1000()
#        print('1000')
#        time.sleep(1.0)
#        tune_1001()
#        print('1001')

#tune_1000()

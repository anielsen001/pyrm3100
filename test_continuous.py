

import sys
import time
import board
sys.path.append('./CircuitPython_RM3100')
import rm3100
import digitalio

i2c = board.I2C()

GAIN_200=74.9
GAIN_400=148.0

drdy_pi_pin = digitalio.DigitalInOut(board.D17) # physical pin 11
drdy_pi_pin.direction = digitalio.Direction.INPUT

with rm3100.RM3100_I2C(
    i2c,
    i2c_address=0x20,
    cycle_count=400,
    drdy_pin = drdy_pi_pin,) as rm:

        rm.start_continuous_reading(frequency=150)
        while (True):
            rx,ry,rz = rxyz = rm.get_next_reading() # raw values
            x,y,z = [ _r /GAIN_400*1000 for _r in rxyz] # x1000 for nT
            print(f'{time.time()}, {x}, {y}, {z}, {rx}, {ry}, {rz}')

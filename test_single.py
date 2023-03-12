# python3 -m pip install RPi.gpio
# python3 -m pip install adafruit-blinka


import sys
import time
import board
sys.path.append('./CircuitPython_RM3100')
import rm3100

i2c = board.I2C()
rm = rm3100.RM3100_I2C(
    i2c,
    i2c_address=0x20,
    cycle_count=400)

GAIN_200=74.9
GAIN_400=148.0

rm.start_single_reading()
time.sleep(.5)
rx,ry,rz = rxyz = rm.get_next_reading() # raw values
x,y,z = [ _r /GAIN_400 for _r in rxyz]
print(f'{time.time()}, {x}, {y}, {z}, {rx}, {ry}, {rz}')

while True:
    rm.start_single_reading()
    time.sleep(.1)
    #print(rm.get_next_reading())
    #x,y,z = rm.convert_to_microteslas(rm.get_next_reading())
    rx,ry,rz = rxyz = rm.get_next_reading() # raw values
    x,y,z = [ _r /GAIN_400*1000 for _r in rxyz] # x1000 for nT

    print(f'{time.time()}, {x}, {y}, {z}, {rx}, {ry}, {rz}')

    # raw counts from runMag - 400 cycles
    # -275021, 29328, 413861

    # raw counts from here - 200 cycles
    # -137468, 14639, 206849


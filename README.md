## Circuit python on Raspberry Pi for PNI RM3100

I have a working python software version based on [CircuitPython_RM3100](https://github.com/furbrain/CircuitPython_RM3100)

## Pin-out connections for I2C interface

| R-Pi physical Pin | RM3100 physical Pin | purpose | 
|---|---|---|
| 1 |  10,12,13 | 3.3V power |
| 3 |  3 | I2C Data SDA| 
| 5 |  1 | I2C Clock SCL/SCK | 
| 9 |2,4, 7,14  | Ground |
| 11  | 5   | DRDY - data ready  |


## Set up python virtual environment

```bash
python3 -m venv venv
python3 -m pip install -r requirements.txt
```

## Get circuit-python repo for RM-3100

```bash
git clone https://github.com/furbrain/CircuitPython_RM3100
```

## Example script

An example script can be found in `test_continuous.py`


import spidev
import time

address = 0x00

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 50000

# sets the value of resistance, value should be 0-127
def digitalPotWrite(value):
    spi.xfer2([address, value])

# ever changing loop
while True:
    for i in range(129):
        digitalPotWrite(i)
        time.sleep(0.01)
    time.sleep(0.5)
    for i in range(128, -1, -1):
        digitalPotWrite(i)
        time.sleep(0.01)

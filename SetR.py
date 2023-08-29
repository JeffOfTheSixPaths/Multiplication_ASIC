import spidev
import time
from gpiozero import LED
import sys

address = 0x00

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 50000

f = LED(16)

#f.on()
f.on()
# sets the value of resistance, value should be 0-127
def digitalPotWrite(value):
    f.off()
    spi.xfer2([address, value])
    f.on()

#print(sys.argv[1])
#print(type(sys.argv[1]))
digitalPotWrite(int(sys.argv[1]))

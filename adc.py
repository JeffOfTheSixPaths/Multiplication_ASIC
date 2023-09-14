from smbus import SMBus
from gpiozero import PWMLED
from time import sleep
bus = SMBus(1)
id = 0x4B
adc_pins = [0x84]
def read(input):
    bus.write_byte(id, adc_pins[input])
    return bus.read_byte(id)

while True:
    value = read(0)
    print(value)
    sleep(.5)

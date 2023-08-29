import spidev
import time
from gpiozero import LED

address = 0x00
STEPS = 128
MAX_R = 10000 # 10k ohms
STEP_R = MAX_R/STEPS

# Setup SPI
spi = spidev.SpiDev()
spi.open(0, 0) # Open SPI bus 0, device (CS) 0
spi.max_speed_hz = 50000

CS_pins = [20,16]
for i,pin in enumerate(CS_pins): 
    CS_pins[i] = LED(pin) #saying it's an LED because it's easy to control like that
    CS_pins[i].on()

#for pin in CS_pins: pin.on()
# Function to write to the digital potentiometer
def digitalPotWrite(pin_index,value):
    CS_pins[pin_index].off()
    spi.xfer2([address, value])
    CS_pins[pin_index].on()


R_eq = 10000 # in ohms
def to_steps(resistance) -> int: #converts resistance to the respective amount of steps
    # round vs round down?
    # TODO: needs to consider the size of the digipots and the inputs later
    step = int(resistance/STEP_R)
    return step

R_eq = to_steps(R_eq)


while True:
    for i in range(R_eq + 1):
        digitalPotWrite(0, i)
        digitalPotWrite(1, R_eq-i)

        time.sleep(0.01)
    time.sleep(0.5)

    for i in range(R_eq, -1, -1):
        digitalPotWrite(0, i)
        digitalPotWrite(1, R_eq-i)
        time.sleep(0.01)
    time.sleep(0.5)


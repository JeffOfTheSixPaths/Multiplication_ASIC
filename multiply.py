import spidev
import time
from gpiozero import LED
from smbus import SMBus
from math import log

address = 0x00
STEPS = 128
MAX_R = 9610 # ~10k ohms
STEP_R = MAX_R/STEPS #should be 75 ohms

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

def to_steps(resistance) -> int: #converts resistance to the respective amount of steps
    # round vs round down?
    # TODO: needs to consider the size of the digipots and the inputs later
    resistance -= STEP_R # step 0 = 75 Ohms, so this needs to be put in for the counting to be correct
    step = int((resistance)/STEP_R)
    return step

#intializing the bus
bus = SMBus(1)
#id of the ADC
id = 0x4B
#ADC pin commands
adc_pins = [0x84]
def read(input):
    bus.write_byte(id, adc_pins[input])
    return bus.read_byte(id)


def multiply(a,b):
  if a == 0 or b == 0: raise Exception("no 0!!")
  R_eq = (5000)/b #dividing 5/b would be too small to put on the digipots and would assume a too large of a current
  R1 = a # just A
  R2 = R_eq - R1 # need to have this value so that the total R_eq stays the same
  steps_r1 = to_steps(R1)
  steps_r2 = to_steps(R2)
  digitalPotWrite(0, steps_r1)
  digitalPotWrite(1, steps_r2)
  return read(0)

I_interval = [0.001, 0.00009] #in A
R_interval = [10**5, 100]

def multiply(a,b):
  if a == 0 or b == 0: raise Exception("no 0!!")
  
  # the amount to multiply b by to make it in the I_interval
  b_factor = -int(log(a, 10)) - 4
  mb *= 10**b_factor
  if mb > I_interval[0]:
     mb *= 10
     #b_factor += 1

  if mb < I_interval[1]:
     raise Exception(f"Cannot put {b} into the Current Interval: {mb}")
      
  
  R_eq = (5)/mb 
  R1 = a # just A
  r_factor = 4 - log(a, 10)
  R1 *= r_factor
  R2 = R_eq - R1 # need to have this value so that the total R_eq stays the same
  steps_r1 = to_steps(R1)
  steps_r2 = to_steps(R2)
  digitalPotWrite(0, steps_r1)
  digitalPotWrite(1, steps_r2)
  return (255-read(0))*(5000/256)

def error(a,b):
  true_value = a*b
  v = multiply(a,b)
  return (v-true_value)/true_value



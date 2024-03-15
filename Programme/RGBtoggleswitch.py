#Code by Daniel S. & Michael E., last update March 2024
from machine import Pin
from time import sleep
Led_g = 15
Led_b = 14
Led_r = 6
butPin = 18
butPinx = 19
butPinxx = 20
mybut = Pin(butPin,Pin.IN,Pin.PULL_UP)
myLed = Pin(Led_g,Pin.OUT)
mybutx = Pin(butPinx,Pin.IN,Pin.PULL_UP)
myLedx = Pin(Led_b,Pin.OUT)
mybutxx = Pin(butPinxx,Pin.IN,Pin.PULL_UP)
myLedxx = Pin(Led_r,Pin.OUT)
butStateNOW = 1
butStateOLD = 1
butStateNOWx = 1
butStateOLDx = 1
butStateNOWxx = 1
butStateOLDxx = 1
LEDState=False
LEDStatex=False
LEDStatexx=False

while True:
    butStateNOW=mybut.value()
    if butStateNOW == 1 and butStateOLD == 0:
        LEDState = not LEDState
        myLed.value(LEDState)
    butStateOLD = butStateNOW
    sleep(0.1)
    
    butStateNOWx=mybutx.value()
    if butStateNOWx == 1 and butStateOLDx == 0:
        LEDStatex = not LEDStatex
        myLedx.value(LEDStatex)
    butStateOLDx = butStateNOWx
    sleep(0.1)
    
    butStateNOWxx=mybutxx.value()
    if butStateNOWxx == 1 and butStateOLDxx == 0:
        LEDStatexx = not LEDStatexx
        myLedxx.value(LEDStatexx)
    butStateOLDxx = butStateNOWxx
    sleep(0.1)
    

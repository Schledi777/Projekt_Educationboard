#source https://github.com/Guitarman9119/Raspberry-Pi-Pico-/blob/main/Joystick%20with%20push%20button/basic.py
from machine import Pin, ADC
import utime

xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))
button = Pin(11,Pin.IN, Pin.PULL_UP)

while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonValue = button.value()
    buttonStatus = "not pressed"


    if buttonValue == 0:
        buttonStatus = "pressed"
        
        
    print("X: " + str(xValue) + ", Y: " + str(yValue) + " -- button value: " + str(buttonValue) + " button status: " + buttonStatus)
    utime.sleep(0.2)

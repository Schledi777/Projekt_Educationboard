#Code by Daniel S. & Michael E., last update March 2024

from machine import Pin, reset
from time import sleep
import sys
#variable for Pin of togglebutton & LED
Led_g = 12
Led_b = 13
Led_r = 10
butPin = 18
butPinx = 19
butPinxx = 20
#Button for returning to Menu
button_pin = Pin(9, Pin.IN, Pin.PULL_UP) 
#Togglebutton & LED declaration
mybut = Pin(butPin,Pin.IN,Pin.PULL_UP)
myLed = Pin(Led_g,Pin.OUT)
mybutx = Pin(butPinx,Pin.IN,Pin.PULL_UP)
myLedx = Pin(Led_b,Pin.OUT)
mybutxx = Pin(butPinxx,Pin.IN,Pin.PULL_UP)
myLedxx = Pin(Led_r,Pin.OUT)
#definition of the States
butStateNOW = 1
butStateOLD = 1
butStateNOWx = 1
butStateOLDx = 1
butStateNOWxx = 1
butStateOLDxx = 1
LEDState=False
LEDStatex=False
LEDStatexx=False


#RETURN TO MENU
debounce_time = 50

def button_pressed(pin):
    from main import main  # Importiere die main-Funktion aus main.py
    time.sleep_ms(debounce_time)  # Wartezeit für den Knopf-Debouncing
    if button_pin.value() == 0:
        # Der Knopf wurde gedrückt
        print("Knopf wurde gedrückt! Starte main.py.")
        main()  # Starte die main-Funktion aus main.py
        sys.exit("main.py")

# Dem Knopf einen Interrupt-Handler hinzufügen
button_pin.irq(trigger=Pin.IRQ_FALLING, handler=button_pressed)

#infinity loop
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

#KreuzJstickLED.py, copyright = MIT
#used lib neopixel.py (renamed argbled_lib.py) => used class Neopixel (renamed class Argled)
#I had to rename the lib and class cause I hab a Error finding the class Neopixel from lib neopixel.py, after I renamed it Code worked 
#Code by Daniel S. & Michael E., last update March 2024  

from machine import Pin, ADC
from argbled_lib import Argbled
import utime
import random
import sys

#Anzahl Pixel Matrix
numpix = 64
#InPut 8x8 matrix
np = Argbled(numpix, 0, 2, "RGB")
#JoyStick Pins
xAxis = ADC(Pin(26))
yAxis = ADC(Pin(27))
button = Pin(17,Pin.IN, Pin.PULL_UP)
button_pin = Pin(9, Pin.IN, Pin.PULL_UP)

red = (0, 255, 0)
orange = (255, 50, 0)
yellow = (255, 100, 0)
green = (255, 0, 0)
blue = (0, 0, 255)
indigo = (100, 0, 90)
violet = (200, 0, 100)
white = (0, 0, 0)
black = (255,255,255)
colors_rgb = [red, orange, yellow, green, blue, indigo, violet]

delay = 1
utime.sleep(delay)  
np.brightness(42)
blank = (0,0,0)

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

while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    bValue = button.value()
    x = 28
    
    np.set_pixel(x, colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(x+1, colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(x-1, colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(x+8, colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(x-8, colors_rgb[random.randint(0, len(colors_rgb)-1)])
        
    if bValue == 0:
        np.set_pixel(x, white)
        np.set_pixel(x+1, white)
        np.set_pixel(x-1, white)
        np.set_pixel(x+8, white)
        np.set_pixel(x-8, white)
    #rechts
    if xValue <= 600:
        np.set_pixel(x+1, green)
        np.set_pixel(x, white)
        np.set_pixel(x-1, white)
        np.set_pixel(x+8, white)
        np.set_pixel(x-8, white)
    
    #links
    if xValue >= 60000:
        np.set_pixel(x-1, red)
        np.set_pixel(x, white)
        np.set_pixel(x+1, white)
        np.set_pixel(x+8, white)
        np.set_pixel(x-8, white)
    
    #hoch
    if yValue <= 600:
        np.set_pixel(x-8, black)
        np.set_pixel(x, white)
        np.set_pixel(x-1, white)
        np.set_pixel(x+8, white)
        np.set_pixel(x+1, white)
    
    #runter
    if yValue >= 60000:
        np.set_pixel(x+8, blue)
        np.set_pixel(x, white)
        np.set_pixel(x+1, white)
        np.set_pixel(x-8, white)
        np.set_pixel(x-1, white)
        

    np.show()
    utime.sleep(delay)

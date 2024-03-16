#used lib neopixel.py (renamed argbled_lib.py) => used class Neopixel (renamed class Argled)
#I had to rename the lib and class cause I hab a Error finding the class Neopixel from lib neopixel.py, after I renamed it Code worked
#Code by Daniel S. & Michael E., last update March 2024 

from machine import Pin, I2C, reset
from argbled_lib import Argbled
from sh1106 import SH1106_I2C
import utime
import random
import sys


WIDTH = 128
HEIGHT = 64          #Pixelgröße Bildschirm
i2c = I2C(0, scl = Pin(5), sda = Pin(4), freq=400000)
button_pin = Pin(9, Pin.IN, Pin.PULL_UP)
display = SH1106_I2C(WIDTH, HEIGHT, i2c)
display.rotate(True)

led_r = Pin(10, Pin.OUT)
led_g = Pin(12, Pin.OUT)
led_b = Pin(13, Pin.OUT)
ledPi = Pin(25, Pin.OUT)
numpix = 64
np = Argbled(numpix, 0, 2, "RGB")

red = (255, 0, 0)
orange = (255, 50, 0)
yellow = (255, 100, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (100, 0, 90)
violet = (200, 0, 100)
colors_rgb = [red, orange, yellow, green, blue, indigo, violet]

delay = 0.1
utime.sleep(delay)  
np.brightness(42)
blank = (0,0,0)

display.text("HTWK Leipzig",20,0)
display.text("Prg: Disco.py",10,28)
display.show()

#clear common Kathode LED
ledPi.value(1)
led_r.value(0)
led_g.value(0)
led_b.value(0)

# RETURN TO MENU
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
    led_r.toggle()
    utime.sleep(1)
    led_r.toggle()

    np.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.show()
    utime.sleep(delay)
    np.fill((0,0,0))

    led_g.toggle()
    utime.sleep(1)
    led_g.toggle()
 
    np.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.show()
    utime.sleep(delay)
    np.fill((0,0,0))
 
    led_b.toggle()
    utime.sleep(1)
    led_b.toggle()
    utime.sleep(1)
    
    np.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    np.show()
    utime.sleep(delay)
    np.fill((0,0,0))

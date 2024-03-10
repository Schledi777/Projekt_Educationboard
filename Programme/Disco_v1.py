#used lib neopixel.py (renamed argbled_lib.py) => used class Neopixel (renamed class Argled)
#I had to rename the lib and class cause I hab a Error finding the class Neopixel from lib neopixel.py, after I renamed it Code worked
#March 2024 
from machine import Pin
from argbled_lib import Argbled
import utime
import random

led_r = Pin(27, Pin.OUT)
led_g = Pin(26, Pin.OUT)
led_b = Pin(22, Pin.OUT)
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

#clear common Kathode LED
ledPi.value(1)
led_r.value(0)
led_g.value(0)
led_b.value(0)
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

  
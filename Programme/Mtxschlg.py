#Source:https://github.com/Guitarman9119/Raspberry-Pi-Pico-/blob/main/Neopixel/Example2.py#L9C2-L9C14
#Code modified by Daniel S. & Michael E., last update March 2024 
from machine import Pin, I2C, reset
from argbled_lib import Argbled
from sh1106 import SH1106_I2C
import utime
import sys

WIDTH = 128
HEIGHT = 64          #Pixelgröße Bildschirm
i2c = I2C(0, scl = Pin(5), sda = Pin(4), freq=400000)
button_pin = Pin(9, Pin.IN, Pin.PULL_UP)
display = SH1106_I2C(WIDTH, HEIGHT, i2c)
display.rotate(True)
numpix = 64
np = Argbled(numpix, 0, 2, "RGB")
blue = (0, 0, 255)
delay = 0.1
utime.sleep(delay)  
np.brightness(42)
blank = (0,0,0) 

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

display.text("HTWK Leipzig",20,0)
display.text("Matrixschlange",5,28)
display.show()

while True:
    display.show() 
    for x in range(60):
        np.set_pixel(x+1, blue)
        np.show()
        utime.sleep(delay)
        np.set_pixel(x, blue)
        np.show()
        utime.sleep(delay)
        np.set_pixel(x+2, blue)
        np.show()
        utime.sleep(delay)
        np.set_pixel(x, blank)
        utime.sleep(delay)
        np.set_pixel(x+1, blank)
        utime.sleep(delay)
        np.set_pixel(x+2, blank)
        np.show()

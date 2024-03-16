#Code by Daniel S. & Michael E., last update March 2024

from machine import I2C, Pin, reset
from sh1106 import SH1106_I2C
from dht import DHT11
import utime as time
import sys

WIDTH = 128
HEIGHT = 64  # Pixelgröße Bildschirm
button_pin = Pin(9, Pin.IN, Pin.PULL_UP)
ledPi = Pin(25, Pin.OUT)
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)
display = SH1106_I2C(WIDTH, HEIGHT, i2c)
display.rotate(True)
ledPi.value(1)

#RETURN TO MENU
# Wartezeit, um Prelleffekte zu vermeiden
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
    pin = Pin(11, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)
    sensor.measure()
    temp  = sensor.temperature()
    hum = sensor.humidity()
    display.fill(0)
    display.text("HTWK Leipzig",20,0)
    display.text("Temperatur: "+str(temp)+"C",0,28)
    display.text("Luftfeuchte: "+str(hum)+"%",0,42)
    time.sleep(1)
    display.show()

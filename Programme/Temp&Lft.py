#Code by Daniel S. & Micheal E., last update March 2024

from machine import I2C, ADC, Pin
from sh1106 import SH1106_I2C
import sys
import framebuf
from dht import DHT11
import utime as time


WIDTH = 128
HEIGHT = 64          #Pixelgröße Bildschirm
i2c = I2C(0, scl = Pin(5), sda = Pin(4), freq=400000)
display = SH1106_I2C(WIDTH, HEIGHT, i2c)
display.rotate(True)
ledPi.value(1)

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
    time.sleep(0.5)
    display.show()
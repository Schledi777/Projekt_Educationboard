from machine import I2C, Pin
from sh1106 import SH1106_I2C
import time
#Definition Breite und Höhe
WIDTH = 128
HEIGHT = 64
#Display Pin Belegung
i2c = I2C(0, scl = Pin(5), sda = Pin(4), freq=400000)
#Definition der Variable für das Display Name ist frei wählbar
display = SH1106_I2C(WIDTH, HEIGHT, i2c)
#Dreht die Anzeige um 180 Grad
display.rotate(True)

while True:
    display.fill(0)
    display.text("HTWK", 0, 0)
    display.text("TEST", 10, 14)
    display.text("TEST2", 20, 28)
    display.text("TEST3", 40, 42)
    display.show()
    time.sleep(3)

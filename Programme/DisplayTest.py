from machine import I2C, ADC, Pin
from sh1106 import SH1106_I2C
import framebuf
import time
import sys


WIDTH = 128
HEIGHT = 64
#Display Pin Belegung
i2c = I2C(0, scl = Pin(5), sda = Pin(4), freq=400000)
#Return to Menu Button
button_pin = Pin(9, Pin.IN, Pin.PULL_UP)
display = SH1106_I2C(WIDTH, HEIGHT, i2c)
display.rotate(True)

buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)

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

display.fill(0)

display.blit(fb, 96, 0)
display.text("Projekt", 0, 5)
display.text("EducationBoard", 0, 28)
display.text("Prg: DisplayTest.py", 0, 42)
display.show()

time.sleep(3)

for i in range(0, 96):
    display.blit(fb, 96-i, 0)
    display.show()
    time.sleep(0.05)

display.rotate(True)

fb_width=32
fb_height=32
blitx = 0
blity = 0
xdir = 1
xlim = WIDTH-fb_width
ydir = 1
ylim = HEIGHT-fb_height

while True:
    display.text("HTWK",50,5)
    display.text("Leipzig",35,15)
    display.blit(fb, blitx, blity)
    display.show()
    
    #prepare next round
    blitx = blitx+xdir
    if blitx == -1:
        blitx=1
        xdir=1
    if blitx == xlim:
        blitx=xlim-1
        xdir=-1
        
    blity = blity+ydir
    if blity == -1:
        blity=1
        ydir=1
    if blity == ylim:
        blity=ylim-1
        ydir=-1


#Code by Daniel S. & Michael E., Last update march 2024
from machine import I2C, Pin, reset
import sys
button_pin = Pin(9, Pin.IN, Pin.PULL_UP)

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

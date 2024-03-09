# Rotary Menu by Kevin McAleer, May 2021
# modified March 2023 for Projekt 

from machine import Pin, I2C
from os import listdir
from sh1106 import SH1106_I2C
from time import sleep

# I2C variables
id = 0
sda = Pin(4)
scl = Pin(5)
i2c = I2C(id=id, scl=scl, sda=sda)
ledPi = Pin(25, Pin.OUT)

# Screen Variables
WIDTH = 128
HEIGHT = 64
line = 1 
highlight = 1
shift = 0
list_length = 0
total_lines = 6

# create the display

i2c = I2C(0, scl = Pin(5), sda = Pin(4), freq=400000)
display = SH1106_I2C(WIDTH, HEIGHT, i2c)
display.init_display()
display.rotate(True)
ledPi.value(1)

# Setup the Rotary Encoder
button_pin = Pin(9, Pin.IN, Pin.PULL_UP)
direction_pin = Pin(7, Pin.IN, Pin.PULL_UP)
step_pin  = Pin(8, Pin.IN, Pin.PULL_UP)

# for tracking the direction and button state
previous_value = True
button_down = False


def get_files():
    """ Get a list of Python files in the root folder of the Pico """
    
    files = listdir()
    menu = []
    for file in files:
        if file.endswith(".py"):
            menu.append(file)

    return(menu)


def show_menu(menu):
    """ Shows the menu on the screen"""
    
    # bring in the global variables
    global line, highlight, shift, list_length

    # menu variables
    item = 1
    line = 1
    line_height = 10

    # clear the display
    display.fill_rect(0,0,WIDTH,HEIGHT,0)

    # Shift the list of files so that it shows on the display
    list_length = len(menu)
    short_list = menu[shift:shift+total_lines]

    for item in short_list:
        if highlight == line:
            display.fill_rect(0,(line-1)*line_height, WIDTH,line_height,1)
            display.text(">",0, (line-1)*line_height,0)
            display.text(item, 10, (line-1)*line_height,0)
            display.show()
        else:
            display.text(item, 10, (line-1)*line_height,1)
            display.show()
        line += 1 
    display.show()


def launch(filename):
    """ Launch the Python script <filename> """
    global file_list
    # clear the screen
    display.fill_rect(0,0,WIDTH,HEIGHT,0)
    display.text("Launching", 1, 10)
    display.text(filename,1, 20)
    display.show()
    sleep(3)
    exec(open(filename).read())
    show_menu(file_list)


# Get the list of Python files and display the menu
file_list = get_files()
show_menu(file_list)

# Repeat forever
while True:
    if previous_value != step_pin.value():
        if step_pin.value() == False:

            # Turned Left 
            if direction_pin.value() == False:
                if highlight > 1:
                    highlight -= 1  
                else:
                    if shift > 0:
                        shift -= 1  

            # Turned Right
            else:
                if highlight < total_lines:
                    highlight += 1
                else: 
                    if shift+total_lines < list_length:
                        shift += 1

            show_menu(file_list)
        previous_value = step_pin.value()   
        
    # Check for button pressed
    if button_pin.value() == False and not button_down:
        button_down = True

        print("Launching", file_list[highlight-1+shift]) 

        # execute script
        launch(file_list[(highlight-1) + shift])
        
        print("Returned from launch")

    # Decbounce button
    if button_pin.value() == True and button_down:
        button_down = False
from machine import I2C, Pin
import time

class SRF08:
    def __init__(self, i2c, address):
        self.i2c = i2c
        self.address = address

    def send_command(self, command):
        self.i2c.writeto(self.address, bytes([command]))

    def read_distance(self):
        # Trigger ranging in centimeters
        self.send_command(0x51)
        time.sleep_ms(70)  # Wait for ranging to complete

        # Read 16-bit distance value (high byte first)
        data = self.i2c.readfrom_mem(self.address, 2, 2)
        distance = (data[0] << 8) + data[1]

        return distance

#I2C pins and create an I2C object
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)

#SRF08 sensor address
srf08_address = 0xE0

#SRF08 object
srf08 = SRF08(i2c, srf08_address)

while True:
    try:
        distance_cm = srf08.read_distance()
        print("Distance: {} cm".format(distance_cm))
    except Exception as e:
        print("Error:", e)

    time.sleep(1)

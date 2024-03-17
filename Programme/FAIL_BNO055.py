#Source YT: https://www.youtube.com/watch?v=uu4slYGSQPE

#modified march 2024

from machine import Pin, I2C
import time

ADDRESS        = 0x29
EULER_REGISTER = 0x1A

i2c=I2C(1, sda=Pin(14), scl=Pin(15), freq=100_000)
buffer = bytearray(6)
result = [0, 0, 0]

def sum_and_sign(lsb,msb):
    res=((lsb | (msb << 8)) & 0xFFFF)
    if res > 32767:
        res -= 65536
    return res

def init():
    if i2c.readfrom_mem(ADDRESS, 0x00, 1) == b'\xa0':
        config=((0x3d, b'\x00', 80), (0x3f, b'\x20', 1000), (0x3e, b'\x00', 80), (0x07, b'\x00', 80), (0x3f, b'\x80', 1000), (0x3d, b'\x0c', 80))
        for register, value, delay in config:
            i2c.writeto_mem(ADDRESS, register, value)
            time.sleep_ms(delay)
    else:
        while True:
            print("bno055 not found...")
            time.sleep_ms(1000)
        
init()

while True:
    time.sleep_ms(20)
    try:
        i2c.readfrom_mem_into(ADDRESS, EULER_REGISTER, buffer)
        time.sleep_ms(20)
    except Exception as error:
        pass
    
    result[0] = sum_and_sign(buffer[0], buffer[1])
    result[1] = sum_and_sign(buffer[2], buffer[3])
    result[2] = sum_and_sign(buffer[4], buffer[5])
    
    zxy = [i/16 for i in result]
    
    z=int(float(zxy[0]))
    x=int(float(zxy[1]))
    y=int(float(zxy[2]))
    print(z,':',x,':',y)
    time.sleep_ms(50)
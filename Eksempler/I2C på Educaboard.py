from machine import I2C, Pin, SoftI2C
from time import sleep

i2c = I2C(0)

print("Running I2C scanner\n")

while True:
    devices_identified = i2c.scan()
    devices_count = len(devices_identified)
    print("Total number of devices: %d" % devices_count)
    
    if devices_count == 122:
        print("Looks like the I2C bus pull-up resistors are missing")
    else:
        for i in range(devices_count):
            print("Device found at address: 0x%02X" % devices_identified[i])
            
    print()
    
    sleep(1)
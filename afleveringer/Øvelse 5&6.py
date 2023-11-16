from machine import Pin
from time import sleep
led1 = Pin(5,Pin.OUT)
pb1 = Pin(0, Pin.IN)
inkrementer = 0

# for at få den til at opdatere værdien skal man lave: inkrementer = inkerementer + 1

        
while True:
        if pb1.value() == 0:
            led1.value(not led1.value())
            print("tænder/slukker LEd")
            led1.on
            sleep(0.2)
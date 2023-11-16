from machine import Pin
from time import sleep
pb1 = Pin(4, pin.IN)
POTMETER = 34
        if pb1.value() == 0;
            led1.value(not led1.value())
            mqqt.webprint("ESP32 her!")
            sleep(0.2)
            
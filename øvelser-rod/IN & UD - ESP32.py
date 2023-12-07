from machine import Pin

USBin = Pin(25, Pin.IN) 
Pout = Pin(26, Pin.OUT)

While True:
    Pout.value((USBin.value()))
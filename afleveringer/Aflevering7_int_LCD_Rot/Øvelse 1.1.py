#Lavet af Mikkel Due-Pedersen
#Hold 1.A ITTEK
from machine import Pin
RED_PIN = 26
led1 = Pin(RED_PIN, Pin.OUT)
def isr_handler_function(Pin_object):
    led1.value(not led1.value()) #inverter værdien, så hvis 1 laver den til 0 og omvendt

rotary_pushbutton = Pin(14, Pin.IN) #pin objektet
rotary_pushbutton.irq(handler = isr_handler_function, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)

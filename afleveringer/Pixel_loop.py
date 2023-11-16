from machine import Pin, ADC
from time import sleep_ms
from neopixel import NeoPixel
n = 16
p = 25
np = NeoPixel(Pin(p, Pin.OUT), n)
pot = ADC(Pin(34, Pin.IN),atten=3)
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_12BIT)
def set_color(r, g, b):
    for i in range(0):
        np[i] = (r, g, b)
    np.write()
def movepixel(sleep):
    for i in range(1):
        np[i] = (0, 255, 0)
    np.write()
def wheel(sleep):
    if pot_val < 0 or pot_val > 16:
        return(np[1])
    if pot_val < 85:
        return(np[2])
    if pos < 170:
        pos -= 85
        return (0,255-pos*3,pos*3)
    pos -= 170
    return (pos*3,0,255 - pos*3)    
    

while True:
    pot_val = pot.read()
    spaending = pot_val * (3.3/4096)
    print("Analog potentiometer vaerdi:	", pot_val)
    print("\nAnalog potentiometer spaending: ", spaending)
    sleep_ms(4096-pot_val)
    if pot_val == 0:
        movepixel(1)
        
from machine import Pin, ADC
from time import sleep_ms
from neopixel import NeoPixel
#atten er sensitiviteten for potmeteret, tjek dokumentation for anden følsomhed
pot = ADC(Pin(34, Pin.IN),atten=3)
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_12BIT)
led1 = Pin(26, Pin.OUT, value=0)
n = 16
p = 25
np = NeoPixel(Pin(p, Pin.OUT), n)
def set_color(r, g, b):
    for i in range(n):
        np[i] = (r, g, b)
    np.write()
def clear():
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()
while True:
    pot_val = pot.read()
    #udregner spændingen, da vi potmeteret går fra 0-4096 og vi arbejder med 3.3v
    spaending = pot_val * (3.3/4096)
    print("Analog potentiometer vaerdi:	", pot_val)
    print("\nAnalog potentiometer spaending: ", spaending)
    led1.value(not led1.value())
    sleep_ms(4096-pot_val) #nu er den inverted, så desto højere den er hurtigere er den
    
    if pot_val < 500:
        set_color(255,0,0)
        sleep_ms(25)
        clear()
                    #man kan anvende 'and' funktion i stedet for !=
                    #pot_val in range(1501, 3001)
    elif pot_val > 1500 != pot_val < 3000:
        set_color(255,255,0)
        sleep_ms(25)
        clear()
    elif pot_val > 3000:
        set_color(0,255,0)
        sleep_ms(25)
        clear()
        
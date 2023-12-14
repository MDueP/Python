#Øvelse 2.3 - Rotary encoder så der printes i retning der drejes i shell
#Lavet af Mikkel Due-Pedersen
#Hold 1.A ITTEK
from gpio_lcd import GpioLcd
from machine import Pin
from rotary_encoder import RotaryEncoder

test = True
rot = RotaryEncoder()

while test:
        res = rot.re_full_step()
        rot.counter += res
        if res == 1:
            print("Højre/CW: ", rot.counter)
        elif res == -1:
            print("Venstre/CW: ", rot.counter)
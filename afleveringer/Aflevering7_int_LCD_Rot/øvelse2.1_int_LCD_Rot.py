# Øvelse 2.1 - Skriv dit navn på LCD Display
from gpio_lcd import GpioLcd
from machine import Pin

# laver objektet lcd, så den indeholder alle de pins LCD'en bruger
lcd = GpioLcd(rs_pin=Pin(27), enable_pin=Pin(25),
                 d4_pin=Pin(33), d5_pin=Pin(32),
                 d6_pin=Pin(21), d7_pin=Pin(22),
                 num_lines=4, num_columns=20)
lcd.clear() #rengør LCD'en
lcd.putstr("Mikkel Due") #putter en string ind med mit navn på LCD'en
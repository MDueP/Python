#Øvelse 2.2 - Lav eget specialtegn og indsæt efter eget navn
#Lavet af Mikkel Due-Pedersen
#Hold 1.A ITTEK
from gpio_lcd import GpioLcd
from machine import Pin

# laver objektet lcd, så den indeholder alle de pins LCD'en bruger
lcd = GpioLcd(rs_pin=Pin(27), enable_pin=Pin(25),
                 d4_pin=Pin(33), d5_pin=Pin(32),
                 d6_pin=Pin(21), d7_pin=Pin(22),
                 num_lines=4, num_columns=20)
lcd.clear()
lcd_custom_smiley = bytearray([0x0A,0x0A,
                               0x0A,0x00,
                               0x00,0x11,
                               0x0E,0x00])
lcd.putstr("Mikkel Due")
lcd.move_to(12, 0) #fortæller hvor min customchar bliver placeret
lcd.custom_char(0, lcd_custom_smiley)
lcd.putchar(chr(0))
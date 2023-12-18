from gpio_lcd import GpioLcd
from rotary_encoder import RotaryEncoder
from machine import Pin
from lcd_menu import Menu
from LMT84 import LMT84
from hcsr04 import HCSR04
import uasyncio as asyncio

lmt84 = LMT84()

rot_pb = Pin(14, Pin.IN, Pin.PULL_UP)
rot = RotaryEncoder()
ultrasonic = HCSR04(2, 15)
lcd = GpioLcd(rs_pin=Pin(27), enable_pin=Pin(25),
                  d4_pin=Pin(33), d5_pin=Pin(32),
                  d6_pin=Pin(21), d7_pin=Pin(22),
                  num_lines=4, num_columns=20)

menu = Menu(lcd, rot, rot_pb)
led1 = Pin(26, Pin.OUT)

# https://maxpromer.github.io/LCD-Character-Creator/
lcd_custom_char_degrees = bytearray([0x0E, 0x0A,
                                     0x0E, 0x00,
                                     0x00, 0x00,
                                     0x00, 0x00])


def lcd_temperature_celsius():
    """callback function to display temperature celsius on lcd"""
    lcd.move_to(1, menu.selected)  # moves to selected line
    lcd.putstr("                  ")  # delete selected line text by adding whitespaces
    lcd.move_to(1, menu.selected)
    lcd.putstr(f"Temp is {lmt84.celsius_temperature():.1f} ")
    lcd.custom_char(2, lcd_custom_char_degrees)
    lcd.putchar(chr(2))
    lcd.putstr("C")


def lcd_temperature_fahrenheit():
    """callback function to display temperature fahrenheit on lcd"""
    lcd.move_to(1, menu.selected)  # moves to selected line
    lcd.putstr("                  ")  # delete selected line text by adding whitespaces
    lcd.move_to(1, menu.selected)
    lcd.putstr(f"Temp is {lmt84.fahrenheit_temperature():.1f} ")
    lcd.custom_char(2, lcd_custom_char_degrees)
    lcd.putchar(chr(2))
    lcd.putstr("F")


def lcd_temperature_kelvin():
    """callback function to display temperature kelvin on lcd"""
    lcd.move_to(1, menu.selected)  # moves to selected line
    lcd.putstr("                  ")  # delete selected line text by adding whitespaces
    lcd.move_to(1, menu.selected)
    lcd.putstr(f"Temp is {lmt84.kelvin_temperature():.1f}K")


def lcd_toggle_led1():
    """callback to Toggle led1"""
    lcd.move_to(1, menu.selected)  # moves to selected line
    lcd.putstr("                  ")  # delete selected line text by adding whitespaces
    lcd.move_to(1, menu.selected)
    lcd.putstr("LED1 is toggled!")
    led1.value(not led1.value())


def HCSR04():
    while True:
        lcd.move_to(1, menu.selected)
        lcd.putstr("                  ")
        lcd.move_to(1, menu.selected)
        lcd.putstr(f"Distance: {ultrasonic.distance_cm()} CM")

menu.tilføj_menu("Temp celsius", lcd_temperature_celsius)
menu.tilføj_menu("Temp fahrenheit", lcd_temperature_fahrenheit)
menu.tilføj_menu("Temp kelvin", lcd_temperature_kelvin)
menu.tilføj_menu("Toggle LED1", lcd_toggle_led1)
menu.tilføj_menu("HCSR04", HCSR04)
print(f"ADC: {lmt84.adc_average():.1f}") #for at se ADC værdien der bliver givet til LMT84 modulet
menu.vismenu()
menu.menuloop()
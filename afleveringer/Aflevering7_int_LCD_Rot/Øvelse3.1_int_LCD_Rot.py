# TODO

# lav en klasse her til at styre menu system til LCD display
from time import sleep
import uasyncio as asyncio
from machine import Pin

class Menu:
    def __init__(self, lcd, rotary, tryk):
        self.lcd = lcd
        self.rotary = rotary
        self.tryk = tryk #rotary knap tryk
        
        self.menu_items = [] # gemmer menu valgene i en liste
        self.line = 1
        self.highlight = 1
        self.shift = 0
        self.list_length = 0
        self.total_lines = 4
        self.select_item = 0
        
        self.rotary_last_state = self.rotary.re_full_step()
        self.rotary_button_pressed = False
        self.int_knap()
        self.int_lcd()
        self.int_rotary()
    def int_knap(self):
        self.tryk.irq(handler=self.tryk_callback, trigger=Pin.IRQ_FALLING)
        
    def tryk_callback(self, pin):
        if not self.rotary_button_pressed:
            self.rotary_button_pressed = True
    def int_lcd(self): #renser LCD-Displayet og sætter den til 0,0
        self.lcd.clear()
        self.lcd.move_to(0, 0)
        
    def int_rotary(self):
        self.rotary_last_state = self.rotary.re_full_step()
        
    def tilføj_menu(self, tekst, callback): #tilføjer til menuen
        if callable(callback):
            self.menu_items.append({"tekst": tekst, "callback": callback})
        
    def vismenu(self):
        self.lcd.clear()
        self.line = 1
        self.list_length = len(self.menu_items)
        short_list = self.menu_items[self.shift:self.shift + self.total_lines]
        
        for item in short_list:
            if self.highlight == self.line:
                self.lcd.move_to(1, self.line-1)
                self.lcd.putstr(item["tekst"])
                self.selected = self.line - 1
            else:
                self.lcd.move_to(1, self.line - 1)
                self.lcd.putstr(item["tekst"])
                self.line += 1
        self.lcd.move_to(0, self.selected)
        self.lcd.blink_cursor_on()
        

    async def menu_nav(self):
        while True:
            res = self.rotary.re_full_step()
            if res == -1:
                if self.highlight > 1:
                    self.highlight -= 1
                else:
                    if self.shift > 0:
                        self.shift -= 1
                self.vismenu()
            if res == 1:
                if self.highlight < self.total_lines:
                    self.highlight += 1
                else:
                    if self.shift + self.total_lines < self.list_length:
                        self.shift += 1
                self.vismenu()
            self.rotary_last_state = res
            if self.rotary_button_pressed:
                callback = self.menu_items[self.selected + self.shift]["callback"]
                if callback:
                    callback()
            if self.rotary_button_pressed:
                await asyncio.sleep(0.2)
                self.rotary_button_pressed = False
    def menuloop(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.menu_nav())
        loop.run_forever()
    
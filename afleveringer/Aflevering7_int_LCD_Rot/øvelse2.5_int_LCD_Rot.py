#Øvelse 2.5 - Lav en menu der vises i shell og hvor det valgte menu-item highligts når der drejes på rotary
#Lavet af Mikkel Due-Pedersen
#Hold 1.A ITTEK
from time import sleep
from rotary_encoder import RotaryEncoder

rot = RotaryEncoder()
line = 1
highlight = 1
shift = 0
list_length = 0
total_lines = 4

def show_menu(menu):
    global line, highlight, shift, list_length
    item = 1
    line = 1
    list_length = len(menu)
    short_list = menu[shift:shift+total_lines]
    for item in short_list:
        if highlight == line:
            print(item.upper(), line-1)
        else:
            print(item, line-1)
        line += 1
menu_items = ["menu1", "menu2", "menu3", "menu4"]
show_menu(menu_items)

while True:
    res = rot.re_full_step()
    if res == -1:
        if highlight > 1:
            highlight -= 1
        else:
            if shift > 0:
                shift -= 1
        show_menu(menu_items)
    if res == 1:
        if highlight < total_lines:
            highlight +=1
        else:
            if shift+total_lines < list_length:
                shift +=1
        show_menu(menu_items)
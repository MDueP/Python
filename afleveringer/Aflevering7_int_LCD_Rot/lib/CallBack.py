from machine import Pin
from time import sleep


class Callback:
    def __init__(self, Rpb):
        self.Rpb = Rpb
        self.menulist = []
        self.Rot_gem = None
        self.Rpb_trykket = False
        self.callback_count = 0
        self.Rpbinterrupt()
        
    def Rpbinterrupt(self):
        self.Rpbinterrupt.irq(handler=self.encoder_button_callback, trigger=Pin.IRQ_Falling)

    
#Øvelse 2.4 - Klasse der kan tage et pin objekt som argument
#metode der tager tekst og callbacks som argumenter og tilføj til en list med dic
#rotary enc knap trykket næste callback fra listens dic kaldes
#tilføj 2 callback funktioner mere som printer en besked i shell når de kaldes

#Lavet af Mikkel Due-Pedersen
#Hold 1.A ITTEK
from time import sleep
from machine import Pin

class PinOb:
    def __init__(self, rot_tryk):
        self.rot_knap = Pin(rot_tryk, Pin.IN)
        
        self.pinob = [] #gemmer callbacks i en liste
        self.select_index = 0 #anvender index i listen, for at vælge callback
        self.rot_knap_trykket = False
        self.rot_knap.irq(handler=self.knap_callback, trigger=Pin.IRQ_FALLING)
    def knap_callback(self, pin):
        if not self.rot_knap_trykket:
            self.rot_knap_trykket = True
    def tilføj_pinob(self, tekst, callback):
        self.pinob.append({"tekst": tekst, "callback": callback})
    #callbacks 1-3
    def print_besked1(self):
        print("Callback 1")
        
    def print_besked2(self):
        print("Callback 2")
        
    def print_besked3(self):
        print("Callback 3")
    #loop der anvender class
    def pinob_loop(self):
        while True:
            if self.rot_knap_trykket:
                self.rot_knap_trykket = False
                
                if self.select_index < len(self.pinob):
                    callback = self.pinob[self.select_index]["callback"]
                    if callback:
                        callback()
                self.select_index = (self.select_index + 1) % len(self.pinob)
            sleep(0.2)
#eksempel på at det virker
rot_tryk = 14 #rotary encoders Pin nummer
pinob = PinOb(rot_tryk)

pinob.tilføj_pinob("besked1", pinob.print_besked1)
pinob.tilføj_pinob("besked2", pinob.print_besked2)
pinob.tilføj_pinob("besked3", pinob.print_besked3)

pinob.pinob_loop()
#Den hopper hen til den næste item i listen, hver gang knappen trykkes. Det glæder både op og ned
# noinspection NonAsciiCharacters
class ohmslov:
    def __init__(self):
        self.spænding = None
        self.strøm = None
        self.modstand = None
        self.effekt = None
    def spænding(self):
        if self.effekt is not None and self.strøm is not None:
            self.spænding = self.effekt / self.strøm
            return self.spænding
        elif self.effekt is not None and self.modstand is not None:
            self.spænding = (self.effekt*self.modstand)**(1/2)
            return self.spænding
        elif self.strøm is not None and self.modstand is not None:
            self.spænding = self.strøm*self.modstand
            return self.spænding
    def strøm(self):
        if self.effekt is not None and self.modstand is not None:
            self.strøm = (self.effekt/self.modstand)**(1/2)
            return self.strøm
        elif self.effekt is not None and self.spænding is not None:
            self.strøm = self.effekt/self.spænding
            return self.strøm
        elif self.spænding is not None and self.modstand is not None:
            self.strøm = self.spænding/self.modstand
            return self.strøm
    def modstand(self):
        if self.spænding is not None and self.strøm is not None:
            self.modstand = self.spænding / self.strøm
            return self.modstand
        elif self.spænding is not None and self.effekt is not None:
            self.modstand = (self.spænding**(2))/self.effekt
            return self.modstand
        elif self.effekt is not None and self.strøm is not None:
            self.modstand = self.effekt/(self.strøm**(2))
            return self.modstand
    def effekt(self):
        if self.spænding is not None and self.strøm is not None:
            self.effekt = self.spænding * self.strøm
            return self.effekt
        elif self.spænding is not None and self.modstand is not None:
            self.effekt = (self.spænding**(2))/self.modstand
            return self.effekt
        elif self.strøm is not None and self.modstand is not None:
            self.effekt = (self.strøm**(2))* self.modstand
            return self.effekt


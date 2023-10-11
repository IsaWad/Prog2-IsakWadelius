
class Djur:
    def __init__(self, namn):
        self.namn = namn

    def sov(self):
        print(f"{self.namn} sover.")

    def at(self):
        print(f"{self.namn} äter.")

class Fågel(Djur):
    def __init__(self, namn, vingspann):
        super().__init__(namn)
        self.vingspann = vingspann
    

class Fisk(Djur):
    def __init__(self, namn, maxdjup):
        super().__init__(namn)
        self.maxdjup = maxdjup

    def simmar(self):
        print(f"{self.namn} simmar.")

class Haj(Fisk):
    def __init__(self, namn, maxdjup, antalTänder):
        super().__init__(namn, maxdjup)
        self.antalTänder = antalTänder
    def at(self, djur):
        print(f"{self.namn} äter {djur}")

class Torsk(Fisk):
    def __init__(self, namn, maxdjup, hastighet):
        super().__init__(namn, maxdjup)
        self.hastighet = hastighet


def fånga(haj,torsk):
    maxdjup = haj.maxdjup
    hastighet = torsk.hastighet
    if maxdjup > hastighet and hastighet < 30:
        return True
    else:
        return False
    

class Fordon:
    def kör(self):
        print("Nu kör vi!")

class Bil(Fordon):
    def tuta(self):
        print("Tuuut!!")

class Cykel(Fordon):
    def plinga(self):
        print("Pling! Pling!")

class Sportbil(Bil):
    def kör(self):
        print("Brum")

torsk = Torsk("Hans", 100, 400)
haj = Haj("Bert", 50, 100)

resultat = fånga(haj, torsk)
torsk.sov()
haj.at("torsk")
#print(resultat)


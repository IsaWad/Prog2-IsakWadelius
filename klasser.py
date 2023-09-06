class Elev:
    def __init__(self, namn, ålder, godkänd):
        self.namn = namn
        self.ålder = ålder
        self.godkänd = godkänd
        self.glad = False

    def presentera(self):
        print("Hej jag heter", self.namn, ". Jag är", self.ålder, "år gammal.")

    def humör(self):
        if self.godkänd == True:
            self.glad = True

        if self.glad == True:
            print(self.namn, "är glad")
        else:
            print(self.namn, "är ledsen")



elev1 = Elev("Hans", 8, False)
print(elev1.__dict__)
elev1.presentera()
elev1.humör()
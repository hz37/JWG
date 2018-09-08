# Definitie van een class.

class MijnVoorbeeldClass:
    """Simpel voorbeeld van class in Python"""
    mijn_geheime_getal = 0
    
    def compute(self):
        self.mijn_geheime_getal = 42
        
    def waarde(self):
        if self.mijn_geheime_getal == 0:
            return 'Ik weet het niet'
        else:
            return self.mijn_geheime_getal

# Maak een object van het type MijnVoorbeeldClass.
			
mijn_voorbeeld = MijnVoorbeeldClass()

# Vraag de huidige waarde op.

x = mijn_voorbeeld.waarde()

print(x)

# Vraag het mijn_voorbeeld object om zichzelf aan te passen.

mijn_voorbeeld.compute()

# Vraag nu nog een keer de huidige waarde op.

x = mijn_voorbeeld.waarde()

print(x)


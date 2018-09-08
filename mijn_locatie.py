# Gegevens over de zon en de maan.
# Geprogrammeerd in Python versie 3.6.1
# Auteur: Jouw Naam Hier.

# De modules die we nodig hebben.

import ephem
from ephem import cities

# Eigen functies.

def leesbare_datumtijd(datum_tijd):
    """Zet PyEphem datum_tijd om in leesbare string zonder microseconden."""
    return ephem.localtime(datum_tijd).isoformat(' ')[0:19]

# Waar bevindt de gebruiker zich?

woonplaats = input('Waar ben je? ')
if woonplaats.find(',') == -1:
	woonplaats += ', Netherlands'
print(woonplaats)

try:
    plaats = cities.lookup(woonplaats)
except ValueError as e:
    print(e)    
    quit()
except:
    print('Het lukte me niet om de coordinaten van jouw locatie te vinden.')
    quit()

# Maak een Zon.

zon = ephem.Sun()

# Geef volgende zonsondergang en zonsopgang weer.

zon_onder = plaats.next_setting(zon)
print('Volgende zonsondergang:\t%s' % leesbare_datumtijd(zon_onder))

zon_op = plaats.next_rising(zon)
print('Volgende zonsopgang:\t%s' % leesbare_datumtijd(zon_op))

# Geef volgende volle maan en nieuwe maan weer.

volle_maan = ephem.next_full_moon(ephem.now())
print('Volgende volle maan:\t%s' % leesbare_datumtijd(volle_maan))

nieuwe_maan = ephem.next_new_moon(ephem.now())
print('Volgende nieuwe maan:\t%s' % leesbare_datumtijd(nieuwe_maan))


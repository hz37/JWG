import ephem
import math

geboorte_datum = input('Wanneer ben je geboren? yyyy/mm/dd ');
try:
    datum1 = ephem.date(geboorte_datum)
except ValueError:
    print('%s??? Grappenmaker...' % geboorte_datum)
    quit()
    
datum2 = ephem.now()
delta = datum2 - datum1

print('Je bent %d jaar oud' % math.floor(delta / 365))
print('Dat zijn %d weken' % round(delta / 7))
print('Je bent %d dagen oud' % delta)
print('Je leeft al %d uren' % round(delta * 24))


"""
Python 3.6.0rc1 (v3.6.0rc1:29a273eee9a5, Dec  7 2016, 05:07:52) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
================ RESTART: D:/make/UV/python uv3 2017/datum.py ================
Wanneer ben je geboren? yyyy/mm/dd 1967/01/22
Je bent 50 jaar oud
Dat zijn 2634 weken
Je bent 18439 dagen oud
Je leeft al 442557 uren
>>> 
"""

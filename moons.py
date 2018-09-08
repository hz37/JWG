import ephem

# Bewaar manen en hun weergave letters in een lijst
# met tuples. 

manen = ((ephem.Io(),       'i'), 
         (ephem.Europa(),   'e'), 
		 (ephem.Ganymede(), 'g'), 
		 (ephem.Callisto(), 'c'))

# We willen weten hoe de Jupiter manen op dit moment staan.		 
		 
nu = ephem.now()

# Maak een lege regel waar we zowel Jupiter als
# zijn vier grootste manen in kunnen weergeven.

lengte = 80
regel = lengte * [' ']

# Plaats Jupiter als een J in het midden van de regel.

jupiterIndex = int(lengte / 2) + 1
regel[jupiterIndex] = 'J'

# Loop door de lijst met manen.
	
for maan, karakter in manen:
    # Waar staat deze maan op dit moment?

    maan.compute(nu)
	
	# Rond af op een heel getal.

    pos = int(round(-maan.x + (lengte / 2)))

	# Voorkom dat we de J overschrijven met een maan.

    if pos != jupiterIndex:
        regel[pos] = karakter	
	
# Geef weer.

print(''.join(regel))

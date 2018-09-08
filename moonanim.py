import ephem

manen = ((ephem.Io(),       'i'), 
         (ephem.Europa(),   'e'), 
		 (ephem.Ganymede(), 'g'), 
		 (ephem.Callisto(), 'c'))

nu = ephem.now()

interval = ephem.minute
m = ephem.Europa()
t = nu

lengte = 80
jupiterIndex = int(lengte / 2) + 1

while True:
    regel = lengte * [' ']
    regel[jupiterIndex] = 'J'
    for maan, karakter in manen:
        maan.compute(nu)
        pos = int(round(-maan.x + lengte / 2))
        if pos != jupiterIndex:
            regel[pos] = karakter	
	
    print(str(ephem.date(nu)), ''.join(regel))
    nu += interval
	

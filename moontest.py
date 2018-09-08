import ephem
import time

nu = ephem.now()

interval = ephem.hour
m = ephem.Callisto()
t = nu

minC = 0.
maxC = 0.

while True:
    m.compute(t)
    if m.x < minC:
        minC = m.x	
    if m.x > maxC:
        maxC = m.x	
    print("Min: %+.2f\tMax: %+.2f" % (minC, maxC))
    t += interval


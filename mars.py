from array import array
import ephem
import matplotlib.pyplot as plt

m = ephem.Mars()
d = ephem.now()
y = array('d')
x = range(0, 365)

for i in x:
    m.compute(d + i)
    y.append(m.earth_distance)
    print(m.earth_distance)
    print(ephem.Date(d+i))
	
plt.plot(x, y)
plt.show()

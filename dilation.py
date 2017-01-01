from math import sqrt

def dilation(snelheid):
	c = 299792458 # de lichtsnelheid in meters/seconde.

	if snelheid > c:
		print("Je kunt niet sneller dan het licht!")
		return -1

	return 1.0 / sqrt(1.0 - pow(snelheid, 2) / pow(c, 2))

antwoord = input("Hoe snel beweegt de raket van je af (in meters/seconde)?")

try:
	snelheid = float(antwoord)

	lorentz_factor = dilation(snelheid)
	
	if lorentz_factor >= 0:
		print("10 seconden in de raket zijn er %f bij jou" % (10.0 * lorentz_factor))
except:
	print("Ik begreep je niet.")

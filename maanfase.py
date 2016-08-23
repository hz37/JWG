# Maanfase uitrekenen met PyEphem.

# We gebruiken twee packages (bibliotheken).

import datetime
import ephem

# Welke dag is het nu?

vandaag = datetime.datetime.now()

# En wanneer is de volgende nieuwe maan?

nieuwe_maan = ephem.next_new_moon(vandaag)
print("De volgende nieuwe maan is op " + str(nieuwe_maan))


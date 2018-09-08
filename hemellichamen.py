import ephem

hemellichamen = ('Sun', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Moon')

for hemellichaam in hemellichamen:
    functie = getattr(ephem, hemellichaam)
    hemellichaam_object = functie()
    hemellichaam_object.compute()
    sterrenbeeld = ephem.constellation(hemellichaam_object)
    print(hemellichaam + '\t staat nu in\t' + sterrenbeeld[1])

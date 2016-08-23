# We gebruiken twee packages (bibliotheken).

import datetime
import ephem

# Voor elke dag in december.

for dag in range(1, 32):
        datum = datetime.date(2016, 12, dag)
        venus = ephem.Venus(datum)
        sterrenbeeld = ephem.constellation(venus)[1]
        print('Op', datum, 'staat Venus in', sterrenbeeld)

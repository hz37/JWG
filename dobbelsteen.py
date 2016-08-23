# Dobbelsteen uit de aardatmosfeer.

import re
import sys

import urllib.request

# Vraag om 1 getal van 1 tot en met 6 van random.org.

web_pagina = 'https://www.random.org/integers/?num=1&' \
	'min=1&max=6&col=1&base=10&format=plain&rnd=new'

verzoek = urllib.request.Request(web_pagina)

# Controleer of het niet mis gaat.

try:
    response = urllib.request.urlopen(verzoek)
except urllib.error.URLError as error:
    print('Er ging iets mis', error.reason)
else:
    resultaat = response.read()

    # Selecteer alleen het getal uit de output.

    nummer = re.search('\d+', str(resultaat))
    print('De dobbelsteen gooit:', nummer.group(0))

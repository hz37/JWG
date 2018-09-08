from astropy.io import fits
import matplotlib.pyplot as plt
import os.path
import sys

if len(sys.argv) != 2:
	print('python fitsviewer.py naam_van_plaatje')
	exit()

fits_plaatje = sys.argv[1]	
	
if os.path.isfile(fits_plaatje):	
	h = fits.open(fits_plaatje)
	plt.imshow(h[0].data)
	plt.show(block = True)
else:
	print(fits_plaatje + ' kan ik niet vinden!')


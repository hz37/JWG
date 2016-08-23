# Rename script for Mark Meewis sfx drive.
# H.Zimmerman, June 12, 2016.

import codecs
import os
import string

def transmogrify(omschrijving):
	# Turn omschrijving into valid filename.
	validFilenameChars = "-_() %s%s" % (string.ascii_letters, string.digits)
	returnValue = ''.join(c for c in omschrijving if (c in validFilenameChars))
	returnValue = ' '.join(returnValue.split())
	return returnValue[:250].strip()

with codecs.open('/Volumes/sfx/data.txt', 'r', 'latin-1') as datafile:
	skipfirstline = datafile.readline()
	print(skipfirstline)
	while True:
		omschrijving = datafile.readline().strip()
		if omschrijving == '':
			break;
		else:
			# rename
			oldname = '/Volumes/sfx/' + datafile.readline().strip()
			oldname = oldname.replace('\\', '/')
			if os.path.isfile(oldname):
				(head, tail) = os.path.split(oldname)
				omschrijving = transmogrify(omschrijving)
				newname = os.path.join(head, omschrijving + '.wav')
				while os.path.isfile(newname):
					newname = newname + '-'
				os.rename(oldname, newname)
				print('renamed:\n' + oldname + '\n' + newname + '\n\n')
			else:
				print('SKIP :' + oldname)

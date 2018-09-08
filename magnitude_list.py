#!/usr/local/bin/python3

# Magnitude tabel.
# Hens Zimmerman, 03-05-2016.

import math
import sys

if not sys.version_info >= (3,0):
    print("Je hebt minstens python 3 nodig voor dit script")
    exit()

# Vijfdemachts wortel van 100.

mag1_diff = pow(100, 1 / 5)

# Print tabel van magnitudes en hoe veel keer helderder
# deze zijn ten opzichte van magnitude 0.
# Gebruikt format specifiers om de tabel mooi uit te lijnen.
# Je kunt de range (-5, 5) aanpassen om de tabel uit te breiden.

for i in range (-5, 5):
    print("Magnitude {0:>2}: {1:8.4f} x zo helder als magnitude 0".
        format(i, 1 / pow(mag1_diff, i)))

#!/usr/local/bin/python3

# Bereken verschil in helderheid tussen twee objecten op basis van magnitude.
# Hens Zimmerman, 01-05-2016.

import math
import sys

def controleer_versie():
    """Controleer of we wel met de juiste python werken"""
    if not sys.version_info >= (3,0):
        print("Je hebt minstens python 3 nodig voor dit script")
        exit()

def magnitude_input():
    """Vraag om een magnitude"""
    num_str = input("Magnitude van eerste object: ").strip()
    try:
        return float(num_str);
    except:
        print("Dat is geen nummer")
        exit()

controleer_versie()

magnitude1 = magnitude_input()
magnitude2 = magnitude_input()

mag1_diff = pow(100, 1 / 5)

ratio = math.pow(10.0, (magnitude1 - magnitude2) / -mag1_diff)

print("Object 1 (magnitude {0}) is {1:.8f} keer zo helder als object 2 (magnitude {2})".
    format(magnitude1, ratio, magnitude2))

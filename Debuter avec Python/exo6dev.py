# Exercice 6

import random
import math
#Quelles sont les formules permettant de calculer ce volume et cette aire ?
print("La formule permettant de calculer le volume du cylindre est: π(r**2)h")
print("La formule permettant de calculer la surface du cylindre est: 2πrh+2πr ")

#Quelles sont les variables que l'on va utiliser ? Quels sont leurs types ?
print("Les variables qu'on va utiliser sont: rayon(r) et hauteur(h). Ils sont tout deux de type float.")

#Écrire les fonctions effectuant ces calculs.
r = random.randint(1, 10)
h = random.randint(1, 10)
pi = (math.pi)

def volume_cylindre(r, h):
    volume = pi * (r**2) * h
    volumeApprox = round(volume, 2)
    return volumeApprox

def surface_cylindre(r, h):
    surface = (2 * pi * r * h) + (2 * pi * (r ** 2))
    surfaceApprox = round(surface, 2)
    return surfaceApprox

print("Le volume du cylindre avec rayon", r ,"et de hauteur", h , "est de", volume_cylindre(r, h))
print("La surface du cylindre avec rayon", r ,"et de hauteur", h , "est de", surface_cylindre(r, h))

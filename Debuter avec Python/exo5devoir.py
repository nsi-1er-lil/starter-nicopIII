# Exercice 5

import random
import math
#Quelle est la formule permettant de calculer le périmètre d'un cercle ?
print("1. La formule pour calculer le perimetre d'une cercle est: 2πr ")

#Quel argument doit prendre en entrée la fonction périmètre_cercle ? Quel serait le type de cet argument ?
print("2. L'argument est le rayon du cercle. Cet argument serait de type float")

#Compléter l'algorithme de la fonction ci-dessus afin qu'elle renvoie le périmètre d'un cercle.
r = random.randint(1, 10)
pi = (math.pi)
def perimetre_cercle(r):
    perimetre = 2 * pi * r
    perimetreApprox = round(perimetre, 2)
    return perimetreApprox
print("Le perimetre du cercle de rayon", r , "est de environ ", perimetre_cercle(r))

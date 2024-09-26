# Exercice 7

#Quelles sont les variables que la fonction doit prendre en entrée ? Quels sont leurs types ?
print("Les variables de la fonction dont la taille et la masse. Ces variables sont tous deux des floats.")

#La fonction doit-elle renvoyer quelque chose ? Si oui, de quel type ?
print("La fonction doit renvoyer l'IMC de l'individu. Cette valeur sera de type float")

#Compléter la fonction IMC écrite en Python ci-dessous.
import random

def IMC(m, t):
    imc = m / (t ** 2)
    imcApprox = round(imc, 2)
    return imcApprox


#Écrire un appel de cette fonction pour une taille de 1,75 m et un poids de 65 kg.
m = 65
t = 1.75
print("L'IMC d'une personne avec une masse de", m , "kg et une taille de", t , "m est de", IMC(m,t) )

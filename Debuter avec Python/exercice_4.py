import random


#Trouver l'aire et le perimetre d'un carre
c = random.randint(1, 10)
P = c * 4
A = c ** 2 
b = A > 5 
print("On prend ", c, "comme la longueure d'un cote")
print("Le perimetre du carre est de", P)
print("L'aire du carre est de", A )
print("L'aire du carre est superieur a 5 ?", b)

# Fonction pour calculer le perimetre d'un carre
x = random.randint(1, 10)
def perimetre(x):
    return x * 4 


print("Le perimetre du carre, calculer avec une fonction, en utilisant", x, "comme longueure d'un cote, est de", perimetre(x))

#Fonction pour calculer l'air d'un carre
def surface(x):
    return x ** 2 

print("L'aire dur carre, calculer avec une fonction, en utilisant", x, "comme longueure d'un cote, est de", surface(x))

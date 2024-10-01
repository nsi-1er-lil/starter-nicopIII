#exo 2


def jeu_video(x) :
    votre_sante = 100
    sante_adversaire = 200
    puissance_attaque = 120
    if x <= 2 :
        votre_sante = votre_sante // 2
    elif 3<= x <= 8 :
        sante_adversaire = sante_adversaire - puissance_attaque
    else :
        sante_adversaire = 0
    print('Nombre de :', x,'| Votre sante',votre_sante,'| Sante adverse',sante_adversaire)
jeu_video(2),jeu_video(8),jeu_video(10)
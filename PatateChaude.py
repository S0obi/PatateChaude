from CircularList import CircularList
from Joueur import Joueur
from random import randint

nbJoueur = input("Nombre de joueur : ")
nbJoueur = int(nbJoueur)

circularListJ = CircularList(Joueur(input("Nom du joueur 1 : ")))

for i in range(1, nbJoueur):
    circularListJ.insertAfter(Joueur(input("Nom du joueur " + str(i+1) + " : ")))

j = circularListJ.head
while circularListJ.length() > 1:
    count = 0
    nbPasseMax = randint(2, 3*nbJoueur)
    while count < nbPasseMax:

        sens = randint(0, 1)

        if sens == 0: # gauche
            print("gauche : " + j.precedent.name + " a la patate chaude !")
            j = j.precedent
        else: # droite
            print("droite : " + j.suivant.name + " a la patate chaude !")
            j = j.suivant

        count += 1

    print(j.name + " a perdu\n")
    circularListJ.remove(j)
    input()

print(circularListJ.head.name + " a gagné !")

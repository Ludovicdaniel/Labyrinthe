# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

from carte import Carte
from labyrinthe import Labyrinthe
from labyrinthe import sauvegarder_labyrinthe
from labyrinthe import recup_labyrinthe_sauvegarde

print("#########   Bienvenue dans roboc !!   ########");
print(" Que voulez-vous faire ? ")
print(" 1 - Commencer une nouvelle partie")
print(" 2 - Reprendre la partie en cours")

# On demande le choix à l'utilisateur
select=0
while not (select == 1 or select == 2):
    select = input("Tapez votre choix : ")
    try:
        select = int(select)
    except ValueError:
        print("Choix invalide : Vous devez taper un nombre")
        continue

if select == 1:
    # On charge les cartes existantes
    cartes = []
    for nom_fichier in os.listdir("cartes"):
        if nom_fichier.endswith(".txt"):
            chemin = os.path.join("cartes", nom_fichier)
            nom_carte = nom_fichier[:-3].lower()
            with open(chemin, "r") as fichier:
                contenu = fichier.read()
		# Création d'une carte, à compléter
                try:
                    carte = Carte(nom_carte,contenu)
                except ValueError as err:
                    print ("Erreur de lecture de {} : {}.").format(chemin,str(err))
                else:
                    cartes.append(carte)



    # On affiche les cartes existantes
    print("Labyrinthes existants :")
    for i, carte in enumerate(cartes):
        print("  {} - {}".format(i + 1, carte.nom))


    # Choix de la carte
    labyrinthe = None
    while labyrinthe is None:
        choix = input("Entrez un numéro de labyrinthe pour commencer à jouer : ")
	# Si le joueur n'a pas entré R, on s'attend à un nombre
        try: 
            choix = int(choix)
        except ValueError:
            print ("Choix invalide")
        else:
            if choix < 1 or choix > len(cartes):
                print ("Numero invalide")
                continue
            carte = cartes[choix - 1]
            labyrinthe = carte.labyrinthe

else:
	labyrinthe = recup_labyrinthe_sauvegarde()



 # Maintenant on affiche la carte à chaque tour
print("\n\n#################   Affichage du labyrinthe   ##################\n\n")
labyrinthe.afficher()

while not labyrinthe.gagnee:
    coup = input("> ")
    if coup == "":
        continue
    elif coup.lower() == "q":
        # On quitte la partie
        break
    elif coup[0].lower() in "nseo":
        lettre = coup[0].lower()
        if lettre == "e":
            direction = "est"
        elif lettre == "s":
            direction = "sud"
        elif lettre == "o":
            direction = "ouest"
        else: # On sait que c'est n
            direction = "nord"

        # On va essayer de convertir le déplacement
        coup = coup[1:]
        if coup == "":
            nombre = 1
        else:
            try:
                nombre = int(coup)
            except ValueError:
                print("Nombre invalide : {}".format(coup))
                continue
        # On déplace le robot et on sauvegarde la partie
        labyrinthe.deplacer_robot(direction, nombre)
        sauvegarder_labyrinthe(labyrinthe)
    else:
        print("\n\n#############   Coups autorisés   #############\n\n")
        print("  Q - Quitter la partie en cours")
        print("  E - Déplacer le robot vers l'est")
        print("  S - Déplacer le robot vers le sud")
        print("  O - Déplacer le robot vers l'ouest")
        print("  N - Déplacer le robot vers le nord")
        print("  Vous pouvez préciser un nombre après la direction")
        print("  Pour déplacer votre robot plus vite. Exemple n3")

if labyrinthe.gagnee:
    print("Félicitation ! Vous avez gagné !")
else:
    print("Votre partie a été sauvegardée.")
    sauvegarder_labyrinthe(labyrinthe)




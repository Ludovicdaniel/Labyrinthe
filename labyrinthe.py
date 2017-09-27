# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

import os
import pickle
from robot import Robot
from mur import Mur
from porte import Porte
from sortie import Sortie

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    limite_x = 20
    limite_y = 20

    # On définit le constructeur
    def __init__(self, robot, obstacles):
        self.robot = robot
        self.grille = {}
        self.grille[robot.x,robot.y] = robot # La clé du robot est son tuple correspondant à ses coordonnées x et y
        self.invisibles = []
        self.gagnee = False

        # Pour tous les obstacles
        for obstacle in obstacles:

            # Si l'obstacle est déjà dans la grille
            if(obstacle.x, obstacle.y) in self.grille:
                raise ValueError("Les coordonnées x={} y={} sont déjà utilisés dans cette grille".format(obstacle.x,obstacle.y))

            # Si un des coordonnées de l'obstacle est en dehors des limites
            if obstacle.x > self.limite_x or obstacle.y > self.limite_y:
                raise ValueError("L'obstacle {} a des coordonnées trop grandes".format(obstacle))

            self.grille[obstacle.x,obstacle.y] = obstacle

    ### Fin du constructeur ###

    def afficher(self):
        """ Cette méthode affiche le labyrinthe dans la console """

        y = 0
        chaine_grille = "" # La grille est une chaine vide au départ, mais qui sera remplie par les symboles des obstacles et du robot

        # Tant que la hauteur y de la grille est inférieur à la limite fixée
        while y < self.limite_y:
            x = 0 # On initialise x à 0
            # Tant la largeur x de la grille est inférieur à la limite fixée
            while x < self.limite_x:
                case = self.grille.get((x,y)) # On place la valeur de la clé(x,y) de la grille ( qui est un objet ) dans la variable case
                if case:
                    chaine_grille += case.symbole # On ajoute à la chaine grille le symbole de l'objet case
                else:
                    chaine_grille += " " # Si il n'y a pas d'objet dans la grille ayant comme clé le tuple (x,y), on ajoute un espace vide

            # On ajoute un saut de ligne et on incrémente y puisque qu'on passe à la prochaine ligne
            chaine_grille += "\n"
            y += 1

        # Une fois toute la grille parcourue, on affiche la grille
        print chaine_grille

    def actualiser_invisibles(self):
        """ Cette méthode actualise les obstacles invisibles.
        Si le robot passe sur un obstacle passable, l'obstacle est remplacé
        par un obstacle invisible """

        # Pour tous les obstacles dans la liste des invisibles
        for obstacle in list(self.invisibles):
            # Si l'obstacle n'est pas dans la grille, on l'ajoute dans la grille et on le retire des invisibles
            if (obstacle.x,obstacle.y) not in self.grille:
                self.grille[obstacle.x,obstacle.y] = obstacle
                self.invisibles.remove(obstacle)

    def deplacer_robot(self,direction,nombre):
        """ Cette méthode déplace le robot dans une direction en précisant le nombre de case.
        Si le robot se heurte à un obstacle infranchissable, il s'arrête """

        robot = self.robot
        coordonnees = [robot.x,robot.y] # On récupère les coordonnées du robot
        if direction == "nord":         # Si le robot va vers le haut, on décrémente le y de 1
            coords[1] -= 1

        elif direction == "est":
            coords[0] += 1

        elif direction == "sud":
            coords[1] += 1

        elif direction == "ouest":
            coords[0] -= 1

        else:
            raise ValueError("Direction inconnue")


        x,y = coords
        if x >= 0 and x < self.limite_x and y >= 0 and y < self.limit_y:
            # On essaye de déplacer le robot
            # On vérifie qu'il n'y a pas d'obstacle
            obstacle = self.grille.get((x,y)) # Renvoie l'objet de coordonnées x,y
            if obstacle is None or obstacle.peut_traverser:
                # Si y'a un obstacle, on le rajoute dans les invisibles
                if obstacle:
                    self.invisibles.append(obstacle)

                # On supprime l'ancienne position du robot
                del self.grille[robot.x,robot.y]

                # On place le robot aux nouvelles coordonnées
                self.grille[x,y] = robot
                robot.x = x
                robot.y = y
                
                # On actualise les invisibles
                self.actualiser_invisibles()

                # On affiche le labyrinthe
                self.afficher()

                # On appele la méthode arriver de l'obstacle, si il existe
                if obstacle:
                    self.arriver(self,robot)
        
        if not self.gagnee and nombre > 1:
            self.deplacer_robot(direction,nombre - 1)

    def creer_labyrinthe_depuis_chaine(chaine):
        """ Méthode pour créer un labyrinthe depuis une chaine de caractère 
        Elle retourne un objet de type Labyrinthe """


        # Définition des symboles
        symboles = {
                "o": Mur,
                "x": Robot,
                ".": Porte,
                "u": Sortie,
                }

        x = 0
        y = 0

        robot = None
        obstacles = []

        # Pour chaque lettre dans la chaine passé en paramètre
        for lettre in chaine:
            # Si la lettre est un retour à la ligne \n, on descend d'un coordonné y
            if lettre == "\n":
                x = 0
                y += 1
                continue

            elif:
                lettre == " ": # Si la lettre est un espace on ne fait rien même si exception
                    pass 

            elif: letter.lower() in symboles: # Si la lettre est dans la liste des symboles
                classe = symboles[lettre.lower()]
                objet = classe(x,y)
                if type(objet) is Robot: # Si le type de la classe est Robot
                    if robot: # Si l'objet robot existe déja
                        raise ValueError("Il ne peut y avoir qu'un robot")
                    robot = objet # Sinon on le crée
                else: # Si c'est pas un robot, c'est donc un obstacle
                    obstacles.append(objet) # On ajoute l'objet aux obstacles

            else:
                raise ValueError("Symbole inconnu")

            x += 1

        labyrinthe = Labyrinthe(robot,obstacles)
        return labyrinthe










            














            







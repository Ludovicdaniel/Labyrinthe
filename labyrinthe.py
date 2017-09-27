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

########### FIN DE LA CLASSE LABYRINTHE ##############

    
def creer_labyrinthe_depuis_chaine(chaine):
    """Crée un labyrinthe depuis une chaîne.
    Les symboles sont définis par correspondance ici.
    """
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
    #print "{}".format(repr(chaine))
    for lettre in chaine:
        if lettre == "\n":
            x = 0
            y += 1
            continue
        elif lettre == "\r":
            pass
        elif lettre == " ":
            pass
        elif lettre.lower() in symboles:
            classe = symboles[lettre.lower()] # On met dans la variable classe la valeur de l'item de clé lettre.lower()  
            objet = classe(x, y)
            
            if objet.nom == "robot":
                
                if robot:
                    raise ValueError("il ne peut y avoir qu'un robot")

                robot = objet
            else:
                obstacles.append(objet)
                
        else:
            raise ValueError("symbole inconnu aux coordonnées {}:{} ".format(x,y))

        x += 1

    labyrinthe = Labyrinthe(robot, obstacles)
    return labyrinthe

























            







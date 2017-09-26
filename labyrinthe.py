# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

import os
import pickle
from robot import Robot

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    limite_x = 20
    limite_y = 20

    # On définit le constructeur
    def __init__(self, robot, obstacles):
        self.robot = robot
        self.grille = {}
        self.grille[robot.x,robot.y] = robot
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





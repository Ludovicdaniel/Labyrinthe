# -*- coding:utf8 -*-

""" Fichier contenant la classe obstacle """

class Obstacle:

    """ Cette classe symbolise tous les obstacles.
    Les obstacles spécifiques tels que les murs et les portes
    seront hérités de celle-ci """

    # Définition des attributs de classe
    nom = "obstacle"
    peut_traverser = True
    symbole = ""

    # Constructeur passant en paramètre les coordonnées de l'obstacle
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<{} (x={}, y={})>".format(self.nom,self.x,self.y)

    def __str__(self):
        return "{} ({}.{})".format(self.nom,self.x,self.y)

    def arriver(self,labyrinthe,robot):
        """ Méthode appelée quand le robot arrive sur l'obstacle """

        pass # Ne rien faire si exception levée




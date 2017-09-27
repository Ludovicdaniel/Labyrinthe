# -*- coding:utf8 -*-

""" Ce module contient la classe robot """

class Robot:
    """ Classe représentant un robot """
    symbole = "X"
    nom = "robot"

    # Constructeur prennant en paramètre les coordonnées x et y du robot
    def __init__(self,x,y):
        self.x = x
        self.y = y

    # Méthode spéciale qui permet de représenter l'objet dans l'interpréteur python
    def __repr__(self):
        return "<Robot (x={} y={})".format(self.x,self.y)

    # Méthode qui permet d'afficher le Robot 
    def __str__(self):
        return "Robot ({}.{})".format(self.x,self.y)






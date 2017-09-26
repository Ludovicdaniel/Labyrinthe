# -*- coding:utf8 -*-

""" Fichier contenant la classe mur """

from obstacle import Obstacle

class Mur(Obstacle):
    """ Classe représentant un mur """

    peut_traverser = False
    nom = "mur"
    symbole = "O"



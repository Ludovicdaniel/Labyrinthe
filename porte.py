# -*- coding:utf8 -*-

""" Fichier contenant la classe Porte, une classe héritée de la classe Obstacle """

from obstacle import Obstacle

class Porte(Obstacle):

    """ Cette classe représente une porte dans le labyrinthe """

    peut_traverser = True
    nom = "porte"
    symbole = "."



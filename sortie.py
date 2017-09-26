# -*- coding:utf8 -*-

""" Fichier contenant la classe Sortie """

from obstacle import Obstacle

class Sortie(Obstacle):
    """ Classe représentant la sortie du labyrinthe """

    peut_traverser = True
    nom = "sortie"
    symbole = "U"

    def arriver(self,labyrinthe,robot):
        """ méthode appelée quand le robot arrive sur une sortie """

        labyrinthe.gagnee = True


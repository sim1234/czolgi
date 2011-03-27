#!/usr/bin/python
# coding: utf-8

import pygame, sys, os
from pygame.locals import * 

def pa(name):
    return sys.path[0]+"/"+name

sys.path.append(pa("sys"))
from button import *
from game import *


#execfile(pa("sys/fn.py"))
#execfile(pa("sys/ini.py"))
#execfile(pa("sys/map.py"))
#execfile(pa("sys/kula.py"))
#execfile(pa("sys/player.py"))
#execfile(pa("sys/button.py"))
#execfile(pa("sys/game.py"))

def main():
    gra=game(740,480,200,0,"Czolgi",1000)
    execfile(pa("sys/menuust.py"))
    gra.graj()

if __name__ == "__main__":
	main()

#print "CYA"
sys.exit(0)

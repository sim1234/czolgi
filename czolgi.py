# coding: utf-8

#print "Running..."

import pygame, sys, os, time, string
from pygame.locals import * 

#from fn import *
#from ini import *
#from map import *
#from kula import *
#from player import *
#from button import *
#from game import *

def pa(name):
    return sys.path[0]+"/"+name

execfile(pa("fn.py"))
execfile(pa("ini.py"))
execfile(pa("map.py"))
execfile(pa("kula.py"))
execfile(pa("player.py"))
execfile(pa("button.py"))
execfile(pa("game.py"))

def main():
    gra=game(740,480,200,0,"Czolgi",1000)
    execfile(pa("menuust.py"))
    gra.graj()

if __name__ == "__main__":
	main()

#print "CYA"
sys.exit(0)

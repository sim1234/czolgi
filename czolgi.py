# coding: utf-8

import pygame, sys, os, time, string
from pygame.locals import * 

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
    gra=game(740,480,200,0,"Czolgi",60)
    execfile(pa("menuust.py"))
    gra.graj()

if __name__ == "__main__":
	main()
	
sys.exit(0)


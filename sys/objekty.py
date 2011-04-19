# coding: utf-8

import pygame, sys, os
from pygame.locals import * 
from fn import *
from kula import *

class stojace_dzialko:
    def __init__(self, (px, py, w, h), color, (x,y,vx,vy), freq, klifetime=-1):
        self.px=int(px)
        self.py=int(py)
        self.w=int(w)
        self.h=int(h)
        self.color=color
        self.nx=x
        self.ny=y
        self.nvx=vx
        self.nvy=vy
        self.freq=int(freq)
        self.ti=1
        self.klt=klifetime
   
    def rysuj(self, mapa_dane):
        pygame.draw.rect(mapa_dane.bm, self.color, (self.px, self.py, self.w, self.h)) 
        
    def jezdz(self, dane):
        if self.ti%self.freq==0:
            k=kula(self.nx+self.px,self.ny+self.py,self.nvx,self.nvy, self.klt)
            dane.nab.append(k)
            dane.sounds["shot"].play()
        self.ti+=1

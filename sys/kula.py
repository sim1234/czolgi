# coding: utf-8

import pygame, sys, os
from pygame.locals import * 
from fn import *

class kula:
    def __init__(self, p_x, p_y, v_x, v_y):
        self.px=p_x
        self.py=p_y
        self.vx=v_x
        self.vy=v_y
    def jezdz(self, dane):
        self.px+=self.vx/4.0
        self.py+=self.vy/4.0
        if self.px<0 or self.px>dane.e_w or self.py<0 or self.py>dane.e_h: return 1
        t=0
        tlen=len(dane.gracze)
        while t<tlen:
            if self.px>=dane.gracze[t].pozx and self.px<=dane.gracze[t].pozx+dane.gracze[t].w and self.py>=dane.gracze[t].pozy and self.py<=dane.gracze[t].pozy+dane.gracze[t].h:
                dane.sounds["hit"].play()
                dane.gracze[t].hp-=1
                if(dane.gracze[t].hp<=0):
                    dane.gracze.pop(t)
                    t-=1
                    tlen-=1    
                return 1
            t+=1        
        if dane.map.zamien(dane, (int(self.px),int(self.py))):
            dane.map.zamien(dane,(int(self.px-1),int(self.py-1)))
            dane.map.zamien(dane,(int(self.px-1),int(self.py)))
            dane.map.zamien(dane,(int(self.px-1),int(self.py+1)))
            dane.map.zamien(dane,(int(self.px),int(self.py-1)))
            dane.map.zamien(dane,(int(self.px),int(self.py+1)))
            dane.map.zamien(dane,(int(self.px+1),int(self.py-1)))
            dane.map.zamien(dane,(int(self.px+1),int(self.py)))
            dane.map.zamien(dane,(int(self.px+1),int(self.py+1)))
            dane.sounds["destroy"].play()
            return 1
                
        pto=1
        if self.py>=1: g=dane.map.odbije(dane.map.bm.get_at((int(self.px), int(self.py-1))))
        else: g=0
        if self.px>=1: l=dane.map.odbije(dane.map.bm.get_at((int(self.px-1), int(self.py))))
        else: l=0
        if self.px<dane.map.w-1: p=dane.map.odbije(dane.map.bm.get_at((int(self.px+1), int(self.py))))
        else: p=0
        if self.py<=dane.map.h-1: d=dane.map.odbije(dane.map.bm.get_at((int(self.px), int(self.py+1))))
        else: d=0
        
        if (l and g) or (p and d):
            xt=self.vx
            self.vx=self.vy*-1
            self.vy=xt*-1
            pto=0
        if (g and p) or (d and l):
            xt=self.vx
            self.vx=self.vy
            self.vy=xt
            pto=0
        if pto and (l or p): self.vx*=-1
        if pto and (d or g): self.vy*=-1
        if g or l or p or d:
            dane.sounds["bounce"].play()
        
        return 0
        
    def rysuj(self, dane):
        pygame.draw.circle(dane.bufor, (0,0,0), (int(self.px), int(self.py)), 2, 0)

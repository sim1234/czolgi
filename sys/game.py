# coding: utf-8

import pygame, sys, os
from pygame.locals import * 
from fn import *
from ini import *
from map import *
from kula import *
from player import *
from button import *

class game:
    def __init__(self, a_w, a_h, a_wd, a_hd, caption, maxfps):
        pygame.init() 
        self.tryb=1
        self.a_w=a_w
        self.a_h=a_h
        self.e_w=a_w-a_wd
        self.e_h=a_h-a_hd
        self.fps=maxfps
        pygame.display.set_icon(pygame.image.load(pa("data/czolgi.png")))
        self.window = pygame.display.set_mode((a_w, a_h)) 
        pygame.display.set_caption(caption) 
        self.screen = pygame.display.get_surface() 
        if not pygame.font: print 'Warning, fonts disabled'
        if not pygame.mixer: print 'Warning, sound disabled'

        self.bufor=pygame.Surface((a_w,a_h))
        self.gracze=[]
        self.nab=[]
        self.map=mapa(pa("maps/mapa1"),0)
        self.lmousekeys=self.mousekeys=pygame.mouse.get_pressed()
        self.lboardkeys=self.boardkeys=pygame.key.get_pressed()
        self.lec=self.jezd=self.wait=0
        self.start=self.search=1
        self.napis=""
        self.kbufor=pygame.Surface((a_w,a_h))
        self.fpsclock=pygame.time.Clock()
        self.ini=inifile()
        self.ini.open(pa("data/czolgi.ini"))
        self.sounds=load_sounds(("hit", "shot", "destroy", "bounce"))
        pygame.time.set_timer(27, 50)
         
    
    def _wait(self, czas, napiss):
        self.wait=int(czas*1000)+pygame.time.get_ticks()
        font = pygame.font.Font(pygame.font.match_font('doesNotExist,Arial'), 20)
        text = font.render(napiss, True, (0,0,0), (220,220,255))
        textRect = text.get_rect()
        textRect.x = self.a_w/2-textRect.width/2
        textRect.y = self.a_h/2-textRect.height/2
        self.bufor.blit(text, textRect)
        self.kbufor.blit(self.bufor,(0,0))
        self.napis=str(napiss)
        self.tryb=3
    
    
    def endframe(self):
        if self.boardkeys[K_ESCAPE]:
            self.tryb=1

        events=pygame.event.get()
        for event in events: 
            if event.type == QUIT: self.tryb=0
        
            if event.type == 27:
                self.lmousekeys=self.mousekeys
                self.lboardkeys=self.boardkeys
                self.mousekeys=pygame.mouse.get_pressed()
                self.boardkeys=pygame.key.get_pressed()
                
        if self.boardkeys[K_TAB]:
            print_text(self.a_w-18, self.a_h-10, str(int(self.fpsclock.get_fps())), self.bufor)
        
        self.screen.blit(self.bufor,(0,0))
        pygame.display.flip() 
        self.fpsclock.tick(self.fps)
    
    
    def main_menu(self):
        self.me.rysuj(self)
        if self.me[0]:
            self.tryb=4
            self.search=1
            pygame.time.wait(100)
        if self.me[1]:
            self.tryb=2
            pygame.time.wait(100)
        if self.me[2]:
            self.tryb=0
        pygame.time.wait(1)
        
        
    def ustawienia(self):
        self.mu.rysuj(self)
        self.mu1.rysuj(self)
        self.mu2.rysuj(self)
        self.mu3.rysuj(self)
        self.mu4.rysuj(self)
        self.butt1.rysuj(self)
        self.butt2.rysuj(self)
        t=1
        while t<7:
            if self.mu1.but[t].cl: self.mu1.but[t].ust(get_key())
            if self.mu2.but[t].cl: self.mu2.but[t].ust(get_key())
            if self.mu3.but[t].cl: self.mu3.but[t].ust(get_key())
            if self.mu4.but[t].cl: self.mu4.but[t].ust(get_key())
            t+=1
        if self.butt1.cl: self.tryb=1
        if self.butt2.cl: 
            t=1
            while t<=4:
                self.ini.set("gracz"+str(t), "up", str(eval("self.mu"+str(t)+".but[1].m_k")))
                self.ini.set("gracz"+str(t), "down", str(eval("self.mu"+str(t)+".but[2].m_k")))
                self.ini.set("gracz"+str(t), "left", str(eval("self.mu"+str(t)+".but[3].m_k")))
                self.ini.set("gracz"+str(t), "right", str(eval("self.mu"+str(t)+".but[4].m_k")))
                self.ini.set("gracz"+str(t), "shoot", str(eval("self.mu"+str(t)+".but[5].m_k")))
                self.ini.set("gracz"+str(t), "speed", str(eval("self.mu"+str(t)+".but[6].m_k")))
                t+=1
            
            self.tryb=1
        pygame.time.wait(1)
        
        
    def czekaj(self):
        if pygame.time.get_ticks()<=self.wait:
            self.bufor.blit(self.kbufor,(0,0))
            pygame.time.wait(1)
        else:
            self.tryb=1
    
    
    def ask_map(self):#lista map
        if self.search:
            self.search=0
            self.maps=menu((self.a_w/2-100, 50, 200, 30), 5, (200,200,200),(220,220,220),(0,0,0), 15, 1)
            for f in os.listdir(pa("maps")):
                if os.path.isdir(pa("maps/"+str(f))):
                    self.maps.push_back(str(f))
        self.maps.rysuj(self)
        for t in range(0,len(self.maps.but)):
            if self.maps.but[t].cl:
                self.start=1
                self.tryb=5
                self.map=mapa(pa("maps/"+str(self.maps.but[t].text)), 0)
        pygame.time.wait(1)
        
    def czolgi(self):#właściwa gra
        if self.start:
            self.map.reload()
            self.nab=[]
            self.gracze=[]
            for x in range(0,len(self.map.gracze)):
                pl=player(self.map.gracze[x][0],
                self.map.gracze[x][1],  20,  20,
                self.ini.read("gracz"+str(x+1),"up"),
                self.ini.read("gracz"+str(x+1),"down"),
                self.ini.read("gracz"+str(x+1),"left"),
                self.ini.read("gracz"+str(x+1),"right"),
                self.ini.read("gracz"+str(x+1),"speed"),
                self.ini.read("gracz"+str(x+1),"shoot"),
                self.ini.read("gracz"+str(x+1),"color"), 
                self.ini.read("gracz"+str(x+1),"ppx"),
                self.ini.read("gracz"+str(x+1),"ppy"),  x+1)
                self.gracze.append(pl)
            self.lec=self.jezd=pygame.time.get_ticks()
            self.start=0
        
        self.map.rysuj()
        self.bufor.blit(self.map.bm,(0,0))
        pygame.draw.rect(self.bufor, (200,200,200),(self.e_w,0,self.a_w,self.a_h))
                
        atim=pygame.time.get_ticks()
        while self.lec<atim or self.jezd<atim:#pętla timerów
            if self.lec<atim:#timer do kul
                t=0
                tlen=len(self.nab)
                while t<tlen:
                        if self.nab[t].jezdz(self):
                            self.nab.pop(t)
                            t-=1
                            tlen-=1
                        t+=1
                self.lec+=4            

            if self.jezd<atim:#timer do jazdy
                t=0
                tlen=len(self.gracze)
                while t<tlen:
                    self.gracze[t].jezdz(self)
                    t+=1
                self.jezd+=7
            atim=pygame.time.get_ticks()

        t=0
        tlen=len(self.gracze)
        while t<tlen:
            self.gracze[t].rysuj(self)
            t+=1
        t=0
        tlen=len(self.nab)
        while t<tlen:
            self.nab[t].rysuj(self)
            t+=1
 
        if len(self.gracze)<=1:
            self.start=1
            self._wait(2, "Wygral gracz "+str(self.gracze[0].name))
        
        
    def graj(self):
        while self.tryb:
            self.bufor.fill(pygame.Color(255,255,255))
            if self.tryb==1:
                self.main_menu()
            elif self.tryb==2:
                self.ustawienia()
            elif self.tryb==3:
                self.czekaj()
            elif self.tryb==4:
                self.ask_map()
            elif self.tryb==5:
                self.czolgi()
            
            self.endframe()
        
        
        

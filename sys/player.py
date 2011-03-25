# coding: utf-8

class player:
  
    def __init__(self, p_x, p_y, width, height, k_w, k_s, k_a, k_d, k_sp, k_sh, colr, pp_x, pp_y, p_name):
        self.wytrzymalosc=800
        self.kier=1
        self.v=0.5
        self.loaded=0
        self.hp=4
        self.space_c=0
        self.l_tmp=50
        self.pozx=float(p_x)
        self.pozy=float(p_y)
        self.k_up=int(k_w)
        self.k_down=int(k_s)
        self.k_left=int(k_a)
        self.k_right=int(k_d)
        self.k_speed=int(k_sp)
        self.k_shoot=int(k_sh)
        #colr=colr[1:-1]
        #print colr
        #colr=colr.split(",")
        #colr=str(colr)[1:-1].split(", ")
        #self.color=(int(colr[0]), int(colr[1]), int(colr[2]))
        self.color=str_to_col(colr)
        self.pa_x=int(pp_x)
        self.pa_y=int(pp_y)
        self.w=int(width)
        self.h=int(height)
        self.name=str(p_name)
        
    def rysuj(self, dane):
        pygame.draw.rect(dane.bufor, self.color,(int(self.pozx), int(self.pozy), int(self.w), int(self.h)))
        if self.kier==1: pygame.draw.rect(dane.bufor, self.color,(int(self.pozx+self.w/2-2), int(self.pozy-4),4,4)) 
        if self.kier==3: pygame.draw.rect(dane.bufor, self.color,(int(self.pozx+self.w), int(self.pozy+self.h/2-2),4,4))
        if self.kier==5: pygame.draw.rect(dane.bufor, self.color,(int(self.pozx+self.w/2-2), int(self.pozy+self.h),4,4))
        if self.kier==7: pygame.draw.rect(dane.bufor, self.color,(int(self.pozx-4), int(self.pozy+self.h/2-2),4,4))
        print_text(dane.e_w+self.pa_x, self.pa_y, "Gracz "+self.name, dane.bufor)
        if not self.loaded: print_text(dane.e_w+self.pa_x, self.pa_y+120, "Ladowanie...", dane.bufor)
        pygame.draw.rect(dane.bufor, (0,0,0),(dane.e_w+self.pa_x,self.pa_y+12,22,104))
        pygame.draw.rect(dane.bufor, (220,255,220),(dane.e_w+self.pa_x+2,self.pa_y+14,18,100))
        pygame.draw.rect(dane.bufor, (127,255,127),(dane.e_w+self.pa_x+2,self.pa_y+114-(self.wytrzymalosc/10),18,self.wytrzymalosc/10))
        pygame.draw.rect(dane.bufor, (0,0,0),(dane.e_w+self.pa_x+30,self.pa_y+12,22,104))
        pygame.draw.rect(dane.bufor, (255,220,220),(dane.e_w+self.pa_x+32,self.pa_y+14,18,100))
        pygame.draw.rect(dane.bufor, (255,127,127),(dane.e_w+self.pa_x+32,self.pa_y+114-(self.hp*25),18,self.hp*25))
        
    def jezdz(self, dane):
        self.v=0.5
        if self.wytrzymalosc>2 and dane.boardkeys[self.k_speed]:
            self.v=1
            self.wytrzymalosc-=3
        if self.v<=0.5 and self.wytrzymalosc<1000:
            self.wytrzymalosc+=2
        ml=1
        mr=1
        md=1
        mu=1
        x=0
        xlen=len(dane.gracze)
        while x<xlen: #miedzy sobą
            if dane.gracze[x].name!=self.name:
                if int(dane.gracze[x].pozx+dane.gracze[x].w) == int(self.pozx) and dane.gracze[x].pozy+dane.gracze[x].h > self.pozy and dane.gracze[x].pozy < self.pozy+self.h: ml=0
                if int(dane.gracze[x].pozx) == int(self.pozx+self.w) and dane.gracze[x].pozy+dane.gracze[x].h > self.pozy and dane.gracze[x].pozy < self.pozy+self.h: mr=0
                if int(dane.gracze[x].pozy+dane.gracze[x].h) == int(self.pozy) and dane.gracze[x].pozx+dane.gracze[x].w > self.pozx and dane.gracze[x].pozx < self.pozx+self.w: mu=0
                if int(dane.gracze[x].pozy) == int(self.pozy+self.h) and dane.gracze[x].pozx+dane.gracze[x].w > self.pozx and dane.gracze[x].pozx < self.pozx+self.w: md=0
            x+=1
        
        x=0
        while x<self.h: # o scianki
            if dane.boardkeys[self.k_left] and self.pozx>=1 and self.pozy<dane.map.h-x:
                if dane.map.dobije(dane.map.bm.get_at((int(self.pozx-1), int(self.pozy+x)))): ml=0
            if dane.boardkeys[self.k_right] and self.pozx<dane.map.w-self.w and self.pozy<dane.map.h-x:
                if dane.map.dobije(dane.map.bm.get_at((int(self.pozx+self.w), int(self.pozy+x)))): mr=0
            x+=1
        x=0;
        while x<self.w:
            if dane.boardkeys[self.k_up] and self.pozx<dane.map.w-x and self.pozy>=1:
                if dane.map.dobije(dane.map.bm.get_at((int(self.pozx+x), int(self.pozy-1)))): mu=0
            if dane.boardkeys[self.k_down] and self.pozx<dane.map.w-x and self.pozy<dane.map.h-self.h:
                if dane.map.dobije(dane.map.bm.get_at((int(self.pozx+x), int(self.pozy+self.h)))): md=0
            x+=1

        if self.pozx <= 0: ml=0
        if self.pozx+1 >= dane.e_w-self.w: mr=0
        if self.pozy <= 0: mu=0
        if self.pozy >= dane.e_h-self.h: md=0
      
        if dane.boardkeys[self.k_left] and not dane.boardkeys[self.k_up] and not dane.boardkeys[self.k_down]:# ruch pion / poziom
            if ml: self.pozx-=self.v
            self.kier=7
        if dane.boardkeys[self.k_right] and not dane.boardkeys[self.k_up] and not dane.boardkeys[self.k_down]: 
            if mr: self.pozx+=self.v
            self.kier=3
        if dane.boardkeys[self.k_up] and not dane.boardkeys[self.k_left] and not dane.boardkeys[self.k_right]:
            if mu:  self.pozy-=self.v
            self.kier=1
        if dane.boardkeys[self.k_down] and not dane.boardkeys[self.k_left] and not dane.boardkeys[self.k_right]: 
            if md: self.pozy+=self.v 
            self.kier=5
      
        if dane.boardkeys[self.k_left] and dane.boardkeys[self.k_up]:#ruch skos
            if ml: self.pozx-=0.7*self.v
            if mu: self.pozy-=0.7*self.v 
            self.kier=8
        if dane.boardkeys[self.k_left] and dane.boardkeys[self.k_down]:
            if ml: self.pozx-=0.7*self.v
            if md: self.pozy+=0.7*self.v 
            self.kier=6
        if dane.boardkeys[self.k_right] and dane.boardkeys[self.k_up]:
            if mr: self.pozx+=0.7*self.v 
            if mu: self.pozy-=0.7*self.v 
            self.kier=2
        if dane.boardkeys[self.k_right] and dane.boardkeys[self.k_down]:
            if mr: self.pozx+=0.7*self.v 
            if md: self.pozy+=0.7*self.v 
            self.kier=4
      
        if self.pozx < 0: self.pozx=0
        if self.pozx > dane.e_w-self.w: self.pozx=dane.e_w-self.w
        if self.pozy < 0: self.pozy=0
        if self.pozy > dane.e_h-self.h: self.pozy=dane.e_h-self.h
        
        if dane.boardkeys[self.k_shoot] and self.loaded:
            #8 1 2
            #7 - 3
            #6 5 4
            done=0
            if self.kier==1 and self.pozx<dane.map.w-self.w/2 and self.pozy>=1:
                if not dane.map.odbije(dane.map.bm.get_at((int(self.pozx+self.w/2),int(self.pozy-1)))): t=kula(self.pozx+self.w/2,self.pozy-1,0,-2-self.v); done=1
            if self.kier==3 and self.pozx<dane.map.w-self.w and self.pozy<dane.map.h-self.h/2:
                if not dane.map.odbije(dane.map.bm.get_at((int(self.pozx+self.w),int(self.pozy+self.h/2)))): t=kula(self.pozx+self.w+1,self.pozy+self.h/2,2+self.v,0); done=1
            if self.kier==5 and self.pozx<dane.map.w-self.w/2 and self.pozy<dane.map.h-self.h: 
                if not dane.map.odbije(dane.map.bm.get_at((int(self.pozx+self.w/2),int(self.pozy+self.h)))): t=kula(self.pozx+self.w/2,self.pozy+self.h+1,0,2+self.v); done=1
            if self.kier==7 and self.pozx>=1 and self.pozy<dane.map.h-self.h/2:
                if not dane.map.odbije(dane.map.bm.get_at((int(self.pozx-1),int(self.pozy+self.h/2)))): t=kula(self.pozx-1,self.pozy+self.h/2,-2-self.v,0); done=1
            if self.kier==2 and self.pozx<dane.map.w-self.w-1 and self.pozy>=1:
                if not dane.map.odbije(dane.map.bm.get_at((int(self.pozx+self.w+1),int(self.pozy-1)))): t=kula(self.pozx+self.w+1,self.pozy-1,2+self.v,-2-self.v); done=1
            if self.kier==4 and self.pozx<dane.map.w-self.w-1 and self.pozy<dane.map.h-self.h-1:
                if not dane.map.odbije(dane.map.bm.get_at((int(self.pozx+self.w+1),int(self.pozy+self.h+1)))): t=kula(self.pozx+self.w+1,self.pozy+self.h+1,2+self.v,2+self.v); done=1
            if self.kier==6 and self.pozx>=1 and self.pozy<dane.map.h-self.h-1:
                if not dane.map.odbije(dane.map.bm.get_at((int(self.pozx-1),int(self.pozy+self.h+1)))): t=kula(self.pozx-1,self.pozy+self.h+1,-2-self.v,2+self.v); done=1
            if self.kier==8 and self.pozx>=1 and self.pozy>=1:
                if not dane.map.odbije(dane.map.bm.get_at((int(self.pozx-1),int(self.pozy-1)))): t=kula(self.pozx-1,self.pozy-1,-2-self.v,-2-self.v); done=1
            if done:
                dane.sounds["shot"].play()
                dane.nab.append(t)
                self.loaded=0
                self.l_tmp=50
        if self.l_tmp: self.l_tmp-=1
        else: self.loaded=1
        
        

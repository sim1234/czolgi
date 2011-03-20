class kula:
    def __init__(self, p_x, p_y, v_x, v_y):
        self.px=p_x
        self.py=p_y
        self.vx=v_x
        self.vy=v_y
    def jezdz(self, dane):
        self.px+=self.vx/4.0
        self.py+=self.vy/4.0
        if self.px<=1 or self.px>=dane.e_w-1 or self.py<=1 or self.py>=dane.e_h-1: return 1
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
        odbtmp=[0,
        0,
        dane.map.odbije(dane.map.bm.get_at((int(self.px), int(self.py-1)))),
        0,
        dane.map.odbije(dane.map.bm.get_at((int(self.px-1), int(self.py)))),
        0,
        dane.map.odbije(dane.map.bm.get_at((int(self.px+1), int(self.py)))),
        0,
        dane.map.odbije(dane.map.bm.get_at((int(self.px), int(self.py+1)))),
        0] 

        if (odbtmp[4] and odbtmp[2]) or (odbtmp[6] and odbtmp[8]):
            xt=self.vx
            self.vx=self.vy*-1
            self.vy=xt*-1
            pto=0
        if (odbtmp[2] and odbtmp[6]) or (odbtmp[8] and odbtmp[4]):
            xt=self.vx
            self.vx=self.vy
            self.vy=xt
            pto=0
        if pto and (odbtmp[4] or odbtmp[6]): self.vx*=-1
        if pto and (odbtmp[8] or odbtmp[2]): self.vy*=-1
        if odbtmp[4] or odbtmp[6] or odbtmp[8] or odbtmp[2]:
            dane.sounds["bounce"].play()
        
        return 0
        
    def rysuj(self, dane):
        global bufor
        pygame.draw.circle(dane.bufor, (0,0,0), (int(self.px), int(self.py)), 2, 0)

# coding: utf-8

class button :
    def __init__(self, (pxt, pyt, wt, ht), cl1t, cl2t, tclt, textt, size=10, rk=0):
        self.px=pxt
        self.py=pyt
        self.w=wt
        self.h=ht
        self.cl1=cl1t
        self.cl2=cl2t
        self.tcl=tclt
        self.text=str(textt)
        self.onm=self.cl=0
        self.m_k=rk
        self.size=size
        self.c1=self.c2=pygame.Surface((self.w, self.h))
        self.render()
    
    def render(self):
        font = pygame.font.Font(pygame.font.match_font('doesNotExist,Arial'), self.size)
        text = font.render(self.text, True, self.tcl, self.cl1)
        text2 = font.render(self.text, True, self.tcl, self.cl2)
        textRect = text.get_rect()
        textRect.x = self.w/2-textRect.width/2
        textRect.y = self.h/2-textRect.height/2
        tmp=pygame.Surface((self.w, self.h))
        tmp2=pygame.Surface((self.w, self.h))
        tmp.fill(self.cl1)
        tmp2.fill(self.cl2)
        tmp.blit(text, textRect)
        tmp2.blit(text2, textRect)
        pygame.draw.rect(tmp, (0,0,0), (0, 0, self.w-1, self.h-1), 2)
        pygame.draw.rect(tmp2, (0,0,0), (0, 0, self.w-1, self.h-1), 2)
        self.c1=tmp
        self.c2=tmp2
      
    def rysuj(self, dane):
        p=pygame.mouse.get_pos()
        self.cl=0
        r=0
        if self.onm or (p[0]>=self.px and p[0]<=self.px+self.w and p[1]>=self.py and p[1]<=self.py+self.h):
            if not self.onm: r=1
            dane.bufor.blit(self.c2,(self.px, self.py, self.w, self.h))
        else: dane.bufor.blit(self.c1,(self.px, self.py, self.w, self.h))
        if (self.onm and dane.boardkeys[K_RETURN]) or (p[0]>=self.px and p[0]<=self.px+self.w and p[1]>=self.py and p[1]<=self.py+self.h and dane.mousekeys[0] and not dane.lmousekeys[0]):
            self.onm=0
            self.cl=1
        return r
      
    def ust(self, rk):
        self.m_k=int(rk)
        self.text=pygame.key.name(int(rk))
        self.render()


class menu:
    def __init__(self, (pxt, pyt, wt, ht), ot, cl1t, cl2t, tclt, size, strzalki=0):
        self.px=pxt
        self.py=pyt
        self.w=wt
        self.h=ht
        self.cl1=cl1t
        self.cl2=cl2t
        self.tcl=tclt
        self.o=ot
        self.pos=0
        self.kt=pygame.key.get_pressed()
        self.str=strzalki
        self.but=[]
        self.size=size
      
    def __getitem__(self, key):
        return self.but[key].cl  
    
    def push_back(self, txt, mk=0):
        t=button((self.px, self.py+len(self.but)*(self.h+self.o), self.w, self.h), self.cl1, self.cl2, self.tcl, txt, self.size, mk)
        self.but.append(t)
        self.but[-1]=button((self.px, self.py+len(self.but)*(self.h+self.o), self.w, self.h), self.cl1, self.cl2, self.tcl, txt, self.size, mk)
        self.but[-1].render()
      
    def rysuj(self, dane):
        x=0
        xlen=len(self.but)
        while x<xlen:
            self.but[x].cl=0
            self.but[x].onm=0
            if self.str:
                if x==self.pos: self.but[x].onm=1
                if x==self.pos and dane.boardkeys[K_RETURN]: self.but[x].cl=1
            if self.but[x].rysuj(dane): self.pos=-2
            x+=1
        if dane.boardkeys[K_DOWN] and not self.kt[K_DOWN]:
            if self.pos==-2: self.pos=-1
            self.pos+=1
          
        if dane.boardkeys[K_UP] and not self.kt[K_UP]: self.pos-=1
        if self.pos<-2: self.pos=len(self.but)-1
        if self.pos==-1: self.pos=len(self.but)-1
        if self.pos==len(self.but): self.pos=0
        self.kt=dane.boardkeys
        

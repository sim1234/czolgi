# coding: utf-8

class mapa:
    def __init__(self, name, serio=1):
        self.name=name
        if serio:
            self.bm=load_image(self.name+"/mapa.bmp")
            self.rozw=(0,0,0)
            self.odb=(0,0,255)
            t=self.bm.get_rect()
            self.w=t.w
            self.h=t.h
    
    def reload(self):
        self.__init__(self.name)
        
    def dobije(self, color):
        r=0
        if color==self.rozw: r=1
        if color==self.odb: r=1
        return r
        
    def zniszczy(self, color):
        r=0
        if color==self.rozw: r=1
        return r
        
    def odbije(self, color):
        r=0
        if color==self.odb: r=1
        return r
        
    def zamien(self, dane, (px, py)):
        if(px<0 or py<0 or px>=self.w or py>=self.h): return 0
        c=self.bm.get_at((px,py))
        if self.zniszczy(c):
            c[0]+=191
            if(c[0]>255): c[0]=255
            c[1]+=191
            if(c[1]>255): c[1]=255
            c[2]+=191
            if(c[1]>255): c[1]=255
            self.bm.set_at((px,py), c)
            return 1
        return 0

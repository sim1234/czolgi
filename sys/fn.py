# coding: utf-8

def load_image(name, colorkey=None):
    try:
        image = pygame.image.load(name)
    except pygame.error, message:
        print "Cannot load image:", name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image#, image.get_rect()

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    try:
        sound = pygame.mixer.Sound(name)
    except pygame.error, message:
        print "Cannot load sound:", wav
        raise SystemExit, message
    return sound

def load_sounds(lista, roz=".wav"):
    r={}
    tlen=len(lista)
    t=0
    while t<tlen:
        r.update({lista[t]:pygame.mixer.Sound(pa("data/"+lista[t]+roz))})
        t+=1
    return r

def print_text(px, py, text, bit, size=10, color=(0,0,0), bgcolor=(200,200,200)):
    font = pygame.font.Font(pygame.font.match_font('doesNotExist,Arial'), size)
    text = font.render(text, True, color, bgcolor)
    textRect = text.get_rect()
    textRect.x = px
    textRect.y = py
    bit.blit(text, textRect)
    
def mbutton(dane, (px, py, w, h), cl1, cl2, tcl, text, bit, size=10, onm=0):
    font = pygame.font.Font(pygame.font.match_font('doesNotExist,Arial'), size)
    p=pygame.mouse.get_pos()
    if onm or (p[0]>px and p[0]<px+w and p[1]>py and p[1]<py+h) : bgcolor=cl1; r=1
    else: bgcolor=cl2; r=0
    text = font.render(text, True, tcl, bgcolor)
    textRect = text.get_rect()
    textRect.x = px+w/2-textRect.width/2
    textRect.y = py+h/2-textRect.height/2
    pygame.draw.rect(bit, (0,0,0), (px,py,w,h),0)
    pygame.draw.rect(bit, bgcolor, (px+2,py+2,w-4,h-4))
    bit.blit(text, textRect)
    #print mousekeys, pygame.mouse.get_pressed()
    return r and dane.boardkeys[0]#==0 and mousekeys[0]
    
def wysczek(dane, czas, napiss):
    dane.wait=int(czas*10)+time.time()*10
    font = pygame.font.Font(pygame.font.match_font('doesNotExist,Arial'), 20)
    text = font.render(napiss, True, (0,0,0), (220,220,255))
    textRect = text.get_rect()
    textRect.x = dane.a_w/2-textRect.width/2
    textRect.y = dane.a_h/2-textRect.height/2
    dane.bufor.blit(text, textRect)
    dane.kbufor.blit(bufor,(0,0))
    dane.napis=str(napiss)
    dane.tryb=3

def get_key():
    while 1:
        pygame.event.pump()
        key=pygame.key.get_pressed()
        t=0
        tlen=len(key)
        while t<tlen:
            if key[t] and t!=K_NUMLOCK and t!=K_SCROLLOCK and t!=K_CAPSLOCK : return t
            t+=1
        pygame.time.wait(1)
        
def str_to_col(col_str):
    color=str(col_str)[1:-1].split(", ")
    color=(int(color[0]), int(color[1]), int(color[2]))
    return color


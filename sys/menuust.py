# coding: utf-8

gra.mu=menu((20, 20, 100, 30), 5, (220,220,220),(220,220,220),(0,0,0), 13, 0)
gra.mu.push_back("Gracz")
gra.mu.push_back("W gore")
gra.mu.push_back("W dol")
gra.mu.push_back("W lewo")
gra.mu.push_back("W prawo")
gra.mu.push_back("Strzal")
gra.mu.push_back("Nitro")

gra.mu1=menu((125, 20, 100, 30), 5, (200,200,200),(220,220,220),(0,0,0), 13, 0)
gra.mu1.push_back("Gracz1")
gra.mu1.but[0].cl1=(220,220,220)
gra.mu1.but[0].render()
gra.mu1.push_back("")
gra.mu1.but[1].ust(gra.ini.read("gracz1", "up"))
gra.mu1.push_back("")
gra.mu1.but[2].ust(gra.ini.read("gracz1", "down"))
gra.mu1.push_back("")
gra.mu1.but[3].ust(gra.ini.read("gracz1", "left"))
gra.mu1.push_back("")
gra.mu1.but[4].ust(gra.ini.read("gracz1", "right"))
gra.mu1.push_back("")
gra.mu1.but[5].ust(gra.ini.read("gracz1", "shoot"))
gra.mu1.push_back("")
gra.mu1.but[6].ust(gra.ini.read("gracz1", "speed"))

gra.mu2=menu((230, 20, 100, 30), 5, (200,200,200),(220,220,220),(0,0,0), 13, 0)
gra.mu2.push_back("Gracz2")
gra.mu2.but[0].cl1=(220,220,220)
gra.mu2.but[0].render()
gra.mu2.push_back("")
gra.mu2.but[1].ust(gra.ini.read("gracz2", "up"))
gra.mu2.push_back("")
gra.mu2.but[2].ust(gra.ini.read("gracz2", "down"))
gra.mu2.push_back("")
gra.mu2.but[3].ust(gra.ini.read("gracz2", "left"))
gra.mu2.push_back("")
gra.mu2.but[4].ust(gra.ini.read("gracz2", "right"))
gra.mu2.push_back("")
gra.mu2.but[5].ust(gra.ini.read("gracz2", "shoot"))
gra.mu2.push_back("")
gra.mu2.but[6].ust(gra.ini.read("gracz2", "speed"))

gra.mu3=menu((335, 20, 100, 30), 5, (200,200,200),(220,220,220),(0,0,0), 13, 0)
gra.mu3.push_back("Gracz3")
gra.mu3.but[0].cl1=(220,220,220)
gra.mu3.but[0].render()
gra.mu3.push_back("")
gra.mu3.but[1].ust(gra.ini.read("gracz3", "up"))
gra.mu3.push_back("")
gra.mu3.but[2].ust(gra.ini.read("gracz3", "down"))
gra.mu3.push_back("")
gra.mu3.but[3].ust(gra.ini.read("gracz3", "left"))
gra.mu3.push_back("")
gra.mu3.but[4].ust(gra.ini.read("gracz3", "right"))
gra.mu3.push_back("")
gra.mu3.but[5].ust(gra.ini.read("gracz3", "shoot"))
gra.mu3.push_back("")
gra.mu3.but[6].ust(gra.ini.read("gracz3", "speed"))

gra.mu4=menu((440, 20, 100, 30), 5, (200,200,200),(220,220,220),(0,0,0), 13, 0)
gra.mu4.push_back("Gracz4")
gra.mu4.but[0].cl1=(220,220,220)
gra.mu4.but[0].render()
gra.mu4.push_back("")
gra.mu4.but[1].ust(gra.ini.read("gracz4", "up"))
gra.mu4.push_back("")
gra.mu4.but[2].ust(gra.ini.read("gracz4", "down"))
gra.mu4.push_back("")
gra.mu4.but[3].ust(gra.ini.read("gracz4", "left"))
gra.mu4.push_back("")
gra.mu4.but[4].ust(gra.ini.read("gracz4", "right"))
gra.mu4.push_back("")
gra.mu4.but[5].ust(gra.ini.read("gracz4", "shoot"))
gra.mu4.push_back("")
gra.mu4.but[6].ust(gra.ini.read("gracz4", "speed"))

gra.butt1=button((125, gra.a_h-50, 100, 30), (200,200,200),(220,220,220),(0,0,0), "Wroc", 15)
gra.butt2=button((230, gra.a_h-50, 100, 30), (200,200,200),(220,220,220),(0,0,0), "Zapisz", 15)

gra.me=menu((gra.a_w/2-100, gra.a_h/2-100, 200, 30), 5, (200,200,200),(220,220,220),(0,0,0), 15, 1)
gra.me.push_back("Start")
gra.me.push_back("Ustawienia")
gra.me.push_back("Wyjscie")

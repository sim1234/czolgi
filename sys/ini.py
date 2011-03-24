# coding: utf-8

class inifile:      
    def open(self, name):
        self.name=name
        f = open(self.name, "rb")  
        self.tresc="\n" + f.read() + "\n"
        f.close()
        return self.tresc
      
    def save(self):
        f = open(self.name, 'w')
        f.write(self.tresc[1:-1])
        f.close() 
        return self.tresc
      
    def read(self, section, variable):
        p1=self.tresc.find("\n[" + section + "]\n")
        if p1==-1 : return "" 
        tmp = p1 + len("\n[" + section + "]\n") - 1
        tmp2 = self.tresc.find("\n[", tmp) + 1
        se = self.tresc[tmp: tmp2]
        p2=se.find("\n" + variable + "=")
        if p2==-1: return ""
        tmp3 = p2 + len("\n" + variable + "=")
        tmp4 = se.find("\n", tmp3)
        return se[tmp3: tmp4]
      
    def set(self, section, variable, value):  
        p1=self.tresc.find("\n[" + section + "]\n")
        if(p1==-1): return ""
        tmp = p1 + len(("\n[" + section + "]\n")) - 1
        tmp2 = self.tresc.find("\n[", tmp) + 1
        se = self.tresc[tmp:tmp2]
        tmp3=se.find("\n" + variable + "=")
        if(tmp3==-1):
            se2 = se + variable + "=" + value + "\n"
        else: 
            tmp4 = se.find("\n", tmp3 + 1)
            se2=se[:tmp3] + "\n" + variable + "=" + value + se[tmp4:]
          
        self.tresc=self.tresc[:tmp] + se2 + self.tresc[tmp2:]
        return self.save()
      
    def new_section(self, name):   
        if self.tresc.find("\n[" + name + "]\n") != -1: return ""
        self.tresc += "[" + name + "]\n"
        return self.save()
      
    def unset(self, section, variable):  
        p1=self.tresc.find("\n[" + section + "]\n")
        if p1==-1: return ""
        tmp = p1 + len("\n[" + section + "]\n") - 1
        tmp2 = self.tresc.find("\n[", tmp) + 1
        se = self.tresc[tmp:tmp2]
        tmp3=se.find("\n" + variable + "=")
        if tmp3==-1: return ""
        tmp4 = se.find("\n", tmp3 + 1)
        self.tresc=self.tresc[:tmp+tmp3] + self.tresc[tmp4+tmp:]
        return self.save()
      
    def unset_section(self, section):
        tmp=self.tresc.find("\n[" + section + "]\n")
        if tmp==-1: return ""
        tmp2 = self.tresc.find("\n[", tmp + len("\n[" + section + "]\n"))
        self.tresc=self.tresc[:tmp-1] + self.tresc[tmp2:]
        return self.save()



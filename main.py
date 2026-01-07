import pyxel

class App:
    def __init__(self):
        pyxel.init(128, 128, title="NDC 2023")
        self.x = 0
        self.y = 0
        self.circs = []
        pyxel.run(self.update, self.draw)
        
    def update(self):
        self.x = (self.x + 1) % pyxel.width
        self.y = (self.y + 1) % pyxel.width
    
    def mov(self):
        ...
    
    def new_circ(self):
        ...
    
    def draw(self):
        pyxel.cls(0)
        pyxel.circ(self.x, self.y, 8, 9)
        pyxel.rectb(0, 0, 128, 128, 13)
    
class Circle:
    def __init__(self,x,y,r,col,spd_x,spd_y,role,pv):
        self.x,self.y,self.r,self.col,self.spd_x,self.spd_y,self.role,self.pv = x,y,r,col,spd_x,spd_y,role,pv


App()

#"C:\Users\patrick.addison\AppData\Roaming\Python\Python311\Scripts\pyxel.exe"
#"C:\Users\patrick.addison\Downloads\projet_filtre\res.pyxres"
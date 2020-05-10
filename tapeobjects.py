from tapeconstants import *
from tapeutils import *

# module for the visual tape objects
class VisualTapeObject:
    def __init__(self,s,x,y,l,b):
        self.s=s
        self.cx=x
        self.cy=y
        self.l=l
        self.b=b
    

class DigiTape(VisualTapeObject):
    def __init__(self,s,x,y,l,b):
        super().__init__(s,x,y,l,b)
        self.cr=6
        self.mr=18
        
    def draw(self):
        pygame.draw.rect(self.s,BLACK,(self.cx-self.l/2,self.cy-self.b/2,self.l,self.b),1)
        # corner circles
        pygame.draw.circle(self.s,BLACK,(int(self.cx-self.l/2+self.cr),int(self.cy-self.b/2+self.cr)),self.cr,1)
        pygame.draw.circle(self.s,BLACK,(int(self.cx+self.l/2-self.cr-1),int(self.cy-self.b/2+self.cr)),self.cr,1)
        pygame.draw.circle(self.s,BLACK,(int(self.cx-self.l/2+self.cr),int(self.cy+self.b/2-self.cr)),self.cr,1)
        pygame.draw.circle(self.s,BLACK,(int(self.cx+self.l/2-self.cr-1),int(self.cy+self.b/2-self.cr)),self.cr,1)
        # central circles
        pygame.draw.circle(self.s,BLACK,(int(self.cx),int(self.cy-self.b/4)),self.mr,1)
        pygame.draw.circle(self.s,BLACK,(int(self.cx),int(self.cy+self.b/4)),self.mr,1)
        # central rectangle
        pygame.draw.rect(self.s,BLACK,(self.cx-self.l/14,self.cy-self.b/10,self.l/7,self.b/5),1)
        # trapezium
        draw_vert_trapezium(self.s,self.cx+self.l/2-12,self.cy,self.b/5,self.b/2,20)
        

# the tape visualizer
class TapeScope(VisualTapeObject):
    def __init__(self,s,x,y,l,b,n,m):
        super().__init__(s,x,y,l,b)
        if n%2==0:
            print('[SCOPE] auto-correcting even cells (%d) to odd (%d)'%(n,n+1))
            self.cells=n+1
        else:
            self.cells=n
        self.margin=m
    
    def render_cells(self):
        vxl=self.cx-self.l/2
        vy=self.cy-self.b/2+self.margin
        vxr=self.cx+self.l/2
        ew=self.b-2*self.margin
        vgap=ew/self.cells
        dx=3
        for i in range(self.cells+1):
            pygame.draw.line(self.s,BLACK,(vxl,vy),(vxr,vy))
            vy+=vgap
        pygame.draw.rect(self.s,RED,(self.cx-self.l/2-dx+1,self.cy-vgap/2-dx+1,self.l+2*dx-1,vgap+2*dx),1)
        
    def populate_cells(self,tapebuf=[]):
        print('[SCOPE] populating cells')
        
    def draw(self):
        pygame.draw.line(self.s,BLACK,(self.cx-self.l/2,self.cy-self.b/2),(self.cx-self.l/2,self.cy+self.b/2))
        pygame.draw.line(self.s,BLACK,(self.cx+self.l/2,self.cy-self.b/2),(self.cx+self.l/2,self.cy+self.b/2))
        self.render_cells()
        

class TioDsp(VisualTapeObject):
    def __init__(self,s,x,y,l,b):
        super().__init__(s,x,y,l,b)
        
    def draw(self):
        pygame.draw.rect(self.s,BLACK,(self.cx-self.l/2,self.cy-self.b/2,self.l,self.b),1)
        

class TpuDsp(VisualTapeObject):
    def __init__(self,s,x,y,l,b):
        super().__init__(s,x,y,l,b)
        self.digitape=DigiTape(self.s,self.cx-self.l*(5/16),self.cy,self.l/3,self.b/2)
        self.tapescope=TapeScope(self.s,self.cx-20,self.cy,self.l/12,self.b/2,10,10)
    
    def draw(self):
        pygame.draw.rect(self.s,BLACK,(self.cx-self.l/2,self.cy-self.b/2,self.l,self.b),1)
        self.digitape.draw()
        self.tapescope.draw()
        

class TapeUI(VisualTapeObject):
    def __init__(self,s,x,y,l,b):
        super().__init__(s,x,y,l,b)
        self.tpudsp=TpuDsp(s,x-l/4,y,l/2-5,b-5)
        self.tiodsp=TioDsp(s,x+l/4,y,l/2-5,b-5)
    
    def draw(self):
        pygame.draw.rect(self.s,BLACK,(self.cx-self.l/2,self.cy-self.b/2,self.l,self.b),1)
        self.tpudsp.draw()
        self.tiodsp.draw()

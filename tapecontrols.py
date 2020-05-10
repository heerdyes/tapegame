# ui controls for game
class ClickableRegion:
    def __init__(self,uid,x,y,l,b):
        self.uid=uid
        self.x=x
        self.y=y
        self.l=l
        self.b=b
    
    def handle_click(pos):
        if self.x<pos[0]<self.x+self.l and self.y<pos[1]<self.y+self.b:
            print('[CLICK] detected click on clickable_region: %s'%self.uid)
        

# mouseclick handler
class ToggleButton(ClickableRegion):
    def __init__(self,uid,x,y,l,b,txt,state):
        super().__init__(uid,x,y,l,b)
        self.txt=txt
        self.state=state # True is on, False is off
        
    def handle_click(pos):
        if self.x<pos[0]<self.x+self.l and self.y<pos[1]<self.y+self.b:
            print('[INFO] toggling state for button [%s]'%self.name)
            self.state=not self.state

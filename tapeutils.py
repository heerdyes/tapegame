import pygame
from tapeconstants import *

# the tape utility module functions
def text_objects(text,font,color):
    textsurf = font.render(text,True,color)
    return textsurf,textsurf.get_rect()

def cell_display(s,text,x,y,color):
    celltxt=pygame.font.Font('cour.ttf',14)
    txtsurf,txtrect=text_objects(text,celltxt,color)
    txtrect.center=(x,y)
    s.blit(txtsurf,txtrect)

def log_display(s,text,x,y,color):
    celltxt=pygame.font.Font('cour.ttf',12)
    txtsurf,txtrect=text_objects(text,celltxt,color)
    txtrect.center=(x,y)
    s.blit(txtsurf,txtrect)

def draw_hori_trapezium(s,cx,cy,a,b,h):
    pygame.draw.line(s,BLACK,(cx-a/2,cy-h/2),(cx+a/2,cy-h/2))
    pygame.draw.line(s,BLACK,(cx-a/2,cy-h/2),(cx-b/2,cy+h/2))
    pygame.draw.line(s,BLACK,(cx+a/2,cy-h/2),(cx+b/2,cy+h/2))
    pygame.draw.line(s,BLACK,(cx-b/2,cy+h/2),(cx+b/2,cy+h/2))

def draw_vert_trapezium(s,cx,cy,a,b,v):
    pygame.draw.line(s,BLACK,(cx-v/2,cy-a/2),(cx-v/2,cy+a/2))
    pygame.draw.line(s,BLACK,(cx-v/2,cy-a/2),(cx+v/2,cy-b/2))
    pygame.draw.line(s,BLACK,(cx-v/2,cy+a/2),(cx+v/2,cy+b/2))
    pygame.draw.line(s,BLACK,(cx+v/2,cy-b/2),(cx+v/2,cy+b/2))
    
def draw_control_panel(s,cx,cy,l,b):
    bw=l/3
    bh=b
    playrect=(cx-l/2,cy-bh,bw,bh)
    pygame.draw.rect(s,GREEN,playrect,1)
    cell_display('>',cx-l/2+bw/2,cy-b/2,GREEN)
    pauserect=(cx-bw/2,cy-bh,bw,bh)
    pygame.draw.rect(s,RED,pauserect,1)
    cell_display('||',cx,cy-b/2,RED)
    resetrect=(cx+bw/2,cy-bh,bw,bh)
    pygame.draw.rect(s,BLACK,resetrect,1)
    cell_display('<<',cx+bw,cy-b/2,BLACK)
    return [playrect,pauserect,resetrect]

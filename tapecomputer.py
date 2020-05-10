import pygame
from digitaltape import *
from tapeconstants import *
from tapeobjects import *

pygame.init()

w=1000
h=600
dspsize=(w,h)
screen=pygame.display.set_mode(dspsize)
pygame.display.set_caption("tape grid computer")

carryon=True
clock=pygame.time.Clock()

# flow
tapeui=TapeUI(screen,w/2,h/2,960,580)
while carryon:
    # main event loop
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            carryon=False
        if event.type==pygame.MOUSEBUTTONUP:
            pos=pygame.mouse.get_pos()
            print('[TODO] broadcast click')
            
    # tape computation logic invocation
    
    # drawing code
    screen.fill(WHITE)
    tapeui.draw()
    # update screen
    pygame.display.flip()
    
    # fps limit
    clock.tick(30)

pygame.quit()

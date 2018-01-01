import pygame as pg
import sys
from colors import *
import time

WIDTH = 20
HEIGHT = 5
BLOCKSIZE = 20
BLOCKSIZE_INNER = 14
BLOCK_OFFSET = 3

wallblock = pg.Surface((BLOCKSIZE,BLOCKSIZE))
wallblock.set_alpha(255)
wallblock.fill(BLUE)
wallblockdark = pg.Surface((BLOCKSIZE_INNER,BLOCKSIZE_INNER))
wallblockdark.set_alpha(255)
wallblockdark.fill(BLUE_DARK)

def drawWalls(surface):
	surface.blit(wallblock,(0,0))
	surface.blit(wallblockdark,(BLOCK_OFFSET,BLOCK_OFFSET))

pg.init()

screen = pg.display.set_mode(((WIDTH+1)*BLOCKSIZE,(HEIGHT+1)*BLOCKSIZE))
pg.display.set_caption("mysnake")
font = pg.font.SysFont(pg.font.get_default_font(),40)
starttext = font.render("PRESS A OR 1 TO START",1,RED)
screen.fill(GREEN)

drawWalls(screen)
screen.blit(starttext,((WIDTH-15)*BLOCKSIZE/2,HEIGHT*BLOCKSIZE/2))
pg.display.flip()
waiting = True
while waiting:
	event = pg.event.wait()
	if event.type == pg.KEYDOWN:
		waiting = False
screen.fill(BLACK)
time.sleep(0.5)

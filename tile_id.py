import pygame as p
from helper import res
import pygame.freetype
from settings import TILE_SIZE

p.init()
win = p.display.set_mode((544, 256))
image = p.image.load(res / 'map' / '14389872632b38dd525b21.68139357rpg_tileset.png')
image = p.transform.scale(image, (544, 256))
font = p.freetype.Font(None, 16)

running = 1
index = 0
for y in range(0, 256, TILE_SIZE):
    for x in range(0, 544, TILE_SIZE):
        font.render_to(image, (x + 10, y + 10), str(index))
        index += 1

while running:
    for event in p.event.get():
        if event.type == p.QUIT or (event.type == p.KEYDOWN and event.key == p.K_ESCAPE):
            running = 0

    win.blit(image, (0, 0))
    p.display.flip()

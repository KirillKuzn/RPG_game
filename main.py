import pygame as p
from settings import *
from player import Player
from helper import res

p.init()

win = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
p.display.set_caption(GAME_TITLE)
p.display.set_icon(p.image.load(res/'sprites'/'frog.png'))
Clock = p.time.Clock()

player = Player(res/'sprites'/'player_sheet.png', (100, 100))
all_sprites = p.sprite.Group()
all_sprites.add(player)

running = 1
while running:
    for event in p.event.get():
        if event.type == p.QUIT or (event.type == p.KEYDOWN and event.key == p.K_ESCAPE):
            running = 0

    win.fill((255, 255, 255))
    all_sprites.draw(win)
    player.update()

    Clock.tick(FPS)
    p.display.flip()

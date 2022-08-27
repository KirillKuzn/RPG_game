# project1
main.py:
import pygame as p
from settings import *
from player import Player
from helper import res

p.init()

win = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
p.display.set_caption(GAME_TITLE)
p.display.set_icon(p.image.load(res/'frog.png'))
Clock = p.time.Clock()

player = Player(res/'player_sheet.png', (100, 100))
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


helper.py:
import pygame as p
from pathlib import Path

class SpaceSheet:
    def __init__(self, path):
        self.sheet = p.image.load(path).convert_alpha()

    def get_image(self, x, y, width, height):
        return self.sheet.subsurface(x, y, width, height)


res = Path("sprites")

player.py:
from helper import SpaceSheet
import pygame as p
from pygame.math import Vector2


class Player(p.sprite.Sprite):
    '''A class that realizes the behavior of a character'''
    speed = 5

    def __init__(self, image_path, pos):
        super().__init__()

        self.sprite_sheet = SpaceSheet(image_path)
        self.image = self.sprite_sheet.get_image(0, 0, 32, 32)
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        self._move()

    def _move(self):
        '''
        This method is responsible for the movement of the character
        :return: None
        '''
        self.velocity = Vector2(0, 0)
        keys = p.key.get_pressed()
        if keys[p.K_w]:
            self.velocity.y = -1
        if keys[p.K_s]:
            self.velocity.y = 1
        if keys[p.K_a]:
            self.velocity.x = -1
        if keys[p.K_d]:
            self.velocity.x = 1

        if self.velocity.length() > 1:
            self.velocity.x = 0
        self.velocity *= Player.speed
        self.rect.center += self.velocity

settings.py:
GAME_TITLE = 'RPG'
FPS = 60
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

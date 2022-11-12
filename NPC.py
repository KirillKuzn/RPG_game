import pygame as p
from settings import *

class NPC(p.sprite.Sprite):
    def __init__(self, game, image, pos):
        self.layer = GROUND_LAYER
        groups = game.all_sprites, game.walls
        super().__init__(groups)

        self.image = image
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        pass
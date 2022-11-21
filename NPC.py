import pygame as p
from settings import *
from message import Message

class NPC(p.sprite.Sprite):
    """ ."""
    def __init__(self, game, image, pos):
        """ ."""
        self._layer = GROUND_LAYER
        groups = game.all_sprites, game.walls
        super().__init__(groups)
        self.game = game
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.message = Message(game, (pos[0] - 10, pos[1] + 10), 'Hello')

    def update(self):
        """ ."""
        if self.rect.colliderect(self.game.player):
            if not self.message.groups():
                self.message.add(self.game.all_sprites)
                self.message.print()
        elif self.message.groups():
            self.message.kill()

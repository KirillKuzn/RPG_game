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

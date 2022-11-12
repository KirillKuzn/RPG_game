from helper import SpaceSheet
import pygame as p
from pygame.math import Vector2
from settings import *


class Player(p.sprite.Sprite):
    '''A class that realizes the behavior of a character'''
    speed = 5

    def __init__(self, game, image_path, pos):
        self._layer = PLAYER_LAYER
        super().__init__(game.all_sprites)

        self.sprite_sheet = SpaceSheet(image_path)
        self.game = game
        self.circle_len = 4
        self._load_images(self.sprite_sheet)
        self.image = self.go_down[0]
        self.rect = self.image.get_rect()
        self.rect.center = pos


        self.velocity = Vector2(0, 0)
        self.last_update = 0
        self.frame = 0

    def update(self):
        self._move()
        self._animate()

    def _move(self):
        '''
        This method is responsible for the movement of the character
        :return: None
        '''
        self.velocity.update(0, 0)
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
        if not self._check_walls():
            self.rect.center += self.velocity


    def _check_walls(self):
        target_player = self.rect.move(self.velocity)
        for target_wall in self.game.walls:
            if target_player.colliderect(target_wall):
                return True
        return False


    def _load_images(self, sheet):
        '''
        This method splits one picture into sixteen and allocates them into 4 lists
        '''
        self.go_up = []
        self.go_down = []
        self.go_right = []
        self.go_left = []

        w = sheet.w // self.circle_len
        h = sheet.h // self.circle_len
        for x in range(0, sheet.w, w):
            self.go_down.append(sheet.get_image(x, 0, w, h))
            self.go_left.append(sheet.get_image(x, h, w, h))
            self.go_right.append(sheet.get_image(x, h * 2, w, h))
            self.go_up.append(sheet.get_image(x, h * 3, w, h))

    def _animate(self):
        '''
        This method is responsible for the animation of the movement of our character
        '''
        now = p.time.get_ticks()
        if now - self.last_update > self.circle_len and self.velocity.length() > 0:
            self.last_update = now
            if self.velocity.y < 0:
                self.current_anim = self.go_up
            if self.velocity.y > 0:
                self.current_anim = self.go_down
            if self.velocity.x < 0:
                self.current_anim = self.go_left
            if self.velocity.x > 0:
                self.current_anim = self.go_right

            self.frame = (self.frame + 1) % self.circle_len
            self.image = self.current_anim[self.frame]




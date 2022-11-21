import pygame as p
import pygame.freetype
from settings import *

class Message(p.sprite.Sprite):
    def __init__(self, game, pos, text, font=None):
        self._layer = MSG_LAYER
        super().__init__(game.all_sprites)
        self.image = p.Surface((200, 100), p.SRCALPHA)
        self.rect = self.image.get_rect(topleft=pos)
        self.border = p.Rect((0, 0), self.rect.size)
        self.text = text
        self.pos_text = (10, 10)
        self.font = p.freetype.Font(font, 16)


    def print(self):
        p.draw.rect(self.image, (0, 0, 0), self.border, width=5, border_radius=10)
        self.font.render_to(self.image, self.pos_text, self.text)

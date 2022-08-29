import pygame as p
from pathlib import Path

class SpaceSheet:
    def __init__(self, path):
        self.sheet = p.image.load(path).convert_alpha()

    def get_image(self, x, y, width, height):
        return self.sheet.subsurface(x, y, width, height)


res = Path("sprites")

import pygame as p
from pathlib import Path

class SpaceSheet:
    def __init__(self, path, scale=1):
        sheet = p.image.load(path).convert_alpha()
        w, h = sheet.get_size()
        target_size = (int(w * scale), int(h * scale))
        self.sheet = p.transform.scale(sheet, target_size)
        self.w, self.h = self.sheet.get_size()

    def get_image(self, x, y, width, height):
        return self.sheet.subsurface(x, y, width, height)


res = Path("res")

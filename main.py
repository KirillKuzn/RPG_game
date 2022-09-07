import pygame as p
from settings import *
from player import Player
from helper import res

class Game:
    def __init__(self):
        p.init()

        self.win = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        p.display.set_caption(GAME_TITLE)
        p.display.set_icon(p.image.load(res / 'sprites' / 'frog.png'))
        self.Clock = p.time.Clock()
        self.running = 1

    def new(self):
        player = Player(res / 'sprites' / 'player_sheet.png', (100, 100))
        self.all_sprites = p.sprite.Group()
        self.all_sprites.add(player)

    def _events(self):
        for event in p.event.get():
            if event.type == p.QUIT or (event.type == p.KEYDOWN and event.key == p.K_ESCAPE):
                self.running = 0

    def _update(self):
        self.all_sprites.update()

    def _draw(self):
        self.win.fill((255, 255, 255))
        self.all_sprites.draw(self.win)
        p.display.flip()

    def run(self):
        while self.running:
            self._events()
            self._update()
            self._draw()
            self.Clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.new()
    game.run()

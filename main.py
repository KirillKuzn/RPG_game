import pygame as p
from settings import *
from player import Player
from helper import res
from world import TileMap, Camera
from NPC import NPC


class Game:
    def __init__(self):
        '''
        Initialization of pygame.
        '''
        p.init()

        self.win = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        p.display.set_caption(GAME_TITLE)
        p.display.set_icon(p.image.load(res / 'sprites' / 'frog.png'))
        self.Clock = p.time.Clock()
        self.running = 1


    def new(self):
        '''
        There are all sprites.
        '''

        self.all_sprites = p.sprite.LayeredUpdates()
        self.walls = p.sprite.Group()
        self.player = Player(self, res / 'sprites' / 'player_sheet.png', (100, 100))
        self.all_sprites.add(self.player)
        self.map = TileMap(self, res / 'map' / 'map.csv',
                           res / 'map' / '14389872632b38dd525b21.68139357rpg_tileset.png', 16)
        self.camera = Camera(self.map.width, self.map.height)
        self.NPC = NPC(self, self.map.image_list[119], (234, 323))

    def _events(self):
        '''
        Event tracking.
        '''
        for event in p.event.get():
            if event.type == p.QUIT or (event.type == p.KEYDOWN and event.key == p.K_ESCAPE):
                self.running = 0

    def _update(self):
        '''
        Update all sprites.
        '''
        self.all_sprites.update()
        self.camera.update(self.player)

    def _draw(self):
        '''
        Draw sprites, fill window and update screen
        '''
        self.win.fill((255, 255, 255))
        #self.all_sprites.draw(self.win)
        for sprite in self.all_sprites:
            self.win.blit(sprite.image, self.camera.apply(sprite))
        p.display.flip()

    def run(self):
        '''
        Game cycle.
        '''
        while self.running:
            self._events()
            self._update()
            self._draw()
            self.Clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.new()
    game.run()

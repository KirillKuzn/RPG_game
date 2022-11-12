import csv

import pygame as pg

from helper import res
from settings import *


class TileMap:
    """Class for storing attributes related to the game map."""
    WALL_IDS = [1, 2, 3, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                18, 19, 20, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
                35, 36, 37, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                52, 53, 54, 58, 59, 60, 61, 52, 53, 54, 65, 66, 67,
                69, 70, 75, 76, 77, 78, 79, 81, 82, 83, 84,
                92, 93, 94, 95, 96, 97, 98, 99, 100, 101,
                107, 108, 109, 110, 11, 112, 113, 114, 115, 116, 117, 118,
                119, 120, 121, 122, 123, 124, 125, 130, 131, 132, 133, 134, 135]

    def __init__(self, game, csv_path, image_path, img_tile_size, spacing=0):
        """Run the private functions to create a map."""
        data_list = self._csv_to_list(csv_path)
        self.image_list = self._parse_image(image_path, img_tile_size, spacing)
        self._load_tiles(game, data_list, self.image_list)
        self.width = len(data_list[0]) * TILE_SIZE
        self.height = len(data_list) * TILE_SIZE

    def _csv_to_list(self, csv_path):
        """Return a 2D list with data from the given csv file."""
        with open(csv_path) as f:
            reader = csv.reader(f)
            data = list(reader)
        return data

    def _parse_image(self, image_path, img_tile_size, spacing):
        """Return a list of tile images from the given tileset."""
        lst = []
        image = pg.image.load(image_path).convert()

        if img_tile_size != TILE_SIZE:
            scale = TILE_SIZE // img_tile_size
            current_size = image.get_size()
            spacing *= scale
            target_size = tuple(i * scale for i in current_size)
            image = pg.transform.scale(image, target_size)

        width, height = image.get_size()
        for y in range(0, height, TILE_SIZE + spacing):
            for x in range(0, width, TILE_SIZE + spacing):
                tile = image.subsurface(x, y, TILE_SIZE, TILE_SIZE)
                lst.append(tile)
        return lst

    def _load_tiles(self, game, data_list, image_list):
        """Create tile objects."""
        for i, row in enumerate(data_list):
            for j, index in enumerate(row):
                wall_id = int(index) in TileMap.WALL_IDS
                Tile(game, j, i, image_list[int(index)], wall_id)


class Tile(pg.sprite.Sprite):
    """Class for storing attributes related to a single tile."""

    def __init__(self, game, x, y, image, is_wall=False):
        """Create a tile sprite in the given position.

        Arguments:
        game - game object
        x, y - row and column where the tile should be placed
        image - image object
        """
        if is_wall:
            group = game.all_sprites, game.walls
        else:
            group = game.all_sprites
        self._layer = GROUND_LAYER
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect()

        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE


class Camera:
    '''
    Class for the movement of the card by the player
    '''
    def __init__(self, map_width, map_height):
        self.offset = (0, 0)
        self.map_width = map_width
        self.map_height = map_height

    def apply(self, image):
        '''
        The method makes the map move
        '''
        return image.rect.move(self.offset)

    def update(self, target):
        '''
        Method updates offset
        '''
        x = -target.rect.x + SCREEN_WIDTH // 2
        y = -target.rect.y + SCREEN_HEIGHT // 2
        x = min(x, 0)
        y = min(y, 0)
        x = max(x, SCREEN_WIDTH - self.map_width)
        y = max(y, SCREEN_HEIGHT - self.map_height)
        self.offset = (x, y)

import csv
import pygame as p
from settings import *


class TileMap:
    '''
    Class of map which made in TiledMap.
    '''
    def __init__(self, csv_path, image_path, spacing=0):
        data_list = self._csv_to_list(csv_path)
        image_list = self._parcing_image(image_path, spacing)

    def _csv_to_list(self, csv_path):
        '''
        Conversion .csv file to list.
        '''
        with open(csv_path) as f:
            reader = csv.reader(f)
            data = list(reader)

        return data

    def _parcing_image(self, image_path, spacing):
        '''
        This method splits one picture into many same pictures.
        '''
        image_list = []
        image = p.image.load(image_path).convert()

        width, height = image.get_size()
        for x in range(0, width, TILE_SIZE):
            for y in range(0, height, TILE_SIZE):
                tile = image.subsurface(x, y, TILE_SIZE, TILE_SIZE)
                image_list.append(tile)
        return image_list

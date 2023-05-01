import pygame as py
import copy
import random
from ship import Ship

class GameClass():

    def __init__(self, width, height, x_tiles, y_tiles):

        self.SCREEN_WIDTH  = width
        self.SCREEN_HEIGHT = height

        self.x_tiles = x_tiles
        self.y_tiles = y_tiles

        self.ship = Ship([random.randint(200, width*x_tiles-200), random.randint(200, height*y_tiles-200)])

        self.scroll_x, self.scroll_y = self.set_scrollers()


    def set_scrollers(self):
        coords = self.ship.space_coordinates + [self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT/2]

        if coords[0] <= self.SCREEN_WIDTH*self.x_tiles and coords[1] <= self.SCREEN_HEIGHT * self.y_tiles:
            self.scroll_x, self.scroll_y = -coords[0], -coords[1]

    def set_scrollers(self):
        screen_dim = [self.SCREEN_WIDTH, self.SCREEN_HEIGHT]
        coords = copy.deepcopy(self.ship.space_coordinates)
        tiles = [self.x_tiles, self.y_tiles]

        for i in range(2):

        
            if coords[i]+screen_dim[i]/2 <= screen_dim[i] * tiles[i] and coords[i]-screen_dim[i]/2 >= 0:
                coords[i] -= screen_dim[i]/2
            else:
                # ship is on the left end of the screen
                if coords[i] < (screen_dim[i]*tiles[i])/2:
                    coords[i] = 0
                # Ship is on the right end of the screen
                else:
                    coords[i] = (screen_dim[i] * (tiles[i]-1))

        return -coords[0], -coords[1]


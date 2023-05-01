import pygame as py
from ship import GameObject
import random

WIDTH = 1400
HEIGHT = 800

tiles_x = 2
tiles_y = 3

class Asteroid(GameObject):
    def __init__(self):

        img = py.image.load(f'assets/asteroids/Asteroids.png')

        space_coordinates = [random.randint(0, WIDTH*tiles_x), random.randint(0, HEIGHT*tiles_y)]

        vector = py.math.Vector2(2, 0)
        vector = vector.rotate(random.randint(0, 360))

        super().__init__(space_coordinates, vector, img)

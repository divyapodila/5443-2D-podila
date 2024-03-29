import os
import pygame
from .Physics import Collidable
from .Animation import AnimatedSprite
from . import settings


class Coin(pygame.sprite.Sprite):

    texture = None
    pickup_sound = None

    @staticmethod
    def _load_resources():

        if Coin.texture is None:
            Coin.texture = pygame.image.load(os.path.join(settings.img_folder,"Collectables", "coin.png")).convert_alpha()

        if Coin.pickup_sound is None:
            Coin.pickup_sound = pygame.mixer.Sound(os.path.join(settings.music_folder, "Retro PickUp Coin 04.wav"))
            Coin.pickup_sound.set_volume(0.2)

    def __init__(self, x, y, groups):
        self._layer = 3
        self.rect = pygame.Rect(x, y, 40, 40)
        pygame.sprite.Sprite.__init__(self, groups)
        self._load_resources()
        self.animated_sprite = AnimatedSprite(8, loop=True)
        self.animated_sprite.load_from_spritesheet(Coin.texture, (40, 40), 4)

    def update(self, delta_time):
        self.animated_sprite.next_frame(delta_time)

    def pickup(self):
        Coin.pickup_sound.play()
        self.kill()

    def render(self, surface, camera):
        self.animated_sprite.render(surface, camera.get_relative_pos(self.rect.x, self.rect.y))


class Health_Potion(pygame.sprite.Sprite):

    texture = None
    pickup_sound = None

    @staticmethod
    def _load_resources():

        if Health_Potion.texture is None:
            Health_Potion.texture = pygame.image.load(os.path.join(settings.img_folder,"Collectables", "potion.png")).convert_alpha()

        if Health_Potion.pickup_sound is None:
            Health_Potion.pickup_sound = pygame.mixer.Sound(os.path.join(settings.music_folder, "Retro PickUp Coin 04.wav"))
            Health_Potion.pickup_sound.set_volume(0.2)

    def __init__(self, x, y, groups):
        self._layer = 3
        self.rect = pygame.Rect(x, y, 40, 52)
        pygame.sprite.Sprite.__init__(self, groups)
        self._load_resources()
        self.animated_sprite = AnimatedSprite(8, loop=True)
        self.animated_sprite.load_from_spritesheet(Health_Potion.texture, (40, 52), 4)

    def update(self, delta_time):
        self.animated_sprite.next_frame(delta_time)

    def pickup(self):
        Health_Potion.pickup_sound.play()
        self.kill()

    def render(self, surface, camera):
        self.animated_sprite.render(surface, camera.get_relative_pos(self.rect.x, self.rect.y))



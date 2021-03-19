import pygame
from pygame.sprite import Sprite
from constants import SNAKE_SIZE


class Segment(Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = pygame.Surface([SNAKE_SIZE, SNAKE_SIZE])
        self.image.fill(pygame.Color('white'))
        self.rect = self.image.get_rect(center=center)
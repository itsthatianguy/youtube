import pygame
from constants import *


class GameBorder():
    def __init__(self, first_tile_center):
        x = first_tile_center[0] - ((SNAKE_SIZE / 2) + BORDER_THICKNESS + BORDER_PADDING)
        y = first_tile_center[1] - ((SNAKE_SIZE / 2) + BORDER_THICKNESS + BORDER_PADDING)
        length = (X_TILES * TILE_SIZE) + (2 * BORDER_PADDING) + BORDER_THICKNESS
        height = (Y_TILES * TILE_SIZE) + (2 * BORDER_PADDING) + BORDER_THICKNESS
        self.area = (x, y, length, height)

    def draw(self, surface):
        pygame.draw.rect(surface, pygame.Color("red"), self.area, BORDER_THICKNESS)

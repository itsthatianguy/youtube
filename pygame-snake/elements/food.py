import pygame
import random


class Food():
    def __init__(self):
        self.coords = (0,0)

    def update(self, snake_tiles, game_tiles):
        available_tiles = list(game_tiles.difference(snake_tiles))
        self.coords = random.choice(available_tiles)

    def get_coords(self):
        return self.coords

    def draw(self, surface):
        pygame.draw.circle(surface, pygame.Color("blue"), self.coords, 10)

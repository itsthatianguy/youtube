import pygame
from pygame.math import Vector2
from constants import TILE_SIZE
from .segment import Segment


class Snake():
    def __init__(self, length, start_center):
        self.segments = []
        self.sprites = pygame.sprite.Group()
        self.velocity = Vector2(TILE_SIZE, 0)
        self.allowed_keys = {
            pygame.K_UP: Vector2(0, -42),
            pygame.K_DOWN: Vector2(0, 42),
            pygame.K_LEFT: Vector2(-42, 0),
            pygame.K_RIGHT: Vector2(42, 0)
        }
        self.processing_event = False
        for i in range(length):
            x = start_center[0] - (TILE_SIZE * i)
            y = start_center[1]
            segment = Segment((x, y))
            self.sprites.add(segment)
            self.segments.append(segment)

    def new_head(self):
        center = self.segments[0].rect.center
        x = center[0] + self.velocity[0]
        y = center[1] + self.velocity[1]
        return Segment((x, y))

    def handle_input(self, key):
        if not self.processing_event:
            self.processing_event = True
            if key in self.allowed_keys and not self.allowed_keys[key] == -self.velocity:
                self.velocity = self.allowed_keys[key]

    def will_collide(self, game_tiles):
        occupying = self.get_all_coords()
        if len(self.sprites.sprites()) > len(occupying):
            return True
        remainder = occupying.difference(game_tiles)
        if len(remainder) > 0:
            return True
        
        return False

    def get_all_coords(self):
        result = set()
        for segment in self.segments:
            result.add(segment.rect.center)
        return result

    def grow(self):
        tail = self.segments[-1]
        new_segment = Segment(tail.rect.center)
        self.segments.append(new_segment)
        self.sprites.add(new_segment)
    
    def get_head_center(self):
        return self.segments[0].rect.center

    def update(self):
        tail = self.segments.pop()
        self.sprites.remove(tail)

        new_head = self.new_head()
        self.segments.insert(0, new_head)
        self.sprites.add(new_head)
        self.processing_event = False

    def draw(self, surface):
        self.sprites.draw(surface)
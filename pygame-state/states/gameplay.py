import pygame
from .base import BaseState


class Gameplay(BaseState):
    def __init__(self):
        super(Gameplay, self).__init__()
        self.rect = pygame.Rect((0, 0), (80, 80))
        self.rect.center = self.screen_rect.center
        self.next_state = "GAME_OVER"

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.rect.move_ip(0, -10)
            if event.key == pygame.K_DOWN:
                self.rect.move_ip(0, 10)
            if event.key == pygame.K_LEFT:
                self.rect.move_ip(-10, 0)
            if event.key == pygame.K_RIGHT:
                self.rect.move_ip(10, 0)
            if event.key == pygame.K_SPACE:
                self.done = True

    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        pygame.draw.rect(surface, pygame.Color("blue"), self.rect)

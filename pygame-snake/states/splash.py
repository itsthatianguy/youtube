import pygame
from .base import BaseState


class Splash(BaseState):
    def __init__(self):
        super(Splash, self).__init__()
        self.title_font = pygame.font.Font(None, 120)
        self.title = self.title_font.render("Incompetent Snake", True, pygame.Color("red"))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        self.next_state = "MENU"
        self.time_active = 0

    def update(self, dt):
        self.time_active += dt
        if self.time_active >= 3000:
            self.done = True

    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        surface.blit(self.title, self.title_rect)

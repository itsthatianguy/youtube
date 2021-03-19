import pygame
from .base import BaseState
from elements.game_border import GameBorder
from elements.snake import Snake
from elements.food import Food
from constants import *


class Gameplay(BaseState):
    def __init__(self):
        super(Gameplay, self).__init__()
        self.next_state = "GAME_OVER"
        self.title_font = pygame.font.Font(None, 72)
        self.game_title_text = self.title_font.render("Incompetent Snake", True, pygame.Color("white"))
        game_title_center = (self.screen_rect.center[0], 80)
        self.game_title_rect = self.game_title_text.get_rect(center=game_title_center)
        game_width, game_height = pygame.display.get_surface().get_size()
        self.x_start = int(GAME_MARGIN + (SNAKE_SIZE / 2))
        self.y_start = int((game_height - ((Y_TILES * TILE_SIZE) + GAME_MARGIN)) + (SNAKE_SIZE / 2))
        self.border = GameBorder((self.x_start, self.y_start))
        x_end = int(game_width - GAME_MARGIN)
        y_end = int(game_height - GAME_MARGIN)
        self.tiles = set()
        for x in range(self.x_start, x_end, TILE_SIZE):
            for y in range(self.y_start, y_end, TILE_SIZE):
                self.tiles.add((x, y))

    def startup(self, persistent):
        self.persist["score"] = 0
        self.update_speed = BASE_SPEED
        self.score = 0
        self.difficulty_level = 1
        snake_x = self.x_start + (4 * TILE_SIZE)
        snake_y = self.y_start + (3 * TILE_SIZE)
        self.snake = Snake(3, (snake_x, snake_y))
        self.food = Food()
        self.food.update(self.snake.get_all_coords(), self.tiles)

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.done = True
            else:
                self.snake.handle_input(event.key)

    def check_food(self):
        head_center = self.snake.get_head_center()
        food_coords = self.food.get_coords()
        if head_center == food_coords:
            self.snake.grow()
            self.food.update(self.snake.get_all_coords(), self.tiles)
            self.score += self.difficulty_level
            self.persist["score"] = self.score
            if self.score % 3 == 0 and not self.score == 0:
                self.difficulty_level += 1

    def update(self, dt):
        self.update_speed -= dt
        if self.update_speed <= 0:
            self.snake.update()
            if self.snake.will_collide(self.tiles):
                self.done = True
            self.check_food()
            self.update_speed = (BASE_SPEED / self.difficulty_level)

    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        surface.blit(self.game_title_text, self.game_title_rect)
        score_text = self.font.render(f"Score: {self.score}", True, pygame.Color("white"))
        surface.blit(score_text, (50, 90))
        self.border.draw(surface)
        self.snake.draw(surface)
        self.food.draw(surface)

import pygame
from constants import FPS
import sys


class BaseScreen:

    def __init__(self, window):
        self.window = window
        self.running = False
        self.next_screen = False
        self.game_time = 0

    def run(self):
        clock = pygame.time.Clock()
        self.running = True
        while self.running:
            self.game_time = pygame.time.get_ticks()
            clock.tick(FPS)
            self.draw()
            self.update()
            for event in pygame.event.get():
                self.manage_event(event)

            pygame.display.update()

    def draw(self):
        pass

    def update(self):
        pass

    def manage_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.running = False
            pygame.quit()
            sys.exit()


import pygame


class Maze(pygame.sprite.Group):

    def __init__(self):
        super().__init__()

    def add_sprite(self, block):
        self.add(block)

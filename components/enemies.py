import pygame


class Enemies(pygame.sprite.Group):

    def __init__(self):
        super().__init__()

    def add_virus(self, virus):
        self.add(virus)

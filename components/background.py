import pygame


class Background(pygame.sprite.Group):

    def __init__(self, image):
        super().__init__()
        self.image = image

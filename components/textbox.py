import pygame
from constants import WIDTH


class TextBox(pygame.sprite.Sprite):

    def __init__(self, font_size, text, color):
        super().__init__()
        font = pygame.font.Font("font/FiraCode-Bold.ttf", font_size)
        self.text_box = font.render(text, True, color)
        self.rect = self.text_box.get_rect()
        self.rect.left = WIDTH / 2 - self.rect.width / 2

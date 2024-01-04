import pygame


class BackgroundImage(pygame.sprite.Sprite):

    def __init__(self, image):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image).convert(), (750, 750))
        self.rect = self.image.get_rect()
        self.rect.right = 750
        self.rect.bottom = 750

    def update(self, x_movement, y_movement):
        self.rect.left += x_movement
        self.rect.top += y_movement

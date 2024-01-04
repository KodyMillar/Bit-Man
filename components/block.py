import pygame
from constants import TILE_SIZE
from functools import lru_cache

@lru_cache
def get_scaled_image():
    BLOCK_IMAGE = pygame.image.load("images/block.png").convert_alpha()
    BLOCK_IMAGE_SCALED = pygame.transform.scale(BLOCK_IMAGE, (TILE_SIZE, TILE_SIZE))

    return BLOCK_IMAGE_SCALED

class Block(pygame.sprite.Sprite):


    def __init__(self):
        super().__init__()
        self.length = 10
        self.width = 8
        self.tile_pos_x = 0
        self.tile_pos_y = 0
        self.image = get_scaled_image()
        self.rect = self.image.get_rect()
        self.rect.right = 100
        self.rect.bottom = 100

    def update(self, movement_x, movement_y):
        self.rect.left += movement_x
        self.rect.top += movement_y

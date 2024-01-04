import pygame
from constants import WIDTH, HEIGHT


class BitMan(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        image = pygame.image.load("images/bitman.png")
        self.image = pygame.transform.scale(image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT / 2 + 50
        self.rect.right = WIDTH / 2 + 50
        self.restricted_movement = {"left": False, "right": False, "up": False, "down": False}
        self.second_restriction = None
        self.direction = "Left"
        self.mask = pygame.mask.from_surface(self.image)
        self.obtained_antivirus = False

    def face_right(self):
        if self.direction == "Left":
            self.image = pygame.transform.flip(self.image, flip_x=True, flip_y=False)
            self.direction = "Right"

    def face_left(self):
        if self.direction == "Right":
            self.image = pygame.transform.flip(self.image, flip_x=True, flip_y=False)
            self.direction = "Left"

    def restrict_movement(self, direction):
        self.restricted_movement[direction] = True

    def remove_restriction(self, direction):
        self.restricted_movement[direction] = False

    def get_restricted_movement(self, direction):
        return self.restricted_movement[direction]

    def reset_restrictions(self):
        self.restricted_movement = self.restricted_movement.fromkeys(("left", "right", "up", "down"), False)

    def get_antivirus(self):
        self.obtained_antivirus = True

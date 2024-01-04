import pygame

class AntiVirus(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("images/anti-virus.png").convert_alpha(), (80, 80))
        self.rect = self.image.get_rect()
        self.camera_pos_x = 0
        self.camera_pos_y = 0
        self.obtained = False

    def update(self, movement_x, movement_y):
        if not self.obtained:
            self.rect.left += movement_x
            self.rect.top += movement_y

    def get_carried(self, bitman):
        # Carried by bitman when he collects antivirus
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.obtained = True
        self.rect.left = bitman.rect.left
        self.rect.top = bitman.rect.top + 10


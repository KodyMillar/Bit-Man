import pygame
from .base import BaseScreen
from components.textbox import TextBox
from constants import TITLE_SIZE, TEXT_SIZE, TEXT_COLOR, WIDTH, HEIGHT


class VictoryScreen(BaseScreen):

    def __init__(self, window):
        super().__init__(window)
        self.window = window
        self.play_again = False
        self.bitman = pygame.transform.scale(pygame.image.load("images/bitman.png").convert_alpha(), (100, 100))
        self.background = pygame.transform.scale(pygame.image.load("images/cybersecurity.png").convert_alpha(), (WIDTH / 3, HEIGHT / 2 + 50))
        self.binary_background = pygame.transform.scale(pygame.image.load("images/binary.png").convert_alpha(), (WIDTH, HEIGHT))
        self.victory = TextBox(TITLE_SIZE, "Victory", (18, 204, 195))
        self.success_message = TextBox(TEXT_SIZE, "You saved the computer from the viruses!", TEXT_COLOR)
        self.play_again_textbox = TextBox(TEXT_SIZE, "Press Enter to play again", TEXT_COLOR)
    
    def draw(self):
        self.window.fill((32, 69, 138))
        self.window.blit(self.binary_background, (0, 0))
        self.window.blit(self.background, (WIDTH / 2 - self.background.get_rect().width / 2, HEIGHT / 2 - 60))
        self.window.blit(self.victory.text_box, (self.victory.rect.left, 100))
        self.window.blit(self.success_message.text_box, (self.success_message.rect.left, 200))
        self.window.blit(self.bitman, (WIDTH / 2 - self.bitman.get_rect().width / 2, 20))
        self.window.blit(self.play_again_textbox.text_box, (self.play_again_textbox.rect.left, 250))

    def manage_event(self, event):
        super().manage_event(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.play_again = True
            self.running = False


import pygame
from .base import BaseScreen
from components.textbox import TextBox
from constants import TITLE_SIZE, TEXT_SIZE, TEXT_COLOR, WIDTH, HEIGHT


class GameOver(BaseScreen):

    def __init__(self, window):
        super().__init__(window)
        self.play_again = False
        game_over_title = "The Viruses Took Over"
        back_to_menu = "Press enter to go to the main menu"
        quit = "Press Esc to quit"
        self.game_over_textbox = TextBox(TITLE_SIZE, game_over_title, (242, 211, 70))
        self.back_to_menu_textbox = TextBox(TEXT_SIZE, back_to_menu, (TEXT_COLOR))
        self.quit = TextBox(TEXT_SIZE, quit, TEXT_COLOR)
        self.game_over_background = pygame.transform.scale(pygame.image.load("images/computer_crash.jpg").convert(), (WIDTH, HEIGHT))

    def manage_event(self, event):
        super().manage_event(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.play_again = True
            self.running = False

    def draw(self):
        self.window.blit(self.game_over_background, (0, 0))
        self.window.blit(self.game_over_textbox.text_box, (self.game_over_textbox.rect.left, 100))
        self.window.blit(self.back_to_menu_textbox.text_box, (self.back_to_menu_textbox.rect.left, 400))
        self.window.blit(self.quit.text_box, (self.quit.rect.left, 475))

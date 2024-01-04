import pygame
from .base import BaseScreen
from components.textbox import TextBox
from constants import TEXT_SIZE, TITLE_SIZE, TEXT_COLOR, WIDTH, HEIGHT
import sys


class MainMenu(BaseScreen):

    def __init__(self, window):
        super().__init__(window)
        game_title = "Bit Man"
        self.menu_title_textbox = TextBox(TITLE_SIZE, game_title, (18, 204, 195))
        self.student_info = TextBox(TEXT_SIZE, "Kody Millar - A01360468", TEXT_COLOR)
        self.start_game_button = TextBox(TEXT_SIZE, "Start Game", TEXT_COLOR)
        self.quit_game_button = TextBox(TEXT_SIZE, "Quit Game", TEXT_COLOR)
        self.background = pygame.transform.scale(pygame.image.load("images/title_screen.jpg").convert(), (WIDTH + 200, 1000))
        self.sel_pos = 290
        self.selection = "start"

    def manage_event(self, event):
        super().manage_event(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if self.sel_pos < 365:
                self.sel_pos += 75
                self.selection = "quit"
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if self.sel_pos > 290:
                self.sel_pos -= 75
                self.selection = "start"
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.running = False
            if self.selection == "quit":
                pygame.quit()
                sys.exit()

    def draw(self):
        self.window.blit(self.background, (0, -50))
        self.window.blit(self.student_info.text_box, (self.student_info.rect.left, 50))
        self.window.blit(self.menu_title_textbox.text_box, (self.menu_title_textbox.rect.left, 100))
        self.window.blit(self.start_game_button.text_box, (self.start_game_button.rect.left, 300))
        self.window.blit(self.quit_game_button.text_box, (self.start_game_button.rect.left + 10, 375))
        pygame.draw.rect(self.window, (80, 167, 217), (self.start_game_button.rect.left - 20, self.sel_pos, 280, 80), width=10)

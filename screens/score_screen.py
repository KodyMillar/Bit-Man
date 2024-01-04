import pygame
from .base import BaseScreen
from components.textbox import TextBox
from constants import TITLE_SIZE, TEXT_SIZE, TEXT_COLOR, WIDTH, HEIGHT


class ScoreScreen(BaseScreen):

    def __init__(self, window, level_time_limit, completion_time, text, victory=False):
        super().__init__(window)
        self.background = pygame.transform.scale(pygame.image.load("images/circuit6.png").convert_alpha(), (WIDTH, HEIGHT))
        self.screen_title = TextBox(TITLE_SIZE, text, TEXT_COLOR)
        narrative_message = "...but the computer is still in danger!"
        time_limit_text = "Round Time Limit: " + str(level_time_limit)
        completion_time_text = "Completion Time: " + str(completion_time)
        self.time_limit_textbox = TextBox(TEXT_SIZE, time_limit_text, TEXT_COLOR)
        self.completion_time_text = TextBox(TEXT_SIZE, completion_time_text, TEXT_COLOR)
        self.narrative_message_textbox = TextBox(TEXT_SIZE, narrative_message, TEXT_COLOR)
        self.victory = victory

    def manage_event(self, event):
        super().manage_event(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.running = False

    def draw(self):
        self.window.fill((0, 0, 0))
        self.window.blit(self.background, (0, 0))
        self.window.blit(self.screen_title.text_box, (self.screen_title.rect.left, 100))
        if not self.victory:
            self.window.blit(self.narrative_message_textbox.text_box, (self.narrative_message_textbox.rect.left, 200))
        self.window.blit(self.time_limit_textbox.text_box, (self.time_limit_textbox.rect.left, 300))
        self.window.blit(self.completion_time_text.text_box, (self.completion_time_text.rect.left, 350))

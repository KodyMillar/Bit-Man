import pygame


class Timer:

    def __init__(self, time_limit):
        self.time_before_round = pygame.time.get_ticks()
        # self.time = pygame.time.get_ticks() - self.time_before_round
        self.time_limit = time_limit
        self.time_remaining = time_limit
        self.completed_time = 0
        self.timer_background = pygame.Surface((90, 45)).convert()
        default_font = pygame.font.get_default_font()
        self.font = pygame.font.Font(default_font, 30)
        self.timer = self.convert_time(self.time_limit)
        self.timer_display = self.font.render(str(self.timer), True, (255, 61, 61))

    def update(self, game_time):
        self.time_remaining = self.time_limit - game_time
        self.timer = self.convert_time(self.time_remaining)
        self.timer_display = self.font.render(str(self.timer), True, (255, 61, 61))

    def get_time_limit(self):
        return self.convert_time(self.time_limit)

    def get_completed_time(self):
        self.completed_time = self.time_limit - self.time_remaining + 1000
        return self.convert_time(self.completed_time)

    @staticmethod
    def convert_time(time_remaining):
        seconds = int(time_remaining / 1000)
        minutes = int(seconds // 60)
        formatted_seconds = seconds - ((seconds // 60) * 60)
        return str(minutes) + ":" + str("{:02d}".format(formatted_seconds))

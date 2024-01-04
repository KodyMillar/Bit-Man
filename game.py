import pygame
from constants import WIDTH, HEIGHT, game_levels
from screens.game import GameScreen
from screens.score_screen import ScoreScreen
from screens.game_over import GameOver
from screens.main_menu import MainMenu
from screens.victory_screen import VictoryScreen


def main():
    """The main function to run the game"""
    pygame.init()
    pygame.font.init()

    # Keep track of game over
    game_over = False

    # Create the game window
    game_window = pygame.display.set_mode((WIDTH, HEIGHT))

    # Create the game over screen
    game_over_screen = GameOver(game_window)

    # Create main menu
    main_menu = MainMenu(game_window)

    # Clear any events from previous gameplay
    pygame.event.clear()

    # Run the main menu
    main_menu.run()

    # Initialize window
    pygame.key.set_repeat(20, 0)

    # Game loop
    for level in game_levels.values():
        game_screen = GameScreen(game_window, level["maze"], level["time limit"], level["background"], level["virus speed"])
        game_screen.run()
        
        # If the player lost, then break the game loop
        game_over = game_screen.lost
        if game_over:
            break
        score_screen = ScoreScreen(game_window, game_screen.timer.get_time_limit(), game_screen.timer.get_completed_time(), level["score screen title"], victory=level["victory"])
        score_screen.run()

    # Victory Screen
    victory_screen = VictoryScreen(game_window)
    if not game_over:
        victory_screen.run()
        if victory_screen.play_again is True:
            main()

    # Check for game over screen
    if game_over:
        game_over_screen.run()
        if game_over_screen.play_again is True:
            main()
    

if __name__ == "__main__":
    main()

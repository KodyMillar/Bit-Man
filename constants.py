WIDTH = 1200
HEIGHT = 700
TILE_SIZE = 100
FPS = 120
TITLE_SIZE = 80
TEXT_SIZE = 40
TEXT_COLOR = (255, 255, 255)

# Levels to loop through in the main function
game_levels = {
        "level 1": {
            "maze": "mazes/maze_level_1.csv",
            "time limit": 180000,
            "background": "images/circuit5.png",
            "virus speed": 4,
            "score screen title": "Level 1 Completed",
            "victory": False
        },
        "level 2": {
            "maze": "mazes/maze_level_2.csv",
            "time limit": 120000, 
            "background": "images/circuit4.png", 
            "virus speed": 4,
            "score screen title": "Level 2 Completed",
            "victory": False
        },
        "level 3": {
            "maze": "mazes/maze_level_3.csv", 
            "time limit": 100000, 
            "background": "images/circuit3.png", 
            "virus speed": 5,
            "score screen title": "Level 3 Completed",
            "victory": True
        }

    }

from components.block import Block
from components.virus import Virus
from components.background_image import BackgroundImage
from constants import TILE_SIZE


def draw_maze(maze, maze_layout, anti_virus, enemies, enemies_cam_pos, background, virus_speed):
    """Draw the maze of the level based on the numbers in the maze layout"""
    # Iterate through the list of numbers from the csv file
    for row_num, row in enumerate(maze_layout):
        for col_num, column in enumerate(row):

            # Create the background images
            if (col_num * TILE_SIZE) % 700 == 0 and (row_num * TILE_SIZE) % 700 == 0:
                bg_image = BackgroundImage(background.image)
                bg_image.rect.left = col_num * TILE_SIZE
                bg_image.rect.top = row_num * TILE_SIZE
                background.add(bg_image)

            # Create the block sprite if number is 1
            if column == "1":
                block = Block()

                # Set block position based on the tile size and the index in the list
                block.rect.left = col_num * TILE_SIZE 
                block.rect.top = row_num * TILE_SIZE
                maze.add(block)

            # Create the antivirus sprite if number is 7
            elif column == "7":
                anti_virus.rect.left = col_num * TILE_SIZE
                anti_virus.rect.top = row_num * TILE_SIZE

            # Create a virus sprite if number is between 2-6
            elif column != "0":
                virus = Virus(column, virus_speed)
                virus.rect.left = col_num * TILE_SIZE
                virus.rect.top = row_num * TILE_SIZE
                enemies.add_virus(virus)
                enemies_cam_pos.add_virus(virus) # create another sprite group for virus camera position
    return maze

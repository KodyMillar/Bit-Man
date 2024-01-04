import pygame
from constants import TILE_SIZE
import random


class Virus(pygame.sprite.Sprite):

    def __init__(self, image_num, speed, direction=None):
        super().__init__()
        virus_images = {
            "2": "images/orange_virus.png",
            "3": "images/purple_virus.png",
            "4": "images/spike_virus.png",
            "5": "images/worm.png",
            "6": "images/trojan.png"
        }
        image = pygame.image.load(virus_images[image_num])
        self.image = pygame.transform.scale(image, (80, 80))
        self.rect = self.image.get_rect()
        self.direction = 5
        self.direction_facing = direction
        self.speed = speed
        self.camera_pos_x = 0 # keep track of cam position for blocks_ahead_of_virus() method
        self.camera_pos_y = 0
        self.movement_x = random.choice([-self.speed, self.speed])
        self.movement_y = random.choice([-self.speed, self.speed])
        self.axis = random.choice(["x", "y"])
        self.dead = False
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, maze, camera_pos_x=None, camera_pos_y=None):
        if maze:
            if "1" in self.blocks_ahead_of_virus(maze):
                self.change_movement()
            if self.axis == "x":
                self.rect.left += self.movement_x
                self.direction = self.movement_x
                if self.movement_x > 0 and self.direction_facing != "right":
                    self.direction_facing = "right"
                    self.image = pygame.transform.flip(self.image, flip_x=True, flip_y=False)
                elif self.movement_x < 0 and self.direction_facing != "left":
                    self.direction_facing = "left"
                    self.image = pygame.transform.flip(self.image, flip_x=True, flip_y=False)
            else:
                self.rect.top += self.movement_y
                self.direction = self.movement_y
        else:
            self.rect.left += camera_pos_x
            self.rect.top += camera_pos_y
            self.camera_pos_x += camera_pos_x
            self.camera_pos_y += camera_pos_y

    def change_movement(self):
        self.movement_x = random.choice([-self.speed, self.speed])
        self.movement_y = random.choice([-self.speed, self.speed])
        self.axis = random.choice(["x", "y"])

    def blocks_ahead_of_virus(self, maze):
        # Get direction in front of the virus
        x_ahead = self.rect.x + self.movement_x / self.speed
        y_ahead = self.rect.y + self.movement_y / self.speed

        if self.axis == "x" and self.direction > 0:
            x_ahead = self.rect.right + self.movement_x / self.speed
        if self.axis == "y" and self.direction > 0:
            y_ahead = self.rect.bottom + self.movement_y / self.speed

        # see if he will collide with a wall
        maze_index_x = int((x_ahead - self.camera_pos_x) // TILE_SIZE) 
        maze_index_y = int((y_ahead - self.camera_pos_y) // TILE_SIZE)
        blocks = [maze[maze_index_y][maze_index_x]]
        return blocks

    def kill_virus(self):
        self.dead = True

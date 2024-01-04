import pygame
from .base import BaseScreen
from components.bit_man import BitMan
from components.enemies import Enemies
from components.enemies_camera_position import EnemiesCameraPosition
from components.anti_virus import AntiVirus
from components.background import Background
from components.maze import Maze
from draw import draw_maze
from components.timer import Timer
from constants import WIDTH
import csv


class GameScreen(BaseScreen):

    def __init__(self, window, maze_file, time_limit, background_image, virus_speed):
        super().__init__(window)
        with open(maze_file, "r") as csvfile:
            self.maze_layout = list(csv.reader(csvfile))
        self.bitman = BitMan()
        self.enemies = Enemies()
        self.enemies_cam_pos = EnemiesCameraPosition()
        self.anti_virus = AntiVirus()
        self.background = Background(background_image)
        maze = Maze()
        self.maze = draw_maze(maze, self.maze_layout, self.anti_virus, self.enemies, self.enemies_cam_pos, self.background, virus_speed) 
        self.timer = Timer(time_limit)
        self.touched_wall = []
        self.lost = False

    def update(self):
        # update the sprites to move
        self.bitman.update()
        self.enemies.update(self.maze_layout)
        self.timer.update(self.game_time - self.timer.time_before_round)

        # Check if bitman collides with maze wall
        self.touched_wall = pygame.sprite.spritecollide(self.bitman, self.maze, dokill=False, collided=pygame.sprite.collide_rect)

        # Die or kill virus when colliding with virus
        touched_virus = pygame.sprite.spritecollide(self.bitman, self.enemies, dokill=False, collided=pygame.sprite.collide_mask)
        if touched_virus:
            if self.bitman.obtained_antivirus:
                for virus in touched_virus:
                    virus.kill()
            else:
                pygame.time.wait(1000)
                self.running = False
                self.lost = True

        # Collect antivirus
        if pygame.Rect.colliderect(self.bitman.rect, self.anti_virus.rect):
            self.bitman.get_antivirus()
            self.anti_virus.get_carried(self.bitman)

        # Check if all viruses have been killed
        for virus in self.enemies:
            if virus.dead is False:
                break
        else:
            self.running = False

        # Check if time limit has been reached
        if self.timer.time_remaining <= 0:
            self.running = False
            self.lost = True

    def manage_event(self, event):
        super().manage_event(event)

        # Reset bitman movement restrictions when no longer touching a wall
        if any(self.bitman.restricted_movement.values()) and len(self.touched_wall) == 0:
            self.bitman.reset_restrictions()

        # Check if character is in corner of maze wall
        bottomleft_collision = [wall.rect.collidepoint(self.bitman.rect.bottomleft) for wall in self.touched_wall]
        topleft_collision = [wall.rect.collidepoint(self.bitman.rect.topleft) for wall in self.touched_wall]
        topright_collision = [wall.rect.collidepoint(self.bitman.rect.topright) for wall in self.touched_wall]
        bottomright_collision = [wall.rect.collidepoint(self.bitman.rect.bottomright) for wall in self.touched_wall]

        # Checks the same conditions for the hitting the right, left, up, and down keys
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            self.bitman.face_right()

            # Check for hitting a wall
            if self.touched_wall and any(self.bitman.restricted_movement.values()) is False:
                self.bitman.restrict_movement("right")
            
            # Check if hitting a corner
            if any(topright_collision) and any(bottomright_collision):
                self.bitman.restrict_movement("right")

            # Move character and camera position if not hitting a wall
            if self.bitman.get_restricted_movement("right") is False:
                self.background.update(-10, 0)
                self.maze.update(-10, 0)
                self.anti_virus.update(-10, 0)
                self.enemies_cam_pos.update(None, -10, 0)

            # Remove movement restriction if touching a wall on the opposite side of his direction
            if self.bitman.get_restricted_movement("left") is True:
                self.bitman.remove_restriction("left")

        # Check for left wall collisions and move character left
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            self.bitman.face_left()
            
            if self.touched_wall and any(self.bitman.restricted_movement.values()) is False:
                self.bitman.restrict_movement("left")        
            
            if any(bottomleft_collision) and any(topleft_collision):
                self.bitman.restrict_movement("left")
    
            if self.bitman.get_restricted_movement("left") is False:
                self.background.update(10, 0)
                self.maze.update(10, 0)
                self.anti_virus.update(10, 0)
                self.enemies_cam_pos.update(None, 10, 0)

            if self.bitman.get_restricted_movement("right") is True:
                self.bitman.remove_restriction("right")

        # Check for wall collisions above and move character up
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            
            if self.touched_wall and any(self.bitman.restricted_movement.values()) is False:
                self.bitman.restrict_movement("up")

            if any(topleft_collision) and any(topright_collision):
                self.bitman.restrict_movement("up")
            
            if self.bitman.get_restricted_movement("up") is False:
                self.background.update(0, 10)
                self.maze.update(0, 10)
                self.anti_virus.update(0, 10)
                self.enemies_cam_pos.update(None, 0, 10)

            if self.bitman.get_restricted_movement("down") is True:
                self.bitman.remove_restriction("down")

        # Check for wall collisions below and move character down
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:

            if self.touched_wall and any(self.bitman.restricted_movement.values()) is False:
                self.bitman.restrict_movement("down")
            
            if any(bottomleft_collision) and any(bottomright_collision):
                self.bitman.restrict_movement("down")
            
            if self.bitman.get_restricted_movement("down") is False:
                self.background.update(0, -10)
                self.maze.update(0, -10)
                self.anti_virus.update(0, -10)
                self.enemies_cam_pos.update(None, 0, -10)

            if self.bitman.get_restricted_movement("up") is True:
                self.bitman.remove_restriction("up")

    def draw(self):
        if not self.lost:
            self.window.fill((250, 250, 250))

            # Draw the background
            self.background.draw(self.window)

            # Draw the main character sprite
            self.window.blit(self.bitman.image, (self.bitman.rect.x, self.bitman.rect.y))
            self.window.blit(self.anti_virus.image, (self.anti_virus.rect.left + 10, self.anti_virus.rect.top + 10))
            self.enemies.draw(self.window)

            # Draw the maze
            self.maze.draw(self.window)

            # Draw the timer
            self.timer.timer_background.fill((0, 0, 0))
            self.window.blit(self.timer.timer_background, (WIDTH-195, 10))
            self.window.blit(self.timer.timer_display, (WIDTH - 180, 20))
        else:
            pass

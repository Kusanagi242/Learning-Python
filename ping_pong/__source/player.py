import pygame
from define import *

class Player():
    x = 0
    y = 0
    color = ""

    def __init__(self, color, x, y):
        self.x = x
        self.y = y
        self.color = color

    # DISPLAY THE PLAYER
    def show(self, surface):
         pygame.draw.rect(surface, self.color, (self.x, self.y, PLAYER_WIDTH, PLAYER_HEIGHT))

    # Function motivation
    # MOVE UP
    def move_up(self):
        print(f"{self.color} moving up {PLAYER_VELOCITY}")
        self.y -= PLAYER_VELOCITY
        if self.y < 0:
            self.y = 0

    # MOVE DOWN
    def move_down(self):
        print(f"{self.color} moving down {PLAYER_VELOCITY}")
        self.y += PLAYER_VELOCITY
        if self.y > WINDOW_HEIGHT - PLAYER_HEIGHT:
            self.y = WINDOW_HEIGHT - PLAYER_HEIGHT
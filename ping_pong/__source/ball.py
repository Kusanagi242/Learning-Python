import pygame
from define import *

class Ball():
    x = WINDOW_WIDTH / 2
    y = WINDOW_HEIGHT / 2


    def __init__(self, color, x, y):
        self.x = x
        self.y = y
        self.color = color
        self.radius = BALL_SIZE
        self.x_vel = BALL_VELOCITY
        self.y_vel = 0

    def show(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def handle_collision(self, playerLeft, playerRight):
        # Move and collision in vertical direction 
        if self.y + self.radius >= WINDOW_HEIGHT:
            self.y_vel *= -1 # reverse the direction in vertical
        elif self.y + self.radius <= 0:
            self.y_vel *= -1

        # Move and collision in horizontal direction
        if self.x_vel < 0:
            # Neu qua bong nam trong khoang canh tren va canh duoi
            if self.y >= playerLeft.y and self.y <= playerLeft.y + PLAYER_HEIGHT:
                # Neu qua bong cham vao player
                if self.x - self.radius <= playerLeft.x + PLAYER_WIDTH:
                    self.x_vel *= -1 # dao chieui qua bong
        else:
            if self.y >= playerRight.y and self.y <= playerRight.y + PLAYER_HEIGHT:
                # Neu qua bong cham vao player
                if self.x + self.radius >= playerRight.x:
                    self.x_vel *= -1 # dao chieui qua bong
        


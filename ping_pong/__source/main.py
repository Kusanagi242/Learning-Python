import pygame
from define import *
from player import Player
from ball import Ball


WINDOW_GAME = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # Frame dimension
pygame.display.set_caption("GAME PING PONG")
# Load icon 
pygame.display.set_icon(pygame.image.load(PATH_IMAGES + 'Logo.png')) # show the icon(import icon)

# FUNCTION: Event
def key_events():
    global run, window_color # global variable

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT -> hit the icon red color to close the frame
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("UP")
                playerRight.move_up()
            if event.key == pygame.K_DOWN:
                print("DOWN")
                playerRight.move_down()
            if event.key == pygame.K_w:
                print("W")
                playerLeft.move_up()
            if event.key == pygame.K_s:
                print("S")
                playerLeft.move_down()
                
# Initialize player
playerLeft  = Player(COLOR_RED, 0, (WINDOW_HEIGHT//2 - PLAYER_HEIGHT//2))
playerRight = Player(COLOR_BLUE, (WINDOW_WIDTH - PLAYER_WIDTH), (WINDOW_HEIGHT//2 - PLAYER_HEIGHT//2))

# Initialize ball
ball = Ball(COLOR_BROWN, WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

FPS = 60
run = True
window_color = COLOR_GREEN

clock = pygame.time.Clock()

while run:
    clock.tick(FPS)
    WINDOW_GAME.fill(window_color)

    # Call Key Event function
    key_events()

    # Draw a Line 
    pygame.draw.line(WINDOW_GAME, COLOR_BLACK, start_pos = (WINDOW_WIDTH/2, 0), end_pos = (WINDOW_WIDTH/2, WINDOW_HEIGHT), width =  LINE_WIDTH)

    # Draw player left
    playerLeft.show(WINDOW_GAME)
    # Draw player right
    playerRight.show(WINDOW_GAME)
    
    # draw the ball
    ball.show(WINDOW_GAME)
    ball.move()
    ball.handle_collision(playerLeft, playerRight)

    # Update interface
    pygame.display.update() 

pygame.quit()
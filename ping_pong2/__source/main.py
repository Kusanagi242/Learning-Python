import pygame
import os

pygame.init()


WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Load icon 
PATH_DIRECTORY = os.path.dirname(__file__)
PATH_IMAGES = os.path.join(PATH_DIRECTORY, 'image/')
pygame.display.set_icon(pygame.image.load(PATH_IMAGES + 'Logo.png')) # show the icon(import icon)

FPS = 60

# COLOR LIST
COLOR_WHITE     = (255, 255, 255)
COLOR_BLACK     = (  0,   0,   0)

COLOR_YELLOW    = (241, 227,   9)
COLOR_RED       = (255,   0,   0)
COLOR_GREEN     = (  0, 255,   0)
COLOR_BLUE      = (  0,   0, 255)
COLOR_GREY      = (154, 154, 150) 

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS = 7

SCORE_FONT = pygame.font.SysFont("comicsans", 50)
WINNING_SCORE = 2

class Paddle:
    # COLOR = COLOR_WHITE
    VEL = 4

    # Default object - paddle
    def __init__(self, x, y, width, height, color):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height
        self.color = color
    
    # draw the player on the window
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    # Move the paddle - player
    def move(self, up = True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

    # Reset the paddle
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y

class Ball:
    MAX_VEL = 10
    COLOR = COLOR_GREEN

    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)
    
    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1 # change the direction when reset the ball

        
def draw(win, paddles, ball, left_score, right_score):
    win.fill(COLOR_BLACK) # add color to the screen

    # draw the scores into the wwindow
    left_score_text = SCORE_FONT.render(f"{left_score}", 1, COLOR_YELLOW)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, COLOR_YELLOW)
    win.blit(left_score_text, (WIDTH//4 - left_score_text.get_width() // 2, 20))
    win.blit(right_score_text, (WIDTH * (3/4) - right_score_text.get_width() // 2, 20))
    
    # draw the list of paddles 
    for paddle in paddles:
        paddle.draw(win)
    
    # draw middle dassh line in window
    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(surface= win, color= COLOR_GREY, rect= (WIDTH // 2 - 3, i, 6, HEIGHT//20)) 
        # win: where to draw | color | WIDTH//2 -5: left 
        # | i: top | 10: width | HEIGHT // 2 : height

    # draw the ball into the window
    ball.draw(win)

    pygame.display.update()

def handle_collision(ball, left_paddle, right_paddle):
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1 # change direction of the ball
    elif ball.y - ball.radius <=0:
        ball.y_vel *= -1
    # Check ball hitting the left-right paddle
    if ball.x_vel < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1 
                # ball move following y direction
                middle_y = left_paddle.y + left_paddle.height /2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel

    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1
                # ball move following y direction
                middle_y = right_paddle.y + right_paddle.height /2
                difference_in_y = middle_y - ball.y
                reduction_factor =  (right_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel


def handle_paddle_movement(keys, left_paddle, right_paddle):
    # Left paddle movement
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:
        left_paddle.move(up = True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.height + left_paddle.VEL <= HEIGHT:
        left_paddle.move(up = False)
    # Right paddle movement
    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
        right_paddle.move(up = True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.height + right_paddle.VEL <= HEIGHT:
        right_paddle.move(up = False)

def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(x= 10, y= (HEIGHT//2 - PADDLE_HEIGHT//2), width= PADDLE_WIDTH, height= PADDLE_HEIGHT, color= COLOR_RED)
    right_paddle = Paddle(x= (WIDTH - PADDLE_WIDTH - 10), y= (HEIGHT//2 - PADDLE_HEIGHT//2), width= PADDLE_WIDTH, height= PADDLE_HEIGHT, color= COLOR_BLUE)
    ball = Ball(x= WIDTH//2, y= HEIGHT//2,radius= BALL_RADIUS)

    left_score = 0
    right_score = 0


    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        # Press key
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys = keys, left_paddle= left_paddle, right_paddle= right_paddle)
        
        ball.move()
        handle_collision(ball= ball, left_paddle= left_paddle, right_paddle= right_paddle)

        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > WIDTH:
            left_score += 1
            ball.reset()

        won = False
        # Check winning score
        if left_score >= WINNING_SCORE:
            won = True
            win_text = "Left Player Won"
        elif right_score >= WINNING_SCORE:
            won = True
            win_text = "Right Player Won"

        if won:
            # Show the winning anouncement
            text = SCORE_FONT.render(win_text, 1, COLOR_WHITE)
            WIN.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(3000) # delay 5000ms
            ball.reset()
            right_paddle.reset()
            left_paddle.reset()
        
    pygame.quit()

if __name__ == '__main__':
    main()



import pygame
import time

# initialize imported pygame modules
pygame.init()

# create the window for the game to be played in, tuple is in pixels
win_width = 800
win_length = 600
window = pygame.display.set_mode((win_width, win_length))
pygame.display.set_caption('Snake Game by Max')

# Variables for the colors used in the game
white = (255, 255, 255)
snake_green = (10, 252, 123)
red = (255, 0, 0)

# boolean to keep the state of game in it, playing vs not
game_over = False

# starting position value for snake
x1 = win_width/2
y1 = win_length/2

snake_block = 10

x1_change = 0  # initialize to 0 for both variables
y1_change = 0

clock = pygame.time.Clock()
snake_speed = 30

font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [win_width/2, win_length/2])


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If 'X' is clicked in the window, window will close
            game_over = True  # parameters of draw.rect are [x place, y place, x size of block, y size of block]
        if event.type == pygame.KEYDOWN:  # Detect if key is pressed down
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block  # The number for each change corresponds to the speed of the snake in game
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -snake_block  # negative because top left of window is (0,0) and bottom right is (800,600)
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = snake_block
    # Check location of snake head. If the head reaches out of bounds of the window then the game ends
    if x1 >= win_width or x1 < 0 or y1 >= win_length or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    window.fill(white)
    pygame.draw.rect(window, snake_green, [x1, y1, snake_block, snake_block])  # Draws a green square, in the center of the window

    pygame.display.update()

    clock.tick(30)

# Display you lost in red for 2 seconds before closing
message("You lost", red)
pygame.display.update()
time.sleep(2)

# uninitialised all pygame modules

pygame.quit()
quit()
import pygame
import time
import random

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
blue = (0, 0, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)

snake_block = 10
snake_speed = 25

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, snake_green, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [win_width / 9, win_length / 3])


def gameLoop():
    game_over = False
    game_close = False

    # starting position value for snake
    x1 = win_width / 2
    y1 = win_length / 2

    x1_change = 0  # initialize to 0 for both variables
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, win_width - snake_block) / 10.0) * 10
    foody = round(random.randrange(0, win_length - snake_block) / 10.0) * 10

    while not game_over:

        while game_close:
            window.fill(white)
            message("You lost. Press Q-Quit or C-Play again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

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
            game_close = True

        x1 += x1_change
        y1 += y1_change
        window.fill(white)

        # Draws food blocks randomly
        pygame.draw.rect(window, blue, [foodx, foody, snake_block, snake_block])

        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)

        clock.tick(snake_speed)
        pygame.display.update()

        if int(x1) == foodx and int(y1) == foody:
            foodx = round(random.randrange(0, win_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, win_length - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    # uninitialised all pygame modules

    pygame.quit()
    quit()


gameLoop()

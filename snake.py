import pygame

# initialize imported pygame modules
pygame.init()

# create the window for the game to be played in, tuple is in pixels
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake Game by Max')

# Variables for the colors used in the game
white = (255, 255, 255)
snake_green = (10, 252, 123)
food_color = (255, 0, 0)

# boolean to keep the state of game in it, playing vs not
game_over = False

# starting position value for snake
x1 = 400
y1 = 300

x1_change = 0  # initialize to 0 for both variables
y1_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If 'X' is clicked in the window, window will close
            game_over = True  # parameters of draw.rect are [x place, y place, x size of block, y size of block]
        if event.type == pygame.KEYDOWN:  # Detect if key is pressed down
            if event.key == pygame.K_LEFT:
                x1_change = -10  # The number for each change corresponds to the speed of the snake in game
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10  # negative because top left of window is (0,0) and bottom right is (800,600)
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10

    x1 += x1_change
    y1 += y1_change
    window.fill(white)
    pygame.draw.rect(window, snake_green, [x1, y1, 10, 10])  # Draws a green square, in the center of the window

    pygame.display.update()

    clock.tick(30)

# uninitialize all pygame modules
pygame.quit()
quit()
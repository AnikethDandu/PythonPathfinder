import pygame
import a_star

from colors import WHITE, RED, BLACK, GREEN

# Initialize PyGame
pygame.init()

# Create the 2D array representing the grid with defined size
ROWS, COLS = (25, 25)
GRID = [[0 for x in range(ROWS)] for y in range(COLS)]

# Set up the screen
SCREEN_SIZE = (ROWS * 25, COLS * 25)
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
SCREEN.fill(WHITE)


# Creates a rectangle with the specified size and position
def return_grid_square(x, y, length):
    return pygame.rect.Rect(x, y, length, length)


# Initialize the grid square sizes
RECT_LENGTH = SCREEN_SIZE[0] // ROWS
RECT_WIDTH = 2

program_running = True

START = [2, 7]
END = [15, 13]

a_star.x_pos = START[0]
a_star.y_pos = START[1]

# Game loop
while program_running:

    # Forces loop to execute 10 times per second
    pygame.time.Clock().tick(10)

    for event in pygame.event.get():
        # Stop the program if the x button is clicked
        if event.type == pygame.QUIT:
            program_running = False

    # Draw the grid
    for x in range(ROWS):
        for y in range(COLS):
            pygame.draw.rect(SCREEN, BLACK, return_grid_square(RECT_LENGTH * x, RECT_LENGTH * y, RECT_LENGTH),
                             RECT_WIDTH)

    # Draw the starting point and endpoint
    pygame.draw.rect(SCREEN, GREEN, return_grid_square(START[0] * 25, START[1] * 25, RECT_LENGTH))
    pygame.draw.rect(SCREEN, RED, return_grid_square(END[0] * 25, END[1] * 25, RECT_LENGTH), 2)

    # Updates screen
    pygame.display.flip()

    if not a_star.finished:
        a_star.find_path(SCREEN, END[0], END[1])
        pygame.time.wait(100)

# Stop the program once the user closes the window
pygame.quit()

import pygame

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
def return_grid_square(x_pos, y_pos, length):
    return pygame.rect.Rect(x_pos, y_pos, length, length)


# Initialize the grid square sizes
RECT_LENGTH = SCREEN_SIZE[0] // ROWS
RECT_WIDTH = 2

program_running = True

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
    pygame.draw.rect(SCREEN, GREEN, return_grid_square(25, 25, RECT_LENGTH))
    pygame.draw.rect(SCREEN, RED, return_grid_square(325, 325, RECT_LENGTH))

    # Updates screen
    pygame.display.flip()

# Stop the program once the user closes the window
pygame.quit()

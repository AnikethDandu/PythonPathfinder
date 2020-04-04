import pygame
import a_star
import dijkstra

from colors import WHITE, RED, BLACK, GREEN, BLUE

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

# Program loop variable
program_running = True

# TODO: Add ability for user to place start and end
# Pre-defined start and end
START = (1, 2)
END = (12, 5)

# TODO: Add ability for user to place obstacles
# Pre-defined obstacles
GRID[5][5] = 1
GRID[6][5] = 1
GRID[7][5] = 1
GRID[8][5] = 1
GRID[8][6] = 1
GRID[8][7] = 1
GRID[8][8] = 1
GRID[8][9] = 1
GRID[7][9] = 1
GRID[6][9] = 1
GRID[5][9] = 1
GRID[0][15] = 1
GRID[0][22] = 1
GRID[1][22] = 1
GRID[2][22] = 1
GRID[2][23] = 1
GRID[10][5] = 1
GRID[10][4] = 1
GRID[10][6] = 1
GRID[10][7] = 1
GRID[10][8] = 1
GRID[10][3] = 1
GRID[10][2] = 1
GRID[10][13] = 1
GRID[9][13] = 1
GRID[8][13] = 1
GRID[7][13] = 1
GRID[11][13] = 1
GRID[12][13] = 1
GRID[6][13] = 1
GRID[5][13] = 1
GRID[14][13] = 1
GRID[15][13] = 1
GRID[13][13] = 1


# Find path
a_star.find_path(GRID, START, END)

# Game loop
while program_running:

    # Forces loop to execute 10 times per second
    pygame.time.Clock().tick(10)

    for event in pygame.event.get():
        # Stop the program if the x button is clicked
        if event.type == pygame.QUIT:
            program_running = False
    # Draw the empty grid
    for x in range(ROWS):
        for y in range(COLS):
            pygame.draw.rect(SCREEN, BLACK, return_grid_square(RECT_LENGTH * x, RECT_LENGTH * y, RECT_LENGTH),
                             RECT_WIDTH)
    # Draw start and end
    pygame.draw.rect(SCREEN, GREEN, return_grid_square(START[0] * 25+2, START[1] * 25+2, RECT_LENGTH-3))
    pygame.draw.rect(SCREEN, RED, return_grid_square(END[0] * 25, END[1] * 25, RECT_LENGTH), 4)
    # Draw obstacles
    for x in range(25):
        for y in range(25):
            if GRID[x][y] == 1:
                pygame.draw.rect(SCREEN, BLACK, return_grid_square(x*25, y*25, RECT_LENGTH))
    # Updates screen
    pygame.display.flip()
    # Draw path
    a_star.draw_path(SCREEN)


# Stop the program once the user closes the window
pygame.quit()

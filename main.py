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


# Initialize the grid square sizes
RECT_LENGTH = SCREEN_SIZE[0] // ROWS
RECT_WIDTH = 2

# Program loop variable
program_running = True

# Pre-defined start and end
START = (0, 0)
END = (24, 24)


# Creates a rectangle with the specified size and position
def return_node(x, y, length):
    return pygame.rect.Rect(x, y, length, length)


# Draw the grid and obstacles
def draw_grid():
    for x in range(ROWS):
        for y in range(COLS):
            if GRID[x][y] == 1:
                pygame.draw.rect(SCREEN, BLACK, return_node(x * 25, y * 25, RECT_LENGTH))
            else:
                pygame.draw.rect(SCREEN, BLACK, return_node(RECT_LENGTH * x, RECT_LENGTH * y, RECT_LENGTH),
                                 RECT_WIDTH)


# For each node, if it is an obstacle, draw an obstacle
# Else, draw an empty node
def clear_board():
    for x in range(ROWS):
        for y in range(COLS):
            if GRID[x][y] == 1:
                pygame.draw.rect(SCREEN, BLACK, return_node(x * 25, y * 25, RECT_LENGTH))
            else:
                pygame.draw.rect(SCREEN, WHITE, return_node(x * 25, y * 25, RECT_LENGTH))


# Set the start to a new specified position and clear the node where the previous start location was
def set_start(x, y):
    global START
    pygame.draw.rect(SCREEN, WHITE, return_node(START[0] * 25, START[1] * 25, RECT_LENGTH))
    START = (x, y)


# Set the end to a new specified position and clear the node where the previous end location was
def set_end(x, y):
    global END
    pygame.draw.rect(SCREEN, WHITE, return_node(END[0] * 25, END[1] * 25, RECT_LENGTH))
    END = (x, y)


# Find the path and draw the display it
def find_path():
    while not a_star.found_path:
        a_star.find_path(GRID, START, END)
    while a_star.found_path:
        a_star.draw_path(SCREEN)


# Game loop
while program_running:
    # Forces loop to execute 10 times per second
    pygame.time.Clock().tick(10)

    for event in pygame.event.get():
        # Stop the program if the x button is clicked
        if event.type == pygame.QUIT:
            program_running = False
        # Draw an obstacle if the mouse left button is clicked
        # Remove an obstacle if the mouse right button is clicked and an obstacle exists in the chosen position
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x //= 25
            y //= 25
            # If the left mouse button is clicked
            if event.button == 1:
                GRID[x][y] = 1
                pygame.draw.rect(SCREEN, BLACK, return_node(x * 25, y * 25, RECT_LENGTH))
            # If the right mouse button is clicked
            if event.button == 3:
                if GRID[x][y] == 1:
                    GRID[x][y] = 0
                    pygame.draw.rect(SCREEN, WHITE, return_node(x * 25, y * 25, RECT_LENGTH))
        if event.type == pygame.KEYDOWN:
            x, y = pygame.mouse.get_pos()
            x //= 25
            y //= 25
            # Change the position of the start node when the s key is pressed to the mouse location
            if event.key == pygame.K_s:
                set_start(x, y)
            # Change the position of the end node when the e key is pressed to the mouse location
            if event.key == pygame.K_e:
                set_end(x, y)
            # Clear the board of the path when the c key is pressed
            if event.key == pygame.K_c:
                clear_board()
            # Find and draw the path when the space bar is pressed
            if event.key == pygame.K_SPACE:
                clear_board()
                find_path()

    # Draw board
    draw_grid()

    # Draw start and end
    pygame.draw.rect(SCREEN, GREEN, return_node(START[0] * 25 + 2, START[1] * 25 + 2, RECT_LENGTH - 3))
    pygame.draw.rect(SCREEN, RED, return_node(END[0] * 25, END[1] * 25, RECT_LENGTH), 4)

    # Updates screen
    pygame.display.flip()

# Stop the program once the user closes the window
pygame.quit()

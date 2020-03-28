import pygame
import math

x_pos = 0
y_pos = 0
finished = False


def find_path(screen, end_x, end_y):
    global x_pos
    global y_pos
    # If the endpoint is not reached yet
    if x_pos != end_x or y_pos != end_y:
        surrounding_nodes = [
            [x_pos + 1, y_pos],
            [x_pos + 1, y_pos + 1],
            [x_pos + 1, y_pos - 1],
            [x_pos, y_pos + 1],
            [x_pos, y_pos - 1],
            [x_pos - 1, y_pos],
            [x_pos - 1, y_pos + 1],
            [x_pos - 1, y_pos - 1]
        ]
        # Initialize minimum cost and next node
        min_total_cost = 100000
        next_node = [0][0]
        # Find the g,h, and f-cost for each surrounding node
        for node in surrounding_nodes:
            g_cost = 0
            h_cost = 0
            # Find the x and y distances from the start and end
            x_g = math.fabs(node[0] - x_pos)
            y_g = math.fabs(node[1] - y_pos)
            x_h = math.fabs(node[0] - end_x)
            y_h = math.fabs(node[1] - end_y)
            # Determine the g-cost (distance away from start)
            if x_g == 1 and y_g == 1:
                g_cost = 14
            if x_g == 1:
                g_cost = 10
            if y_g == 1:
                g_cost = 10
            # Determine the h-cost (distance away from end)
            while x_h > 0 or y_h > 0:
                if x_h > 0 and y_h > 0:
                    x_h -= 1
                    y_h -= 1
                    h_cost += 14
                if x_h > 0:
                    x_h -= 1
                    h_cost += 10
                if y_h > 0:
                    y_h -= 1
                    h_cost += 10
            # Determine the total cost of moving to the node
            f_cost = g_cost + h_cost
            # Find the lowest-cost move
            if f_cost < min_total_cost:
                min_total_cost = f_cost
                next_node = node
        # Set the starting position to the next node
        x_pos = next_node[0]
        y_pos = next_node[1]
        # Draw the move
        pygame.draw.rect(screen, (0, 0, 255), (x_pos * 25, y_pos * 25, 25, 25))
    else:
        # Finish the algorithm
        print("Target Reached")
        global finished
        finished = True

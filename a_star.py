# A-STAR ALGORITHM

import pygame
from node import Node
from colors import YELLOW, BLUE

open_list = []
closed_list = []
path = []
finished_path = False


# Find path and use parents of nodes to determine path
def find_path(grid, start, end):
    global open_list
    global closed_list
    start = Node(previous=Node(position=start), position=start)
    end = Node(previous=Node(position=end), position=end)
    # Algorithm has not visited start so add it to OPEN list
    open_list.append(start)
    while True:
        # Find node with lowest f-cost (best move) and add it to CLOSED (visited) list
        current_node = find_lowest_f_cost(start, end)
        closed_list.append(current_node)
        # If the current node node is the end node
        if current_node.position == end.position:
            # Create the path by tracing the previous node of each node that has been visited
            end.previous = current_node
            closed_list.append(end)
            calculate_path(end, start)
            break
        # Find the neighbors of the current node
        neighbors = return_node_neighbors(grid, current_node)
        # For each neighbor of the current node: If the neighbor is already in the OPEN (not visited) list and there
        # is a faster way to get there, remove the node
        # If the neighbor is in the CLOSED (visited) list and there is a faster way to get there, remove the node
        # If the neighbor is not in the OPEN or CLOSED list, add it to the OPEN list
        # and set it's previous node to the current node
        for neighbor in neighbors:
            place_holder_node = neighbor
            neighbor.calculate_costs(start, end)
            place_holder_node.calculate_costs(current_node, end)
            cost = current_node.g_cost + place_holder_node.g_cost
            if neighbor in open_list and cost < neighbor.g_cost:
                open_list.remove(neighbor)
            if neighbor in closed_list and cost < neighbor.g_cost:
                closed_list.remove(neighbor)
            if neighbor not in open_list and neighbor not in closed_list:
                neighbor.g_cost = cost
                open_list.append(neighbor)
                neighbor.previous = current_node


# Return node with lowest f_cost in list of nodes not visited yet
def find_lowest_f_cost(start, end):
    minimum_f_cost = 1000000
    lowest_node = Node(position=(0, 0))
    for node in open_list:
        node.calculate_costs(start, end)
        if node.f_cost < minimum_f_cost:
            minimum_f_cost = node.f_cost
            lowest_node.position = node.position
    return open_list.pop(open_list.index(lowest_node))


# Return nodes surrounding given node that exist inside of grid and are not an obstacle
def return_node_neighbors(grid, node):
    surrounding_nodes = [
        Node(position=(node.position[0] + 1, node.position[1])),
        Node(position=(node.position[0] + 1, node.position[1] + 1)),
        Node(position=(node.position[0] + 1, node.position[1] - 1)),
        Node(position=(node.position[0], node.position[1] + 1)),
        Node(position=(node.position[0], node.position[1] - 1)),
        Node(position=(node.position[0] - 1, node.position[1])),
        Node(position=(node.position[0] - 1, node.position[1] + 1)),
        Node(position=(node.position[0] - 1, node.position[1] - 1)),
    ]
    surrounding_nodes = [node for node in surrounding_nodes if
                         25 > node.position[0] >= 0 and 25 > node.position[1] >= 0]
    return list([node for node in surrounding_nodes if grid[node.position[0]][node.position[1]] != 1])


# Draw path chosen by algorithm
def draw_path(screen):
    global finished_path
    if len(open_list) > 0:
        node = open_list.pop(0)
        pygame.draw.rect(screen, BLUE, (node.position[0] * 25, node.position[1] * 25, 25, 25))
    else:
        if len(closed_list) == 0:
            finished_path = True
    if len(closed_list) > 0:
        node = closed_list.pop(0)
        pygame.draw.rect(screen, (0, 200, 255), (node.position[0] * 25, node.position[1] * 25, 25, 25))
    else:
        if len(open_list) == 0:
            finished_path = True
    if finished_path:
        if len(path) > 0:
            node = path.pop()
            pygame.draw.rect(screen, YELLOW, (node.position[0] * 25, node.position[1] * 25, 25, 25))


# Add to path list using previous node position of current node
def calculate_path(node, start):
    if node.position == start.position:
        return
    path.append(node.previous)
    calculate_path(node.previous, start)

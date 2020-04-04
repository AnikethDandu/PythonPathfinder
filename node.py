import math


class Node:
    # Initialize the node with a parent (default: None), position (default: (0, 0)), and g, h, and f costs
    def __init__(self, previous=None, position=(0, 0), distance=math.inf):
        self.previous = previous
        self.position = position
        self.distance = distance
        self.g_cost = 0
        self.h_cost = 0
        self.f_cost = 0

    # Return if this node is equal to another node (based on position)
    def __eq__(self, other):
        return self.position == other.position

    # Calculate g-cost (cost of moving from previous node to current node: 10 = straight, 14 = diagonal)
    # Calculate h-cost (cost of moving from current node to end)
    # Calculate f-cost (g(n) + h(n) where n is current node)
    def calculate_costs(self, start, end):
        x_dist = abs(self.position[0] - start.position[0])
        y_dist = abs(self.position[1] - start.position[1])
        if x_dist == 1 and y_dist == 1:
            self.g_cost = 14
        else:
            self.g_cost = 10
        x_dist = abs(self.position[0] - end.position[0])
        y_dist = abs(self.position[1] - end.position[1])
        self.h_cost = 10*math.sqrt(math.pow(x_dist, 2) + math.pow(y_dist, 2))
        self.f_cost = self.g_cost + self.h_cost

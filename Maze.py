import math
import random
from queue import PriorityQueue
import matplotlib.pyplot as plt
import numpy as np

"""
All code designed and written by
Troy Chibbaro – tbc41
Rishi Jammalamadaka - rj433

Each of us contributed an equal amount work via virtual collaboration.
"""


#iterate through a row and use blocking/unblocking probability
def set_blocked_unblocked(row):
    for i in range(len(row)):
        num = random.uniform(0, 1)
        row[i] = 0 if num > 0.3 else 1


#Check if point is out of bounds
def out_of_bounds(x, y, size):
    return x < 0 or x >= size or y < 0 or y >= size


#Return number of neighbors on fire
def get_num_neighbors_on_fire(grid, cell):
    size = len(grid[0])
    neighbor_positions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    count = 0
    for curX, curY in neighbor_positions:
        posX, posY = cell[0] + curX, cell[1] + curY
        if not out_of_bounds(posX, posY, size):
            # Found neighbor on fire
            if grid[posX][posY] == 2:
                count += 1
    return count


#Object to store current point, parent, and heuristic data. heuristic is ONLY used by agent 3
class AStarRoutePoint:
    def __init__(self, pos, parent):
        #Store parent and position
        self.parent = parent
        self.x, self.y = pos

        #Store heuristics and f value of estimated path cost
        self.f = 0
        self.distance_traveled = 0

    #Comparator for priority queue
    def __lt__(self, other):
        return self.f < other.f


#Our implementation of the A* search algorithm
def a_star_search(grid, start, end):
    #Create priority queue and store starting point
    queue = PriorityQueue()
    queue.put(AStarRoutePoint((start[0], start[1]), None))

    size = len(grid[0])

    #Store visited cells
    visited = []

    #Loop until queue is empty
    while not queue.empty():
        #De-queue the highest priority and mark it as visited
        current = queue.get()

        #Make sure we haven't gone this point yet
        if (current.x, current.y) in visited:
            continue

        #Now, we've visited
        visited.append((current.x, current.y))

        #Goal found, iterate through all parents and return route
        if current.x == end[0] and current.y == end[1]:
            res = [current]
            temp = current.parent
            while temp:
                res.append(temp)
                temp = temp.parent
            res.reverse()
            return res

        #Goal not found, add neighbors to queue
        #We only define neighbors to be cardinal directions, as we want to ensure
        #this path exists for agents to go through only using up left right and down
        for neighbor in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            pos = (neighbor[0] + current.x, neighbor[1] + current.y)

            if not out_of_bounds(pos[0], pos[1], size):
                #verify neighbor is not on fire or a wall
                data = grid[pos[0]][pos[1]] == 0
                if pos not in visited and grid[pos[0]][pos[1]] == 0:
                    #Create AStarRoutePoint object
                    cell = AStarRoutePoint(pos, current)

                    #Compute f using heuristic, heuristic being manhattan distance.
                    #Then, place into queue.
                    cell.f = (current.distance_traveled + 1) + (abs(pos[0] - end[0]) + abs(pos[1] - end[1]))
                    queue.put(cell)

    #if no path is found in loop, return empty route
    return []


def can_reach_center(grid, size):
    #Store midpoint
    mp = size//2

    # Call A* on each of four corners
    uleft = a_star_search(grid, (0, 0), (mp, mp))
    uright = a_star_search(grid, (size-1, 0), (mp, mp))
    bleft = a_star_search(grid, (0, size-1), (mp, mp))
    bright = a_star_search(grid, (size-1, size-1), (mp, mp))

    if uleft and uright and bleft and bright:
        return True
    return False


class Maze:
    #Constructor stores modifier and maze size
    def __init__(self, fire_modifier=0.5, mazeSize=51):
        self.fire_modifier = fire_modifier
        self.mazeSize = mazeSize
        while True:
            # First, initialize whole grid with blocked/unblocked spaces
            grid = []
            for x in range(mazeSize):
                grid.append([0] * mazeSize)
                set_blocked_unblocked(grid[x])

            # Unblock corners
            grid[0][0] = 0
            grid[0][self.mazeSize-1] = 0
            grid[self.mazeSize-1][0] = 0
            grid[self.mazeSize-1][self.mazeSize-1] = 0

            # verify path to center from corners
            if can_reach_center(grid, self.mazeSize):
                # Fire started in center
                grid[self.mazeSize//2][self.mazeSize//2] = 2
                self.grid = grid
                break
            else:
                #print("Bad maze, creating a new one")
                continue

    #Spread fire using equation from writeup and get num neighbors on fire
    def spread_fire(self):
        for x in range(self.mazeSize):
            for y in range(self.mazeSize):
                # Only spread fire to open spaces, not walls
                if self.grid[x][y] == 0:
                    if random.uniform(0, 1) < 1 - math.pow(1 - self.fire_modifier, get_num_neighbors_on_fire(self.grid, (x, y))):
                        self.grid[x][y] = 2


    #return a copy of the maze with fire spread 3 timesteps in the future.
    def return_simulation(self, runs=3):
        grid_copy = [r[:] for r in self.grid]
        for _ in range(runs):
            for x in range(len(grid_copy)):
                for y in range(len(grid_copy[0])):
                    # Only spread fire to open spaces, not walls
                    if grid_copy[x][y] == 0:
                        if random.uniform(0, 1) < 1 - math.pow(1 - self.fire_modifier, get_num_neighbors_on_fire(grid_copy, (x, y))):
                            grid_copy[x][y] = 2
        return grid_copy



    #return plot of the grid
    def plot_grid(self):
        plt.imshow(self.grid, cmap="Paired")
        plt.xticks(np.arange(-0.5, self.mazeSize+0.5, step=1))
        plt.yticks(np.arange(self.mazeSize-1.5, -1.5, step=-1))
        plt.show()


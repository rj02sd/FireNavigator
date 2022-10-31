from Maze import a_star_search

"""
All code designed and written by
Troy Chibbaro – tbc41
Rishi Jammalamadaka - rj433

Each of us contributed an equal amount work via virtual collaboration.
"""


#Ensure point not out of bounds
def out_of_bounds(x, y, size):
    return x < 0 or x >= size or y < 0 or y >= size


#check if reachable
def walkable(grid, x, y):
    return grid[x][y] == 0


#returns a route planned by A* search
def plan_route(grid, start, end):
    return a_star_search(grid, start, end)

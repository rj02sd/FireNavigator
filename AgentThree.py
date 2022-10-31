from Maze import Maze
from routing import plan_route
"""
All code designed and written by
Troy Chibbaro – tbc41
Rishi Jammalamadaka - rj433

Each of us contributed an equal amount work via virtual collaboration.
"""


class AgentThree:
    def __init__(self, maze, starting_corner=(0, 0), target_destination=(0,0)):
        #Store start position and the maze
        self.curX, self.curY = starting_corner
        self.maze = maze
        grid_size = len(maze.grid[0])
        if(target_destination[0]==0 & target_destination[1]==0 & starting_corner[0]==0 & starting_corner[1]==0):
            self.destination = (grid_size - 1, grid_size - 1)
        else:
            self.destination = target_destination

    def move(self):
        #Store all cells where agent moved
        moved_to = [(0, 0)]

        #plan route with A* search
        route_current = plan_route(self.maze.grid, (self.curX, self.curY), self.destination)
        route_current = route_current[1:]

        #While agent is not on fire
        while self.maze.grid[self.curX][self.curY] != 2:
            #Store simulation route
            future_maze = self.maze.return_simulation()
            route_future = plan_route(future_maze, (self.curX, self.curY), self.destination)
            route_future = route_future[1:]

            #If our future route cannot reach destination, we still attempt to move through current route
            if(len(route_future) == 0):
                route_current = plan_route(self.maze.grid, (self.curX, self.curY), self.destination)
                route_current = route_current[1:]
                if(len(route_current) ==0):
                    #print("Agent can't proceed further, destination cant be reached")
                    moved_to.append((self.curX, self.curY))
                    for t in moved_to:
                        self.maze.grid[t[0]][t[1]] = 4
                    self.maze.grid[self.curX][self.curY] = 3
                    return False
                self.curX = route_current[0].x
                self.curY = route_current[0].y
                route_current = route_current[1:]
                moved_to.append((self.curX, self.curY))
                continue
            

            #Move to selected cell and store remainder of route
            self.curX = route_future[0].x
            self.curY = route_future[0].y
            moved_to.append((self.curX, self.curY))
            
            route_current = route_future[1:]

            
            #Check if agent reached dest. if not, spread fire
            if (self.curX, self.curY) == self.destination:
                for t in moved_to:
                    self.maze.grid[t[0]][t[1]] = 4
                #print("Agent reached destination")
                self.maze.grid[self.curX][self.curY] = 3
                return True
            else:
                self.maze.spread_fire()

        #print("Agent burned at point ", (self.curX, self.curY))
        for t in moved_to:
            self.maze.grid[t[0]][t[1]] = 4
        self.maze.grid[self.curX][self.curY] = 3
        return False

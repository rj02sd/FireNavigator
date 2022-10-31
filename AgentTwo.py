from routing import plan_route

"""
All code designed and written by
Troy Chibbaro – tbc41
Rishi Jammalamadaka - rj433

Each of us contributed an equal amount work via virtual collaboration.
"""


class AgentTwo:
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

        # Call plan route to return a route, skip first step
        route = plan_route(self.maze.grid, (self.curX, self.curY), self.destination)
        route = route[1:]

        #While agent is not on fire
        while self.maze.grid[self.curX][self.curY] != 2:
            for point in route:
                #Found point on current route on fire, route around fire
                if self.maze.grid[point.x][point.y] == 2:
                    route = plan_route(self.maze.grid, (self.curX, self.curY), self.destination)
                    if len(route) == 0:
                        #print("Agent can't proceed further, destination cant be reached")
                        moved_to.append((self.curX, self.curY))
                        for t in moved_to:
                            self.maze.grid[t[0]][t[1]] = 4
                        self.maze.grid[self.curX][self.curY] = 3
                        return False
                    break

            #Move to selected cell
            self.curX = route[0].x
            self.curY = route[0].y
            moved_to.append((self.curX, self.curY))

            route = route[1:]
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

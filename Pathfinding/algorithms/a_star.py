from queue import PriorityQueue
from utils import h
from node import Node
from grid import Grid


class AStar:
    def __init__(self, grid: list[list[Node]]):
        '''
        The AStar class is the class that implements the A* algorithm.
        It is used to find the shortest path between two nodes.

        Args:
            * grid (list[list[Node]]) - The grid of nodes.
        '''

        self.grid = grid
        
        self.running = False
        self.start = None
        self.end = None
        self.count = 0
        self.open_set = PriorityQueue()
        self.open_set_hash = {}
        self.came_from = {}


    def reset(self):
        '''
        Reset all attributes of the algorithm by calling the __init__ function.
        '''
            
        self.__init__(self.grid)


    def run(self, grid: Grid) -> bool:
        '''
        Run this function to start the algorithm.

        Args:
            * grid (Grid) - The grid of nodes.

        Returns:
            * bool - True on success, False on failure.
        '''

        try:
            self.start = grid.getNodeByType('start')[0]
            self.end = grid.getNodeByType('end')[0]
        except IndexError:
            print('No start or end node found.')
            return False


        self.open_set.put((self.start.f_score, self.count, self.start))
        self.open_set_hash = {self.start}

        self.start.g_score = 0
        self.start.f_score = h(self.start.pos(), self.end.pos())

        self.running = True
        return True


    def reconstruct_path(self):
        '''
        Reconstruct the path from the end node to the start node.
        '''

        current = self.end

        while current != self.start:
            current = self.came_from[current]
            current.type = 'path' if current.type != 'start' else 'start'


    def update(self):
        '''
        Update the algorithm. This function is called every frame.
        '''

        if not self.running: return
        if self.open_set.empty():
            self.running = False
            return

        current = self.open_set.get()[2]
        self.open_set_hash.remove(current)

        if current == self.end:
            self.running = False
            self.reconstruct_path()
            print(self.start.type, self.end.type)
            return

        for neighbour in current.neighbours:
            neighbour_temp_g_score = current.g_score + 1

            if neighbour_temp_g_score < neighbour.g_score:
                self.came_from[neighbour] = current
                neighbour.g_score = neighbour_temp_g_score
                neighbour.f_score = neighbour.g_score + h(neighbour.pos(), self.end.pos())

                if neighbour not in self.open_set_hash:
                    self.open_set.put((neighbour.f_score, self.count, neighbour))
                    self.open_set_hash.add(neighbour)
                    self.count += 1
                    neighbour.type = 'open' if neighbour.type != 'end' else 'end'

        if current != self.start:
            current.type = 'closed'

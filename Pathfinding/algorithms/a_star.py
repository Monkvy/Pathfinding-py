import pygame
from node import Node


class AStar:
    def __init__(self, grid: list[list[Node]]):
        '''
        The AStar class is the class that implements the A* algorithm.
        It is used to find the shortest path between two nodes.

        Args:
            * grid (list[list[Node]]) - The grid of nodes.
        '''

        self.grid = grid

    def update(self):
        pass
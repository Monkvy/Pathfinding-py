import pygame
from node import Node


class Grid:
    def __init__(self, rows: int, columns: int, node_size: int=20, node_margin: int=1):
        '''
        The Grid class is the class that represents the grid.

        Args:
            * rows (int) - The amount of rows in the grid.
            * columns (int) - The amount of columns in the grid.
            * node_size (int, optional) - The size of the nodes.
            * node_margin (int, optional) - The margin between the nodes.
        '''
        
        self.rows = rows
        self.columns = columns
        self.node_size = node_size
        self.node_margin = node_margin

        self.content = []
        for row in range(rows):
            self.content.append([])
            for column in range(columns):
                self.content[row].append(Node(row, column))


    def getNode(self, row: int, column: int) -> Node:
        '''
        Get the node at the given position.

        Args:
            * row (int) - The row of the node.
            * column (int) - The column of the node.

        Returns:
            * Node - The node at the given position.
        '''

        return self.content[row][column]

    
    def getNodeByType(self, type: str) -> list:
        '''
        Get all nodes with the given type.

        Args:
            * type (str) - The type of the nodes.

        Returns:
            * list - A list of nodes with the given type.
        '''

        return [node for row in self.content for node in row if node.type == type]
    

    def reset(self):
        '''
        Reset the grid by calling the __init__ method.
        '''

        self.__init__(self.rows, self.columns, self.node_size, self.node_margin)


    def draw(self, surface: pygame.Surface):
        '''
        Draw the grid.
        '''

        for row in self.content:
            for node in row:
                node.draw(surface, self.node_size, self.node_margin)
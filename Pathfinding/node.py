import pygame


class Node:
    colors = {
        'idle': pygame.Color('white'),
        'barrier': pygame.Color('black'),
        'start': pygame.Color('orange'),
        'end': pygame.Color('turquoise'),
        'path': pygame.Color('purple'),
        'open': pygame.Color('green'),
        'closed': pygame.Color('red')
    }

    def __init__(self, row: int, column: int):
        '''
        The Node class is the class that represents a single node in the grid.
        All possible node types are defined in the Node.colors dictionary.

        Args:
            * row (int) - The row of the node.
            * column (int) - The column of the node.
        '''

        self.row = row
        self.column = column
        self.type = 'idle'
        self.neighbours = []
        self.g_score = float('inf')
        self.h_score = float('inf')
        self.f_score = 0


    def pos(self) -> tuple:
        '''
        Return the position of the node.

        Returns:
            * (tuple) - The position of the node.
        '''
        
        return self.row, self.column


    def updateNeighbors(self, grid):
        '''
        Update the neighbours of the node.

        Args:
            * grid (Grid) - The grid that the node is part of.
        '''
        
        self.neighbours = []

        # Down
        if (self.row < grid.rows - 1) and (grid.getNode(self.row + 1, self.column).type != 'barrier'):
            self.neighbours.append(grid.getNode(self.row + 1, self.column))

        # Up
        if (self.row > 0) and (grid.getNode(self.row - 1, self.column).type != 'barrier'):
            self.neighbours.append(grid.getNode(self.row - 1, self.column))

        # Right
        if (self.column < grid.columns - 1) and (grid.getNode(self.row, self.column + 1).type != 'barrier'):
            self.neighbours.append(grid.getNode(self.row, self.column + 1))
        
        # Left
        if (self.column > 0) and (grid.getNode(self.row, self.column - 1).type != 'barrier'):
            self.neighbours.append(grid.getNode(self.row, self.column - 1))


    def drawOutline(self, surface: pygame.Surface, size: int, margin: int, color: pygame.Color):
        '''
        Draw the outline of the node.

        Args:
            * surface (pygame.Surface) - The surface to draw on.
            * size (int) - The size of the node.
            * margin (int) - The margin between the nodes.
            * color (pygame.Color) - The color of the outline.
        '''

        x = self.column * (size + margin) - margin
        y = self.row * (size + margin) - margin

        pygame.draw.rect(surface, color, (x, y, size + margin * 2, size + margin * 2), 1)


    def draw(self, surface: pygame.Surface, size: int, margin: int):
        '''
        Draw the node on the surface.

        Args:
            * surface (pygame.Surface) - The surface to draw on.
            * size (int) - The size of the node.
            * margin (int) - The margin between the nodes.
        '''

        # Calculate the position of the node in pixels based on the size of the node.
        x = self.column * (size + margin)
        y = self.row * (size + margin)

        # Draw the node.
        pygame.draw.rect(surface, Node.colors[self.type], (x, y, size, size))


    def __lt__(self, other):
        return False

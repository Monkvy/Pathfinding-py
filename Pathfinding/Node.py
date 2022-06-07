import pygame


class Node:
    def __init__(self):
        '''
        The Node class is the class that represents a single node in the grid.
        '''

        self.type = 'none'
        self.neighbours = []
        self.g_score = 0
        self.h_score = 0
        self.f_score = 0

    def closed(self):
        pass

    def draw(self, surface: pygame.Surface):
        pass


import pygame


class Node:
    def __init__(self):
        self.type = 'none'
        self.g_cost = 0
        self.h_cost = 0
        self.f_cost = 0

    def draw(self, surface: pygame.Surface):
        pass


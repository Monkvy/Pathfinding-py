import pygame


class Node:
    def __init__(self):
        self.type = 'none'
        self.g_score = 0
        self.h_score = 0
        self.f_score = 0

    def draw(self, surface: pygame.Surface):
        pass


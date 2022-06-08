import pygame
from grid import Grid
from algorithms import *
from utils import clickedGridPos


class Application:
    def __init__(self, title: str, rows: int, columns: int, node_size: int=20, node_margin: int=1):
        '''
        The application class is the main class of the program.

        Args:
            * title (str) - The title of the window.
            * rows (int) - The amount of rows in the grid.
            * columns (int) - The amount of columns in the grid.
            * node_size (int, optional) - The size of the nodes.
            * node_margin (int, optional) - The margin between the nodes.
        '''

        # Initialize pygame
        pygame.init()

        # Create a window
        self.screen = pygame.display.set_mode((columns * node_size + (columns + 1) * node_margin, rows * node_size + (rows + 1) * node_margin))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(title)

        # Running flag
        self.running = True

        # This flag is used to determine if the user has started the visualisation.
        self.started = False

        # Every node is part of a grid
        self.grid = Grid(rows, columns, node_size, node_margin)

        # The current algorithm
        self.algorithm = AStar(self.grid)


    def run(self):
        '''
        Run this function to start the main loop.
        '''

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # Create a new node
                if pygame.mouse.get_pressed()[0] and not self.started:
                    # Get the position of the mouse click
                    node_pos = clickedGridPos(event.pos, self.grid)
                    node = self.grid.getNode(node_pos[1], node_pos[0])

                    # Only create nodes if the user has selected a empty node
                    if node.type == 'idle':

                        # If the grid does not contain a start node, create one
                        if not any(node.type == 'start' for row in self.grid.content for node in row):
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                node.type = 'start'
                        
                        # If the grid does not contain an end node, create one
                        elif not any(node.type == 'end' for row in self.grid.content for node in row):
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                node.type = 'end'

                        # If the grid already contains a start and end node, create a barrier
                        else: node.type = 'barrier'
                
                # Remove a node
                elif pygame.mouse.get_pressed()[2] and not self.started:
                    node_pos = clickedGridPos(event.pos, self.grid)
                    node = self.grid.getNode(node_pos[1], node_pos[0])
                    node.type = 'idle'

                # Start the visualisation
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if not self.started:
                            self.started = True
                            
                            # Update the neighbours of every node
                            for row in self.grid.content:
                                for node in row:
                                    node.updateNeighbors(self.grid)
                            
                            # Start the algorithm
                            if not self.algorithm.run(self.grid): self.started = False
                        
                        else:
                            self.started = False
                            self.algorithm.reset()
                            self.grid.reset()


            # Execute the algorithm
            self.algorithm.update()


            self.screen.fill((0, 0, 0))
            self.grid.draw(self.screen)

            # Fps & display
            pygame.display.flip()
            pygame.display.set_caption(f'{self.algorithm.__class__.__name__} - {"Running" if self.algorithm.running else "Stopped"}')
            self.clock.tick(60)
            

        # Cleanup
        pygame.quit()
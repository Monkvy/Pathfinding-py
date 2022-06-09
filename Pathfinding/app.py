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

        # All tools (the tool at index 0 is the current tool)
        self.tools = ['start', 'end', 'barrier', 'move']

        # Variable for node the user is currently moving
        self.moving_node = None


    def run(self):
        '''
        Run this function to start the main loop.
        '''

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                mouse_pos = pygame.mouse.get_pos()

                # Create a new node
                if pygame.mouse.get_pressed()[0] and not self.started:
                    # Get the position of the mouse click
                    node_pos = clickedGridPos(mouse_pos, self.grid)
                    node = self.grid.getNode(node_pos[1], node_pos[0])

                    # Only create nodes if the user has selected a empty node
                    if node.type == 'idle':
                        match self.tools[0]:

                            # Create start node
                            case 'start':
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if len(self.grid.getNodeByType('start')) > 0:
                                        self.grid.getNodeByType('start')[0].type = 'idle'
                                    node.type = 'start'
                            
                            # Create end node
                            case 'end':
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if len(self.grid.getNodeByType('end')) > 0:
                                        self.grid.getNodeByType('end')[0].type = 'idle'
                                    node.type = 'end'

                            # Create a barrier
                            case 'barrier': 
                                node.type = 'barrier'

                # Move a node
                if pygame.mouse.get_pressed()[0] and (self.tools[0] == 'move'):
                    node_pos = clickedGridPos(mouse_pos, self.grid)
                    node = self.grid.getNode(node_pos[1], node_pos[0])

                if (event.type == pygame.MOUSEBUTTONDOWN) and (self.moving_node == None):
                    node_pos = clickedGridPos(mouse_pos, self.grid)
                    node = self.grid.getNode(node_pos[1], node_pos[0])

                    # Only move nodes if the user has selected a node
                    if (event.button == 1) and (node.type != 'idle') and (self.tools[0] == 'move'):
                        self.moving_node = node
                
                if (event.type == pygame.MOUSEBUTTONUP) and (self.moving_node != None):
                    node_pos = clickedGridPos(mouse_pos, self.grid)
                    node = self.grid.getNode(node_pos[1], node_pos[0])

                    # Only move nodes if the user has selected a node
                    if event.button == 1:
                        if node.type == 'idle':
                            node.type = self.moving_node.type
                            self.moving_node.type = 'idle'
                        self.moving_node = None
                
                # Remove a node
                elif pygame.mouse.get_pressed()[2] and not self.started:
                    node_pos = clickedGridPos(mouse_pos, self.grid)
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
                            self.algorithm.running = not self.algorithm.running

                    elif event.key == pygame.K_r:
                        self.started = False
                        self.algorithm.reset()
                        self.grid.reset()

                    # Switch tools
                    elif event.key == pygame.K_UP:
                        # Append the current tool to the end of the list and remove the first element (the current tool)
                        self.tools.append(self.tools.pop(0))
                    elif event.key == pygame.K_DOWN:
                        # Append the current tool to the start of the list and remove the last element (the current tool)
                        self.tools.insert(0, self.tools.pop())


            # Reset the moving node to avoid bugs
            if self.tools[0] != 'move':
                self.moving_node = None


            # Execute the algorithm
            self.algorithm.update()

            self.screen.fill((0, 0, 0))
            self.grid.draw(self.screen)

            # Draw outlines if the user is moving a node
            if self.moving_node != None:
                self.moving_node.drawOutline(self.screen, self.grid.node_size, self.grid.node_margin, (0, 255, 0))
                
                # Draw the outline of the node, the user is moving to
                node_pos = clickedGridPos(mouse_pos, self.grid)
                node = self.grid.getNode(node_pos[1], node_pos[0]).drawOutline(self.screen, self.grid.node_size, self.grid.node_margin, (0, 255, 0))


            # Fps & display
            pygame.display.flip()
            pygame.display.set_caption(f'{self.algorithm.__class__.__name__} - {"Running" if self.algorithm.running else "Stopped"}')
            self.clock.tick(60)
            

        # Cleanup
        pygame.quit()
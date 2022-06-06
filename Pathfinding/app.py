import pygame


class Application:
    def __init__(self, title: str, width: int, height: int):
        '''
        The application class is the main class of the program.

        Args:
            * title (str) - The title of the window.
            * width (int) - The width of the window.
            * height (int) - The height of the window.
        '''

        # Initialize pygame
        pygame.init()

        # Create a window
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(title)

        # Running flag
        self.running = True


    def run(self):
        '''
        Run this function to start the main loop.
        '''

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))

            # Fps & display
            pygame.display.flip()
            self.clock.tick(60)
            

        # Cleanup
        pygame.quit()
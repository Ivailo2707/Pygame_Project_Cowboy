import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.running = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_SPACE:
                    print("Space key pressed")

    def run(self):
        self.running = True
        while self.running:
            self.handle_events()
            # Update game logic
            # Draw game graphics
            pygame.display.flip()

        pygame.quit()

game = Game()
game.run()
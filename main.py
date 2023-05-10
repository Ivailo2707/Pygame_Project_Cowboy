import pygame
import os

WIDTH, HEIGHT = 1100, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cowboy shooter")

FPS = 60


DESERT = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Desert.png')), (WIDTH, HEIGHT))

def draw_window():
    WIN.blit(DESERT, (0, 0))

    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    while(run):
        clock.tick(FPS)
        for event in pygame.event.get(): #checks if window is closed
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        draw_window()
    main()

if __name__ == "__main__":
    main()
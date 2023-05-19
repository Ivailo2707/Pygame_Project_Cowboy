import pygame
import os
from Player1 import Player1

WIDTH, HEIGHT = 1100, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cowboy shooter")

FPS = 60

PLAYER_1_IMAGE = pygame.image.load(os.path.join('Assets', 'Player_1.png'))

P1 = Player1(WIDTH/2 - 60, 600, 100, 160, PLAYER_1_IMAGE)

DESERT = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Desert.png')), (WIDTH, HEIGHT))



def draw_window():
    WIN.blit(DESERT, (0, 0))
    P1.draw(WIN)
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    while(run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        P1.handle_movement()
        draw_window()
    main()

if __name__ == "__main__":
    main()
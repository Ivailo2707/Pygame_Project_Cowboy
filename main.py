import pygame
import os
from Player1 import Player1
from Player2 import Player2
from Bullet_Controller import Bullet_Controller

WIDTH, HEIGHT = 1100, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cowboy shooter")

FPS = 60

PLAYER_1_IMAGE = pygame.image.load(os.path.join('Assets', 'Player_1.png'))
PLAYER_2_IMAGE = pygame.image.load(os.path.join('Assets', 'Player_2.png'))

P1 = Player1(WIDTH/2 - 60, 600, 100, 160, PLAYER_1_IMAGE)
P2 = Player2(WIDTH/2 - 60, 100, 80, 100, PLAYER_2_IMAGE)

DESERT = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Desert.png')), (WIDTH, HEIGHT))

def draw_window():
    WIN.blit(DESERT, (0, 0))
    P1.draw(WIN)
    P2.draw(WIN)
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    BuCtrl = Bullet_Controller()
    while(run):
        clock.tick(FPS)
        BuCtrl.shoot(run)
        P1.handle_movement()
        P2.handle_movement()
        draw_window()
    main()

if __name__ == "__main__":
    main()
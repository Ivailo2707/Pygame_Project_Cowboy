import pygame
import os
from Player1 import Player1
from Player2 import Player2
from Game_Controller import Game_Controller
from Cactus_cover import Cactus_Cover


pygame.font.init()

WIDTH, HEIGHT = 1100, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cowboy shooter")

PLAYER_1_IMAGE = pygame.image.load(os.path.join('Assets', 'Player_1.png'))
PLAYER_2_IMAGE = pygame.image.load(os.path.join('Assets', 'Player_2.png'))
CACTUS_IMAGE = pygame.image.load(os.path.join('Assets', 'cactus.png'))

P1 = Player1(WIDTH/2 - 60, 600, 100, 130, PLAYER_1_IMAGE)
P2 = Player2(WIDTH/2 - 60, 100, 80, 100, PLAYER_2_IMAGE)
GaCtrl = Game_Controller()
SIDE_1_COVER_1 = Cactus_Cover(WIDTH - 900, HEIGHT - 350, 120, 60, CACTUS_IMAGE)
SIDE_1_COVER_2 = Cactus_Cover(WIDTH - 600, HEIGHT - 350, 120, 60, CACTUS_IMAGE)
SIDE_1_COVER_3 = Cactus_Cover(WIDTH - 200, HEIGHT - 400, 120, 60, CACTUS_IMAGE)

DESERT = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Desert.png')), (WIDTH, HEIGHT))

def draw_window():
    WIN.blit(DESERT, (0, 0))
    P1.draw_health(WIN, GaCtrl.get_1_curr_health())
    P2.draw_health(WIN, GaCtrl.get_2_curr_health())
    if SIDE_1_COVER_1.get_status():
        SIDE_1_COVER_1.draw(WIN)

    elif not SIDE_1_COVER_1.get_status():
        background_rect = pygame.Rect(WIDTH - 900, HEIGHT - 300, 120, 60)
        WIN.blit(DESERT, (WIDTH - 900, HEIGHT - 300), background_rect)

    if SIDE_1_COVER_2.get_status():
        SIDE_1_COVER_2.draw(WIN)

    elif not SIDE_1_COVER_2.get_status():
        background_rect = pygame.Rect(WIDTH - 900, HEIGHT - 300, 120, 60)
        WIN.blit(DESERT, (WIDTH - 900, HEIGHT - 300), background_rect)

    if SIDE_1_COVER_3.get_status():
        SIDE_1_COVER_3.draw(WIN)

    elif not SIDE_1_COVER_3.get_status():
        background_rect = pygame.Rect(WIDTH - 900, HEIGHT - 300, 120, 60)
        WIN.blit(DESERT, (WIDTH - 900, HEIGHT - 300), background_rect)


    P1.draw(WIN)
    P2.draw(WIN)
    GaCtrl.draw_bullets(WIN)
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    while (run):
        clock.tick(60)
        GaCtrl.game(WIN)
        P1.handle_movement()
        P2.handle_movement()
        draw_window()
    

if __name__ == "__main__":
    main()
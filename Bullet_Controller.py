import pygame
import os
from Player1 import Player1
from Player2 import Player2

PLAYER_1_IMAGE = pygame.image.load(os.path.join('Assets', 'Player_1.png'))
PLAYER_2_IMAGE = pygame.image.load(os.path.join('Assets', 'Player_2.png'))
WIDTH, HEIGHT = 1100, 800

class Bullet_Controller:
    def __init__(self):
        self.__P1 = Player1(WIDTH/2 - 60, 600, 100, 160, PLAYER_1_IMAGE)
        self.__P2 = Player2(WIDTH/2 - 60, 100, 80, 100, PLAYER_2_IMAGE)
        self.__P1_bullets = []
        self.__P2_bullets = []

    def shoot(self, run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(self.__P1_bullets) < 3:
                    bullet = pygame.Rect(WIDTH/2 + 100, 648, 10, 5)
                    self.__P1_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(self.__P2_bullets) < 3:
                    bullet = pygame.Rect(WIDTH/2, 148, 10, 5)
                    self.__P2_bullets.append(bullet)
        
        print(self.__P1_bullets, self.__P2_bullets)
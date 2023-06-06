import pygame
import os
from Player1 import Player1
from Player2 import Player2
from Cactus_cover import Cactus_Cover
from Bullet_Controller import Bullet_Controller
from Cactus_Damage_Controller import Cactus_Damage_Control
from Draw_Controller import Draw_Controller

PLAYER_1_IMAGE = pygame.image.load(os.path.join('Assets', 'Player_1.png'))
PLAYER_2_IMAGE = pygame.image.load(os.path.join('Assets', 'Player_2.png'))
WIDTH, HEIGHT = 1100, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cowboy shooter")
CACTUS_IMAGE = pygame.image.load(os.path.join('Assets', 'cactus.png'))


class Game_Controller:
    def __init__(self):
        self._P1 = Player1(WIDTH/2 - 60, 600, 100, 160, PLAYER_1_IMAGE)
        self._P2 = Player2(WIDTH/2 - 60, 100, 80, 100, PLAYER_2_IMAGE)
        self._P1_bullets = []
        self._P2_bullets = []
        self._cover_1_1 = Cactus_Cover(WIDTH - 900, HEIGHT - 300, 120, 60, CACTUS_IMAGE)
        self._cover_1_2 = Cactus_Cover(WIDTH - 600, HEIGHT - 350, 120, 60, CACTUS_IMAGE)
        self._cover_1_3 = Cactus_Cover(WIDTH - 200, HEIGHT - 400, 120, 60, CACTUS_IMAGE)
        self._cover_2_1 = Cactus_Cover(WIDTH - 900, HEIGHT - 550, 120, 60, CACTUS_IMAGE)
        self._cover_2_2 = Cactus_Cover(WIDTH - 600, HEIGHT - 600, 120, 60, CACTUS_IMAGE)
        self._cover_2_3 = Cactus_Cover(WIDTH - 200, HEIGHT - 650, 120, 60, CACTUS_IMAGE)
        self._Bullet_Ctrl = Bullet_Controller(self._P1_bullets, self._P2_bullets, self._P1, self._P2, self._cover_1_1, self._cover_1_2, self._cover_1_3, self._cover_2_1, self._cover_2_2, self._cover_2_3)
        self._cactus_damage_ctrl = Cactus_Damage_Control(self._cover_1_1, self._cover_1_2, self._cover_1_3, self._cover_2_1, self._cover_2_2, self._cover_2_3, self._P1, self._P2)
        self._Draw_Ctrl = Draw_Controller(self._cover_1_1, self._cover_1_2, self._cover_1_3, self._cover_2_1, self._cover_2_2, self._cover_2_3, self._P1, self._P2, self._Bullet_Ctrl)

    


    def game(self):
        run = True
        clock = pygame.time.Clock()
        while(run):
            clock.tick(60)
            self._P1.handle_movement()
            self._P2.handle_movement()

            if self._cover_1_1.get_health() <= 0:
                self._cover_1_1.remove()

            if self._cover_1_2.get_health() <= 0:
                self._cover_1_2.remove()

            if self._cover_1_3.get_health() <= 0:
                self._cover_1_3.remove()

            if self._cover_2_1.get_health() <= 0:
                self._cover_2_1.remove()

            if self._cover_2_2.get_health() <= 0:
                self._cover_2_2.remove()

            if self._cover_2_3.get_health() <= 0:
                self._cover_2_3.remove()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()


                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LCTRL and len(self._P1_bullets) < 3:
                        bullet = pygame.Rect(self._P1.get_x() + self._P1.get_width()//2, self._P1.get_y(), 10, 5)
                        self._P1_bullets.append(bullet)

                    if event.key == pygame.K_RCTRL and len(self._P2_bullets) < 3:
                        bullet = pygame.Rect(self._P2.get_x(), self._P2.get_y() + 50, 10, 5)
                        self._P2_bullets.append(bullet)

            
                self._cactus_damage_ctrl.take_damage_on_colision(event)
                self._Bullet_Ctrl.hit(event)

            winner_text = ""
            if self._P2.get_health() <= 0:
                winner_text = "Player 1 wins!"
            if self._P1.get_health() <= 0:
                winner_text = "Player 2 wins!"

            if winner_text != "":
                self._Draw_Ctrl.draw_winner(winner_text)
                pygame.quit()
        
            self._cactus_damage_ctrl.handle_cactus_colissions()
            self._Bullet_Ctrl.handle_bullets()
            self._P1.handle_movement()
            self._P2.handle_movement()
            self._Draw_Ctrl.draw_window() 
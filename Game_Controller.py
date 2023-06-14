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
CACTUS_IMAGE = pygame.image.load(os.path.join('Assets', 'cactus.png'))

pygame.mixer.init()

class Game_Controller:
    def __init__(self):
        self._P1 = Player1(WIDTH/2 - 60, 600, 100, 160, PLAYER_1_IMAGE)
        self._P2 = Player2(WIDTH/2 - 60, 100, 80, 100, PLAYER_2_IMAGE)
        self._covers = [
            Cactus_Cover(WIDTH - 900, HEIGHT - 300, 120, 60, CACTUS_IMAGE),
            Cactus_Cover(WIDTH - 600, HEIGHT - 350, 120, 60, CACTUS_IMAGE),
            Cactus_Cover(WIDTH - 200, HEIGHT - 400, 120, 60, CACTUS_IMAGE),
            Cactus_Cover(WIDTH - 900, HEIGHT - 550, 120, 60, CACTUS_IMAGE),
            Cactus_Cover(WIDTH - 600, HEIGHT - 600, 120, 60, CACTUS_IMAGE),
            Cactus_Cover(WIDTH - 200, HEIGHT - 650, 120, 60, CACTUS_IMAGE)
        ]
        self._Bullet_Ctrl = Bullet_Controller(self._P1, self._P2, self._covers)
        self._cactus_damage_ctrl = Cactus_Damage_Control(self._covers, self._P1, self._P2)
        self._Draw_Ctrl = Draw_Controller(self._covers, self._P1, self._P2, self._Bullet_Ctrl)

    def game(self):
        timer = 0
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            timer += clock.get_time()

            self._P1.handle_movement()
            self._P2.handle_movement()

            for cover in self._covers:
                if cover.get_health() <= 0:
                    cover.remove()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

                self._P1.shoot(event)
                self._P2.shoot(event)
                self._Bullet_Ctrl.hit(event)

            winner_text = ""
            if self._P2.get_health() <= 0:
                winner_text = "Player 1 wins!"
                sound = pygame.mixer.Sound(os.path.join('Assets', 'player1_wins.mp3'))
            if self._P1.get_health() <= 0:
                winner_text = "Player 2 wins!"
                sound = pygame.mixer.Sound(os.path.join('Assets', 'player2_wins.mp3'))

            if timer >= 121000:
                winner_text = "Draw!"

            if winner_text != "":
                sound.play()
                self._Draw_Ctrl.draw_winner(winner_text)
                pygame.quit()

            self._cactus_damage_ctrl.handle_cactus_collisions()
            self._Bullet_Ctrl.handle_bullets()
            self._P1.handle_movement()
            self._P2.handle_movement()
            self._Draw_Ctrl.draw_window(timer)

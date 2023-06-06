import pygame
import os

pygame.font.init()

PLAYER_1_IMAGE = pygame.image.load(os.path.join('Assets', 'Player_1.png'))
PLAYER_2_IMAGE = pygame.image.load(os.path.join('Assets', 'Player_2.png'))
WIDTH, HEIGHT = 1100, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cowboy shooter")
CACTUS_IMAGE = pygame.image.load(os.path.join('Assets', 'cactus.png'))

class Draw_Controller:
    def __init__(self, cover_1_1, cover_1_2, cover_1_3, cover_2_1, cover_2_2, cover_2_3, P1, P2, Bullet_Controller):
        self._DESERT = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Desert.png')), (WIDTH, HEIGHT))
        self._cover_1_1 = cover_1_1
        self._cover_1_2 = cover_1_2
        self._cover_1_3 = cover_1_3
        self._cover_2_1 = cover_2_1
        self._cover_2_2 = cover_2_2
        self._cover_2_3 = cover_2_3
        self._P1 = P1
        self._P2 = P2
        self._Bullet_Ctrl = Bullet_Controller
        self._caput_m = (35, 15, 13)
        self._winner_font = pygame.font.SysFont('comicsans', 100)

    def draw_winner(self, text):
        winner_text = self._winner_font.render(text, 1, self._caput_m)
        WIN.blit(winner_text, (WIDTH/2 - winner_text.get_width()/2, HEIGHT/2 - winner_text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(5000)
    
    def draw_window(self):
        WIN.blit(self._DESERT, (0, 0))
        self._P1.draw_health(WIN, self._P1.get_health())
        self._P2.draw_health(WIN, self._P2.get_health())
        if self._cover_1_1.get_status():
            self._cover_1_1.draw(WIN)

        if self._cover_1_2.get_status():
            self._cover_1_2.draw(WIN)

        if self._cover_1_3.get_status():
            self._cover_1_3.draw(WIN)

        elif not self._cover_1_3.get_status():
            background_rect = pygame.Rect(WIDTH - 200, HEIGHT - 400, 120, 60)
            WIN.blit(self._DESERT, (WIDTH - 200, HEIGHT - 400), background_rect)

        if self._cover_2_1.get_status():
            self._cover_2_1.draw(WIN)

        elif not self._cover_2_1.get_status():
            background_rect = pygame.Rect(WIDTH - 900, HEIGHT - 550, 120, 60)
            WIN.blit(self._DESERT, (WIDTH - 900, HEIGHT - 550), background_rect)

        if self._cover_2_2.get_status():
            self._cover_2_2.draw(WIN)

        elif not self._cover_2_2.get_status():
            background_rect = pygame.Rect(WIDTH - 600, HEIGHT - 600, 120, 60)
            WIN.blit(self._DESERT, (WIDTH - 600, HEIGHT - 600), background_rect)

        if self._cover_2_3.get_status():
            self._cover_2_3.draw(WIN)

        elif not self._cover_2_3.get_status():
            background_rect = pygame.Rect(WIDTH - 200, HEIGHT - 650, 120, 60)
            WIN.blit(self._DESERT, (WIDTH - 200, HEIGHT - 650), background_rect)

        self._P1.draw(WIN)
        self._P2.draw(WIN)
        self._Bullet_Ctrl.draw_bullets(WIN)
        pygame.display.update()
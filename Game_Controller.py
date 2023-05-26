import pygame
import os
from Player1 import Player1
from Player2 import Player2

PLAYER_1_IMAGE = pygame.image.load(os.path.join('Assets', 'Player_1.png'))
PLAYER_2_IMAGE = pygame.image.load(os.path.join('Assets', 'Player_2.png'))
WIDTH, HEIGHT = 1100, 800

class Game_Controller:
    def __init__(self):
        self._P1 = Player1(WIDTH/2 - 60, 600, 100, 160, PLAYER_1_IMAGE)
        self._P2 = Player2(WIDTH/2 - 60, 100, 80, 100, PLAYER_2_IMAGE)
        self._P1_bullets = []
        self._P2_bullets = []
        self._BVEL = 8
        self._BULLET_1_IMAGE = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'bullet.png')), 180)
        self._BULLET_2_IMAGE = pygame.image.load(os.path.join('Assets', 'bullet.png'))
        self._P1_HIT = pygame.USEREVENT + 1
        self._P2_HIT = pygame.USEREVENT + 2
        self._P1_UPDATED_HEALTH = 10
        self._P2_UPDATED_HEALTH = 10

    def handle_bullets(self):
        for bullet in self._P1_bullets:
            bullet.y -= self._BVEL
            if self._P2.get_rect().colliderect(bullet):
                pygame.event.post(pygame.event.Event(self._P2_HIT))
                self._P1_bullets.remove(bullet)
            elif bullet.y < 0:
                self._P1_bullets.remove(bullet)

        for bullet in self._P2_bullets:
            bullet.y += self._BVEL
            if self._P1.get_rect().colliderect(bullet):
                pygame.event.post(pygame.event.Event(self._P1_HIT))
                self._P2_bullets.remove(bullet)
            elif bullet.y > HEIGHT:
                self._P2_bullets.remove(bullet)


    def draw_bullets(self, window):
        bullet_width = 15
        bullet_height = 25  

        for bullet in self._P1_bullets:
            bullet_rect = pygame.Rect(bullet[0], bullet[1], bullet_width, bullet_height)
            bullet_image_scaled = pygame.transform.scale(self._BULLET_1_IMAGE, (bullet_width, bullet_height))
            window.blit(bullet_image_scaled, bullet_rect)

        for bullet in self._P2_bullets:
            bullet_rect = pygame.Rect(bullet[0], bullet[1], bullet_width, bullet_height)
            bullet_image_scaled = pygame.transform.scale(self._BULLET_2_IMAGE, (bullet_width, bullet_height))
            window.blit(bullet_image_scaled, bullet_rect)


    def game(self):
        self._P1.handle_movement()
        self._P2.handle_movement()
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

            if event.type == self._P2_HIT:
                self._P2_UPDATED_HEALTH = self._P2.take_normal_damage()

            if event.type == self._P1_HIT:
                self._P1_UPDATED_HEALTH = self._P1.take_normal_damage()
            

        winner_text = ""
        if self._P2.get_health() <= 0:
            winner_text = "Player 1 wins!"
        if self._P1.get_health() <= 0:
            winner_text = "Player 2 wins!"

        if winner_text != "":
            pass

        self.handle_bullets()

    def get_1_curr_health(self):
        return self._P1_UPDATED_HEALTH

    def get_2_curr_health(self):
        return self._P2_UPDATED_HEALTH
       
import pygame
import os
from Cactus_cover import Cactus_Cover
from Player1 import Player1
from Player2 import Player2

WIDTH, HEIGHT = 1100, 800
CACTUS_IMAGE = pygame.image.load(os.path.join('Assets', 'cactus.png'))

class Bullet_Controller:
    def __init__(self, P1_bullets, P2_bullets, P1, P2, cover_1_1, cover_1_2, cover_1_3, cover_2_1, cover_2_2, cover_2_3):
        self._BVEL = 8
        self._P1_HIT = pygame.USEREVENT + 7
        self._CACTUS_SIDE_1_NUM_1_HIT = pygame.USEREVENT + 8
        self._CACTUS_SIDE_1_NUM_2_HIT = pygame.USEREVENT + 9
        self._CACTUS_SIDE_1_NUM_3_HIT = pygame.USEREVENT + 10
        self._P2_HIT = pygame.USEREVENT + 11
        self._CACTUS_SIDE_2_NUM_1_HIT = pygame.USEREVENT + 12
        self._CACTUS_SIDE_2_NUM_2_HIT = pygame.USEREVENT + 13
        self._CACTUS_SIDE_2_NUM_3_HIT = pygame.USEREVENT + 14
        self._P1_bullets = P1_bullets
        self._P2_bullets = P2_bullets
        self._BULLET_1_IMAGE = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'bullet.png')), 180)
        self._BULLET_2_IMAGE = pygame.image.load(os.path.join('Assets', 'bullet.png'))
        self._cover_1_1 = cover_1_1
        self._cover_1_2 = cover_1_2
        self._cover_1_3 = cover_1_3
        self._cover_2_1 = cover_2_1
        self._cover_2_2 = cover_2_2
        self._cover_2_3 = cover_2_3
        self._P1 = P1
        self._P2 = P2

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


    def handle_bullets(self):
        for bullet in self._P1_bullets:
            bullet.y -= self._BVEL
            if self._P2.get_rect().colliderect(bullet):
                pygame.event.post(pygame.event.Event(self._P2_HIT))
                self._P1_bullets.remove(bullet)
            elif self._cover_1_1.get_obstacle_rect().colliderect(bullet):
                if self._cover_1_1.get_status():
                    pygame.event.post(pygame.event.Event(self._CACTUS_SIDE_1_NUM_1_HIT))
                    self._P1_bullets.remove(bullet)
                else:
                    pass
            
            elif self._cover_1_2.get_obstacle_rect().colliderect(bullet):
                if self._cover_1_2.get_status():
                    pygame.event.post(pygame.event.Event(self._CACTUS_SIDE_1_NUM_2_HIT))
                    self._P1_bullets.remove(bullet)
                else:
                    pass
                
            elif self._cover_1_3.get_obstacle_rect().colliderect(bullet):
                if self._cover_1_3.get_status():
                    pygame.event.post(pygame.event.Event(self._CACTUS_SIDE_1_NUM_3_HIT))
                    self._P1_bullets.remove(bullet)
                else:
                    pass

            elif self._cover_2_1.get_obstacle_rect().colliderect(bullet):
                if self._cover_2_1.get_status():
                    pygame.event.post(pygame.event.Event(self._CACTUS_SIDE_2_NUM_1_HIT))
                    self._P1_bullets.remove(bullet)
                else:
                    pass
                
            elif self._cover_2_2.get_obstacle_rect().colliderect(bullet):
                if self._cover_2_2.get_status():
                    pygame.event.post(pygame.event.Event(self._CACTUS_SIDE_2_NUM_2_HIT))
                    self._P1_bullets.remove(bullet)
                else:
                    pass

            elif self._cover_2_3.get_obstacle_rect().colliderect(bullet):
                if self._cover_2_3.get_status():
                    pygame.event.post(pygame.event.Event(self._CACTUS_SIDE_2_NUM_3_HIT))
                    self._P1_bullets.remove(bullet)
                else:
                    pass

            elif bullet.y < 0:
                self._P1_bullets.remove(bullet)

        for bullet in self._P2_bullets:
            bullet.y += self._BVEL
            if self._P1.get_rect().colliderect(bullet):
                pygame.event.post(pygame.event.Event(self._P1_HIT))
                self._P2_bullets.remove(bullet)
            elif self._cover_1_1.get_obstacle_rect().colliderect(bullet):
                if self._cover_1_1.get_status():
                    pygame.event.post(pygame.event.Event(self._CACTUS_SIDE_1_NUM_1_HIT))
                    self._P2_bullets.remove(bullet)
                else:
                    pass

            elif self._cover_1_2.get_obstacle_rect().colliderect(bullet):
                if self._cover_1_2.get_status():
                    pygame.event.post(pygame.event.Event(self._CACTUS_SIDE_1_NUM_1_HIT))
                    self._P2_bullets.remove(bullet)
                else:
                    pass
                
            elif self._cover_1_3.get_obstacle_rect().colliderect(bullet):
                if self._cover_1_3.get_status():
                    pygame.event.post(pygame.event.Event(self._CACTUS_SIDE_1_NUM_1_HIT))
                    self._P2_bullets.remove(bullet)
                else:
                    pass
        
            elif self._cover_2_1.get_obstacle_rect().colliderect(bullet):
                if self._cover_2_1.get_status():
                    pygame.event.post(pygame.event.Event(self._CACTUS_SIDE_2_NUM_1_HIT))
                    self._P2_bullets.remove(bullet)
                else:
                    pass
                
            elif self._cover_2_2.get_obstacle_rect().colliderect(bullet):
                if self._cover_2_2.get_status():
                    pygame.event.post(pygame.event.Event(self._CACTUS_SIDE_2_NUM_2_HIT))
                    self._P2_bullets.remove(bullet)
                else:
                    pass

            elif self._cover_2_3.get_obstacle_rect().colliderect(bullet):
                if self._cover_2_3.get_status():
                    pygame.event.post(pygame.event.Event(self._CACTUS_SIDE_2_NUM_3_HIT))
                    self._P2_bullets.remove(bullet)
                else:
                    pass
       

            elif bullet.y > HEIGHT:
                self._P2_bullets.remove(bullet)


    def hit(self, event):
        if event.type == self._P2_HIT:
            self._P2.take_normal_damage()
         
        if event.type == self._P1_HIT:
                self._P1.take_normal_damage()
            
        if event.type == self._CACTUS_SIDE_1_NUM_1_HIT:
                self._cover_1_1.take_bullet_damage()

        if event.type == self._CACTUS_SIDE_1_NUM_2_HIT:
                self._cover_1_2.take_bullet_damage()

        if event.type == self._CACTUS_SIDE_1_NUM_3_HIT:
                self._cover_1_3.take_bullet_damage()

        if event.type == self._CACTUS_SIDE_2_NUM_1_HIT:
                self._cover_2_1.take_bullet_damage()

        if event.type == self._CACTUS_SIDE_2_NUM_2_HIT:
                self._cover_2_2.take_bullet_damage()

        if event.type == self._CACTUS_SIDE_2_NUM_3_HIT:
                self._cover_2_3.take_bullet_damage()


import pygame
import os

pygame.mixer.init()
WIDTH, HEIGHT = 1100, 800

class Bullet_Controller:
    def __init__(self, P1, P2, covers):
        self._BVEL = 8
        self._BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'hit.mp3'))
        self._BULLET_HIT_CACTUS_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'bullet_hit_cactus.mp3'))
        self._P1_HIT = pygame.USEREVENT + 7
        self._P2_HIT = pygame.USEREVENT + 8
        self._CACTUS_HIT_EVENTS = [pygame.USEREVENT + i for i in range(9, 15)]
        self._BULLET_1_IMAGE = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'bullet.png')), 180)
        self._BULLET_2_IMAGE = pygame.image.load(os.path.join('Assets', 'bullet.png'))
        self._covers = covers
        self._P1 = P1
        self._P2 = P2

    def draw_bullets(self, window):
        bullet_width = 15
        bullet_height = 25  

        for bullet in self._P1.get_bullets():
            bullet_rect = pygame.Rect(bullet[0], bullet[1], bullet_width, bullet_height)
            bullet_image_scaled = pygame.transform.scale(self._BULLET_1_IMAGE, (bullet_width, bullet_height))
            window.blit(bullet_image_scaled, bullet_rect)

        for bullet in self._P2.get_bullets():
            bullet_rect = pygame.Rect(bullet[0], bullet[1], bullet_width, bullet_height)
            bullet_image_scaled = pygame.transform.scale(self._BULLET_2_IMAGE, (bullet_width, bullet_height))
            window.blit(bullet_image_scaled, bullet_rect)


    def handle_bullets(self):
        for bullet in self._P1.get_bullets():
            bullet.y -= self._BVEL
            if self._P2.get_rect().colliderect(bullet):
                pygame.event.post(pygame.event.Event(self._P2_HIT))
                self._P1.get_bullets().remove(bullet)
            else:
                for i, cover in enumerate(self._covers):
                    if cover.get_obstacle_rect().colliderect(bullet) and cover.get_status():
                        pygame.event.post(pygame.event.Event(self._CACTUS_HIT_EVENTS[i]))
                        self._P1.get_bullets().remove(bullet)
                        break

            if bullet.y < 0:
                self._P1.get_bullets().remove(bullet)

        for bullet in self._P2.get_bullets():
            bullet.y += self._BVEL
            if self._P1.get_rect().colliderect(bullet):
                pygame.event.post(pygame.event.Event(self._P1_HIT))
                self._P2.get_bullets().remove(bullet)
            else:
                for i, cover in enumerate(self._covers):
                    if cover.get_obstacle_rect().colliderect(bullet) and cover.get_status():
                        pygame.event.post(pygame.event.Event(self._CACTUS_HIT_EVENTS[i]))
                        self._P2.get_bullets().remove(bullet)
                        break

            if bullet.y > HEIGHT:
                self._P2.get_bullets().remove(bullet)

    def hit(self, event):
        if event.type == self._P2_HIT:
            self._P2.take_normal_damage()
            self._BULLET_HIT_SOUND.play()
         
        if event.type == self._P1_HIT:
            self._P1.take_normal_damage()
            self._BULLET_HIT_SOUND.play()

        for i, hit_event in enumerate(self._CACTUS_HIT_EVENTS):
            if event.type == hit_event:
                self._covers[i].take_bullet_damage()
                self._BULLET_HIT_CACTUS_SOUND.play()

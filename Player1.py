import pygame
import os

WIDTH, HEIGHT = 1100, 800

class Player1:
    def __init__(self, x, y, width, height, p1_image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.VEL = 6
        self.p1_image = p1_image
        self.bullets = []
        self.health = 10

    def draw(self, window):
        player_image = pygame.transform.scale(self.p1_image, (self.width, self.height))
        window.blit(player_image ,(self.x, self.y, self.width, self.height))

    def handle_movement(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed [pygame.K_w] and self.y + self.VEL > HEIGHT/2:
            self.y -= self.VEL
        if keys_pressed [pygame.K_a] and self.x + self.VEL > -10:
            self.x -= self.VEL
        if keys_pressed [pygame.K_s] and self.y + self.VEL < 675:
            self.y += self.VEL
        if keys_pressed [pygame.K_d] and self.x + self.VEL < 1030:
            self.x += self.VEL
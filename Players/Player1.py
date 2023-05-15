import pygame
import os

class Player1:
    def __init__(self, P1_IMAGE, PLAYER_1, HEALTH):
        self.WIDTH = 1100
        self.HEIGHT = 800
        self.P_WIDTH = 55
        self.P_HEIGHT = 80
        self.P1_IMAGE = P1_IMAGE
        self.PLAYER_1 = PLAYER_1
        self.health = HEALTH
    def handle_movement(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed [pygame.K_a] and yellow.x - VEL > 0:
            yellow.x -= VEL
        if keys_pressed [pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:
            yellow.x += VEL
        if keys_pressed [pygame.K_w] and yellow.y - VEL > 0:
            yellow.y -= VEL
        if keys_pressed [pygame.K_s] and yellow.y + VEL + yellow.width < HEIGHT:
            yellow.y += VEL
import pygame
import os


class Player1:
    def __init__(self, x, y, width, height, p1_image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.p1_image = p1_image
        self.rect = pygame.Rect(x, y, width, height)
        self.bullets = []
        self.health = 10

    def draw(self, window):
        window.blit(self.p1_image, (self.x, self.y))
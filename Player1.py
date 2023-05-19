import pygame
import os


class Player1:
    def __init__(self, x, y, p1_image):
        self.x = x
        self.y = y
        self.p1_image = p1_image
        self.bullets = []
        self.health = 10

    def draw(self, window):
        window.blit(self.p1_image, (self.x, self.y))
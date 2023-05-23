import pygame
import os

WIDTH, HEIGHT = 1100, 800

class Player1:
    def __init__(self, x, y, width, height, p1_image):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__VEL = 6
        self.__p1_image = p1_image
        self.__health = 10

    def draw(self, window):
        player_image = pygame.transform.scale(self.__p1_image, (self.__width, self.__height))
        window.blit(player_image ,(self.__x, self.__y, self.__width, self.__height))

    def handle_movement(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed [pygame.K_w] and self.__y + self.__VEL > HEIGHT/2:
            self.__y -= self.__VEL
        if keys_pressed [pygame.K_a] and self.__x + self.__VEL > -10:
            self.__x -= self.__VEL
        if keys_pressed [pygame.K_s] and self.__y + self.__VEL < 675:
            self.__y += self.__VEL
        if keys_pressed [pygame.K_d] and self.__x + self.__VEL < 1030:
            self.__x += self.__VEL
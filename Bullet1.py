import pygame


class Bullet1:
    def __init__(self, x, y, width, height, bullet_image):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__VEL = 10
        self.__bullet_image = bullet_image
        self.__bullets = []
    
    def draw(self, window):
        bullet_image = pygame.transform.scale(self.__bullet_image, (self.__width, self.__height))
        window.blit(bullet_image ,(self.__x, self.__y, self.__width, self.__height))

    def bul_movement(self):
        for bullet in self.__bullets:
            self.__y -= self.__VEL
            if self.__x < 0:
                self.__bullets.remove(bullet)
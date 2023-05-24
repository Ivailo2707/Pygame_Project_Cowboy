import pygame


WIDTH, HEIGHT = 1100, 800

class Player2:
    def __init__(self, x, y, width, height, p2_image):
        self.rect = pygame.Rect(x, y, width, height)
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__VEL = 6
        self.__p2_image = p2_image
        self.bullets = []
        self.__health = 10

    def draw(self, window):
        player_image = pygame.transform.scale(self.__p2_image, (self.__width, self.__height))
        window.blit(player_image ,(self.__x, self.__y, self.__width, self.__height))

    def handle_movement(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed [pygame.K_LEFT] and self.__x + self.__VEL > -10:
            self.__x -= self.__VEL
        if keys_pressed [pygame.K_RIGHT] and self.__x + self.__VEL < 1030:
            self.__x += self.__VEL
        if keys_pressed [pygame.K_UP] and self.__y - self.__VEL > 0:
            self.__y -= self.__VEL
        if keys_pressed [pygame.K_DOWN] and self.__y - self.__VEL < HEIGHT/2 - self.__height:
            self.__y += self.__VEL

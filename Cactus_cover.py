import pygame

class Cactus_Cover:
    def __init__(self, x, y, height, width, image):
        self._x = x
        self._y = y
        self._height = height
        self._width = width
        self._health = 5
        self._cactus_image = image

    def draw(self, window):
        obstacle_image = pygame.transform.scale(self._cactus_image, (self._width, self._height))
        window.blit(obstacle_image ,(self._x, self._y, self._width, self._height))

    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def get_height(self):
        return self._height
    
    def get_width(self):
        return self._width
    
    def get_obstacle_rect(self):
        return pygame.Rect(self._x, self._y, self._width, self._height)
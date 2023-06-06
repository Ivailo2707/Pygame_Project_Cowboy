import pygame
import os

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1100, 800

class Player2:
    def __init__(self, x, y, width, height, p2_image):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._VEL = 4
        self._bullets = []
        self._p2_image = p2_image
        self._health = 10
        self._health_font = pygame.font.SysFont('comicsans', 40)
        self._white = (250, 250, 250)
        self._BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gunshot.mp3'))

    def draw(self, window):
        player_image = pygame.transform.scale(self._p2_image, (self._width, self._height))
        window.blit(player_image ,(self._x, self._y, self._width, self._height))

    
    def get_width(self):
        return self._width
    
    def get_height(self):
        return self._height


    def handle_movement(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed [pygame.K_LEFT] and self._x + self._VEL > -10:
            self._x -= self._VEL
        if keys_pressed [pygame.K_RIGHT] and self._x + self._VEL < 1030:
            self._x += self._VEL
        if keys_pressed [pygame.K_UP] and self._y - self._VEL > 0:
            self._y -= self._VEL
        if keys_pressed [pygame.K_DOWN] and self._y - self._VEL < HEIGHT/2 - self._height - 10:
            self._y += self._VEL

    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def get_rect(self):
        return pygame.Rect(self._x, self._y, self._width, self._height)
    
    def take_normal_damage(self):
        self._health -= 1
        return self._health
    
    def take_colission_with_cactus_damage(self):
        self._health -= 0.01
        return self._health


    def draw_health(self, window, curr_health):
        p2_health_tounded = round(curr_health, 2)
        p1_health_text = self._health_font.render("Health: " + str(p2_health_tounded), 1, self._white)
        window.blit(p1_health_text, (50, 50))

    def shoot(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RCTRL and len(self._bullets) < 3:
                bullet = pygame.Rect(self._x + self._width//2.2, self._y + self._height//2, 10, 5)
                self._bullets.append(bullet)
                self._BULLET_FIRE_SOUND.play()


    def get_health(self):
        return self._health
    
    def get_bullets(self):
        return self._bullets
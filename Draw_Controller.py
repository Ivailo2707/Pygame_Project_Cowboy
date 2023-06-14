import pygame
import os

pygame.font.init()

WIDTH, HEIGHT = 1100, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cowboy shooter")


class Draw_Controller:
    def __init__(self, covers, P1, P2, Bullet_Controller):
        self._DESERT = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Desert.png')), (WIDTH, HEIGHT))
        self._covers = covers
        self._P1 = P1
        self._P2 = P2
        self._Bullet_Ctrl = Bullet_Controller
        self._caput_m = (35, 15, 13)
        self._winner_font = pygame.font.SysFont('comicsans', 100)
        self._timer_font = pygame.font.SysFont('comicsans', 50)

    def draw_winner(self, text):
        winner_text = self._winner_font.render(text, 1, self._caput_m)
        WIN.blit(winner_text, (WIDTH/2 - winner_text.get_width()/2, HEIGHT/2 - winner_text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(5000)

    def draw_time(self, timer):
        timer_text = pygame.transform.rotate(self._timer_font.render("Time: " + str(int(timer / 1000)) + "/120" + "s", True, (255, 255, 255)), 270)
        WIN.blit(timer_text, (1000, HEIGHT//2 - timer_text.get_height()//2))

    def draw_window(self, timer):
        WIN.blit(self._DESERT, (0, 0))
        self._P1.draw_health(WIN, self._P1.get_health())
        self._P2.draw_health(WIN, self._P2.get_health())

        for cover in self._covers:
            if cover.get_status():
                cover.draw(WIN)

        self.draw_time(timer)
        self._P1.draw(WIN)
        self._P2.draw(WIN)
        self._Bullet_Ctrl.draw_bullets(WIN)
        pygame.display.update()

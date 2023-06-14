import pygame

class Cactus_Damage_Control():
    def __init__(self, covers, P1, P2):
        self._covers = covers
        self._P1 = P1
        self._P2 = P2

    def handle_cactus_collisions(self):
        for i in range(0, 3):
            if (self._P1.get_rect().colliderect(self._covers[i].get_obstacle_rect())):
                if self._covers[i].get_status():
                    self._P1.take_colission_with_cactus_damage()

        for i in range(3, 6):
            if (self._P2.get_rect().colliderect(self._covers[i].get_obstacle_rect())):
                if self._covers[i].get_status():
                    self._P2.take_colission_with_cactus_damage()


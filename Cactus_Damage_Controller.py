import pygame

class Cactus_Damage_Control():
    def __init__(self, cover_1_1, cover_1_2, cover_1_3, cover_2_1, cover_2_2, cover_2_3, P1, P2):
        self._P1_COLLIDE_WITH_CACTUS_SIDE_1_NUMBER_1 = pygame.USEREVENT + 1
        self._P1_COLLIDE_WITH_CACTUS_SIDE_1_NUMBER_2 = pygame.USEREVENT + 2
        self._P1_COLLIDE_WITH_CACTUS_SIDE_1_NUMBER_3 = pygame.USEREVENT + 3
        self._P2_COLLIDE_WITH_CACTUS_SIDE_2_NUMBER_1 = pygame.USEREVENT + 4
        self._P2_COLLIDE_WITH_CACTUS_SIDE_2_NUMBER_2 = pygame.USEREVENT + 5
        self._P2_COLLIDE_WITH_CACTUS_SIDE_2_NUMBER_3 = pygame.USEREVENT + 6
        self._cover_1_1 = cover_1_1
        self._cover_1_2 = cover_1_2
        self._cover_1_3 = cover_1_3
        self._cover_2_1 = cover_2_1
        self._cover_2_2 = cover_2_2
        self._cover_2_3 = cover_2_3
        self._P1 = P1
        self._P2 = P2

    def handle_cactus_colissions(self):
        if self._P1.get_rect().colliderect(self._cover_1_1.get_obstacle_rect()):
            pygame.event.post(pygame.event.Event(self._P1_COLLIDE_WITH_CACTUS_SIDE_1_NUMBER_1))

        elif self._P1.get_rect().colliderect(self._cover_1_2.get_obstacle_rect()):
            pygame.event.post(pygame.event.Event(self._P1_COLLIDE_WITH_CACTUS_SIDE_1_NUMBER_2))

        elif self._P1.get_rect().colliderect(self._cover_1_3.get_obstacle_rect()):
            pygame.event.post(pygame.event.Event(self._P1_COLLIDE_WITH_CACTUS_SIDE_1_NUMBER_3))

        if self._P2.get_rect().colliderect(self._cover_2_1.get_obstacle_rect()):
            pygame.event.post(pygame.event.Event(self._P2_COLLIDE_WITH_CACTUS_SIDE_2_NUMBER_1))

        elif self._P2.get_rect().colliderect(self._cover_2_2.get_obstacle_rect()):
            pygame.event.post(pygame.event.Event(self._P2_COLLIDE_WITH_CACTUS_SIDE_2_NUMBER_2))

        elif self._P2.get_rect().colliderect(self._cover_2_3.get_obstacle_rect()):
            pygame.event.post(pygame.event.Event(self._P2_COLLIDE_WITH_CACTUS_SIDE_2_NUMBER_3))

    def take_damage_on_colision(self, event):
            if event.type == self._P1_COLLIDE_WITH_CACTUS_SIDE_1_NUMBER_1:
                if self._cover_1_1.get_status() == True:
                    self._P1.take_colission_with_cactus_damage()
                else:
                    pass

            if event.type == self._P1_COLLIDE_WITH_CACTUS_SIDE_1_NUMBER_2:
                if self._cover_1_2.get_status() == True:
                    self._P1.take_colission_with_cactus_damage()
                else:
                    pass 

            if event.type == self._P1_COLLIDE_WITH_CACTUS_SIDE_1_NUMBER_3:
                if self._cover_1_3.get_status() == True:
                    self._P1.take_colission_with_cactus_damage()
                else:
                    pass 

            if event.type == self._P2_COLLIDE_WITH_CACTUS_SIDE_2_NUMBER_1:
                if self._cover_2_1.get_status() == True:
                    self._P2.take_colission_with_cactus_damage()
                else:
                    pass

            if event.type == self._P2_COLLIDE_WITH_CACTUS_SIDE_2_NUMBER_2:
                if self._cover_2_2.get_status() == True:
                    self._P2.take_colission_with_cactus_damage()
                else:
                    pass 

            if event.type == self._P2_COLLIDE_WITH_CACTUS_SIDE_2_NUMBER_3:
                if self._cover_2_3.get_status() == True:
                    self._P2.take_colission_with_cactus_damage()
                else:
                    pass 
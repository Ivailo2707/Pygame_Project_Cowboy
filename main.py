import pygame
import os
from Player1 import Player1
from Player2 import Player2
from Game_Controller import Game_Controller
from Cactus_cover import Cactus_Cover


pygame.font.init()

GaCtrl = Game_Controller()

def main():
    GaCtrl.game()
    

if __name__ == "__main__":
    main()
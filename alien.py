import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, al_game):
        super().__init__()
        self.screen = al_game.screen
        self.image = pygame.image.load("D:\\图片\\alien_bmp.bmp")
        self.image = pygame.transform.scale(self.image, (90,45))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        

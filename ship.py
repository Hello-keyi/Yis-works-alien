import pygame

class Ship :

    def __init__(self,al_game):
        self.screen = al_game.screen
        self.screen_rect = al_game.screen.get_rect()
        self.image = pygame.image.load("D:\图片\ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme (self):
        self.screen_blit(self.image,self.rect)

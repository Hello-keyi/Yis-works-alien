import pygame

class Keyi:
    #生成这个类

    def __init__(self,al_game):
        #给图片进行初始化操作，告诉他一开始要有什么信息

        self.image = pygame.image.load("image\profile_photo_bmp.bmp")
        #给他图片
        self.screen = al_game.screen
        #设计尺寸
        self.image = pygame.transform.scale(self.image, (50, 50))
        #告诉对象，生成的页面
        self.screen_rect = al_game.screen.get_rect()
        #告诉对象，窗口的大小
        self.rect = self.image.get_rect()
        #给对象一个矩形
        



    def blitme(self):
        #运行的时候，给他图片和位置
        self.screen.blit(self.image,self.rect)

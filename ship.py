import pygame
#加入pygame


class Ship :
#这个是关于ship的参数设置


    def __init__(self,al_game):
        #对这个对象进行一开始的操作
        
        self.screen = al_game.screen
        #告诉对象，生成的页面
        self.settings = al_game.settings
        #我给他seet的参数
        self.screen_rect = al_game.screen.get_rect()
        #告诉对象，窗口的大小
        self.image = pygame.image.load("D:\图片\ship_bmp.bmp")
        self.image = pygame.transform.scale(self.image, (60,60))
        #让对象有了图片，生成的图片
        self.rect = self.image.get_rect()
        #给对象一个属性，位置
        self.rect.midbottom = self.screen_rect.midbottom
        #接下来是按键设置的初始设置
        self.moving_right = False
        

        #右的设置
        self.moving_left = False
        #左的设置
        self.moving_up = False
        #上的设置
        self.moving_down = False 
        #下的设置
        self.x = float(self.rect.x)
        #给坐标设置成浮点数
        self.y = float(self.rect.y)



    def blitme (self):
        #每一次刷新，都给对象图片和位置

        self.screen.blit(self.image,self.rect)



    def update (self):
        #这里是运行游戏时，实时刷新船的绘画位置的

        if self.moving_right and self.rect.right < self.screen_rect.right :
            self.x += self.settings.ship_speed_x
            #这里是右边
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed_x
            #这里是左边
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed_y
            #这里是上边
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed_y
            #这里是下边
        self.rect.x = self.x
        #再把位置传给属性
        self.rect.y = self.y
        #这样x和y的坐标就都给了属性了
        


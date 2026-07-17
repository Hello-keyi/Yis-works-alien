import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #外星人的类

    def __init__(self, al_game):
        #对外星人初始化操作

        super().__init__()
        #继承
        self.screen = al_game.screen
        #告诉他生成的页面
        self.settings = al_game.settings
        #给他基本设置，包括速度，大小，方向等等
        self.image = pygame.image.load("images/alien_bmp.bmp")
        #给他图片
        self.image = pygame.transform.scale(self.image, (90,45))
        #给他图片大小
        self.rect = self.image.get_rect()
        #一个矩形区域
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #给出坐标，分别是长和宽
        self.x = float(self.rect.x)
        #给他矩形左上角的横坐标
        


    def update(self):
        #更新外星人的x坐标

        self.x += self.settings.alien_speed * self.settings.fleet_direction
        #横坐标加上设计值
        self.rect.x = self.x
        #告诉这个矩形新的位置
    


    def check_edges(self):
        #检查外星人是否接触边界

        screen_rect = self.screen.get_rect()
        #让一个变量储存屏幕的矩形数据
        return (self.rect.right >= screen_rect.right ) or (self.rect.left <= 0 )
        #返回布尔值，对象的右坐标和屏幕右坐标的比较
        #还有对象左坐标和左边界的比较
    




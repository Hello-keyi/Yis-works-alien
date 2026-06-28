import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    #子弹参数，对子弹的操作


    def __init__(self,al_game):
        #创建一个子弹对象

        super().__init__()
        self.screen = al_game.screen
        #子弹的页面
        self.settings = al_game.settings
        #子弹的设置继承
        self.color = self.settings.bullet_color
        #子弹的颜色设置
        self.rect = pygame.Rect(0,0,self.settings.bullet_width
                                ,self.settings.bullet_height)
        #子弹长宽高
        self.rect.midtop = al_game.ship.rect.midtop
        #子弹出现在飞船头部
        self.y = float(self.rect.y)
        #子弹的位置



    def update(self):

        #更新子弹的位置
        self.y -= self.settings.bullet_speed
        #子弹的y坐标改变的值是setting的设置值
        self.rect.y = self.y
        #子弹当前位置值改为子弹的y坐标



    def draw_bullet(self):
        #画出子弹，包括子弹的绘画页面，颜色，位置

        pygame.draw.rect(self.screen,self.color,self.rect)


        
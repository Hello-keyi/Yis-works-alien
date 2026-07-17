import pygame.font


class Button_again:
    #按钮类

    def __init__(self,ai_game,msg):
        #初始化按钮属性

        self.screen = ai_game.screen
        #获取屏幕
        self.screen_rect = self.screen.get_rect()
        #获取屏幕的矩形属性

        self.width, self.height = 200, 50
        #定义按钮的长和宽
        self.button_again_color = (0, 135, 0)
        #定义按钮的颜色
        self.text_color = (255, 255, 255)
        #定义文字的颜色
        self.font = pygame.font.Font(None, 48)
        #定义字体和大小

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        #创建一个矩形对象，位置在(0,0)，长宽为width和height
        self.rect.center = self.screen_rect.center
        #将矩形对象的中心设置为屏幕的中心

        self._prep_msg(msg)
        #将msg渲染为图像，并使其在按钮上居中


    def _prep_msg(self,msg):
        #将msg渲染为图像，并使其在按钮上居中

        self.msg_image = self.font.render(msg, True, self.text_color, self.button_again_color)
        #将msg渲染为图像，抗锯齿为True，文字颜色为text_color，背景颜色为button_color
        self.msg_image_rect = self.msg_image.get_rect()
        #获取图像的矩形属性
        self.msg_image_rect.center = self.rect.center
        #将图像的矩形属性的中心设置为按钮的矩形属性的中心


    def draw_button_again(self):
        #绘制按钮

        self.screen.fill(self.button_again_color, self.rect)
        #用button_color填充按钮的矩形区域
        self.screen.blit(self.msg_image, self.msg_image_rect)
        #将msg_image绘制到屏幕上，位置为msg_image_rect
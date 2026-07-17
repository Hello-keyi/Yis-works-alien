import pygame.font
import read_score


class Scoreboard:
    #一个关于计分板的类,显示信息

    def __init__(self,al_game):
        #初始化
        
        self.screen = al_game.screen
        #给页面
        self.screen_rect = self.screen.get_rect()
        #拿到页面大小位置参数

        self.settings = al_game.settings
        #继承设置类数据
        self.stats = al_game.stats
        #拿到状态设置

        self.text_color = (0,30,0)
        #字体颜色设置
        self.font = pygame.font.Font(None,30)
        #字形设置

        self.perp_score()
        #准备图像




    def perp_score(self):
        #得分显示

        score_str = str(f"prints:{self.stats.score}")
        #拿到字体内容
        level_str = str(f"level:{self.settings.ship_level}")
        #拿到数据
        limit_str = str(f"limit:{self.stats.ship_limit}")
        #给变量赋值
        score_first_str = str("first: " + str(read_score.get_top3()[0]))
        #方便书写
        score_second_str = str("second: " + str(read_score.get_top3()[1]))
        #方便书写
        score_third_str = str("third: " + str(read_score.get_top3()[2]))
        #方便书写



        self.score_image = self.font.render(score_str,True,
                    self.text_color,self.settings.bg_color)
        #给锯齿设置，字体颜色，字体内容，背景颜色
        self.level_image = self.font.render(level_str,True,
                    self.text_color,self.settings.bg_color)
        #给锯齿设置，字体颜色，字体内容，背景颜色
        self.limit_image = self.font.render(limit_str,True,
                    self.text_color,self.settings.bg_color)
        #给锯齿设置，字体颜色，字体内容，背景颜色
        self.score_first_image = self.font.render(score_first_str,True,
                    self.text_color,self.settings.bg_color)
        #给锯齿设置，字体颜色，字体内容，背景颜色
        self.score_second_image = self.font.render(score_second_str,True,
                    self.text_color,self.settings.bg_color)
        #给锯齿设置，字体颜色，字体内容，背景颜色
        self.score_third_image = self.font.render(score_third_str,True,
                    self.text_color,self.settings.bg_color)
        #给锯齿设置，字体颜色，字体内容，背景颜色



        self.score_rect = self.score_image.get_rect()
        #创建矩形
        self.score_rect.right = self.screen_rect.right - 20
        #字体的横坐标位置
        self.score_rect.top = 20
        #字体的纵坐标的设置

        self.level_rect = self.level_image.get_rect()
        #创建矩形
        self.level_rect.right = self.screen_rect.right - 20
        #字体的横坐标位置
        self.level_rect.top = 50
        #字体的纵坐标的设置

        self.limit_rect = self.limit_image.get_rect()
        #创建矩形
        self.limit_rect.right = self.screen_rect.right - 20
        #字体的横坐标位置
        self.limit_rect.top = 80
        #字体的纵坐标的设置

        self.score_first_rect = self.score_first_image.get_rect()
        #创建矩形
        self.score_first_rect.right = self.screen_rect.right - 20
        #字体的横坐标位置
        self.score_first_rect.top = 110
        #字体的纵坐标的设置

        self.score_second_rect = self.score_second_image.get_rect()
        #创建矩形
        self.score_second_rect.right = self.screen_rect.right - 20
        #字体的横坐标位置
        self.score_second_rect.top = 140
        #字体的纵坐标的设置

        self.score_third_rect = self.score_third_image.get_rect()
        #创建矩形
        self.score_third_rect.right = self.screen_rect.right - 20
        #字体的横坐标位置
        self.score_third_rect.top = 170
        #字体的纵坐标的设置




    def show_score(self):
        #展示分数

        self.screen.blit(self.score_image,self.score_rect)
        #显示分数
        self.screen.blit(self.level_image,self.level_rect)
        #显示等级
        self.screen.blit(self.limit_image,self.limit_rect)
        #显示剩余飞船
        self.screen.blit(self.score_first_image,self.score_first_rect)
        #第一
        self.screen.blit(self.score_second_image,self.score_second_rect)
        #第二
        self.screen.blit(self.score_third_image,self.score_third_rect)
        #第三

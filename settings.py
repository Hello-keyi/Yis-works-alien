class Settings :
    #这个东西掌管页面，页面的长款和颜色

    def __init__(self):
        #设置一些初始化的操作

        self.screen_width = 1200
        #页面的宽
        self.screen_height = 800
        #页面的高
        self.bg_color = (250,250,250)
        #页面的颜色
        self.ship_speed_x = 3
        #这里设置船x的速度
        self.ship_speed_y = 3.5
        #这里设置船y的速度
        self.bullet_speed = 3
        #设置子弹速度
        self.bullet_width = 2
        #设置子弹宽度
        self.bullet_height = 7
        #设置子弹长度
        self.bullet_color = (60,60,60)
        #设置子弹颜色
        self.bullet_allowed = 5
        #限制子弹数量
        
        
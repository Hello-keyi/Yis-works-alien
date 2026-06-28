import sys
import pygame
from settings import Settings
from ship import Ship
from keyi import Keyi
from bullet import Bullet
from alien import Alien
#我要吐槽，蟒蛇书给的一堆有的没的方法，我看不懂，给一点注释吧



class AlienInvasion():

    def __init__(self):
        #第一个函数是初始化

        pygame.init()
        self.clock = pygame.time.Clock()
        #这个东西主管时间吧
        self.settings = Settings()
        #这个东西包含set的内容，实际上是页面的数据，包括长，宽和颜色
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width , self.settings.screen_height)
        )
        #这里面的数据利用了set，定义了screen，装下set的数据
        self.ship = Ship(self)
        #赋予属性，这个属性是一个类
        self.bullet = pygame.sprite.Group()
        #给pygame管理
        self.aliens = pygame.sprite.Group()
        #外星人给他
        self.keyi = Keyi(self)
        #给他一个背景类
        self._create_fleet()
        #创建外星人并且加入组
        pygame.display.set_caption("柯忆大王的外星人小游戏")
        #文字说明



    def run_game(self):
        #运行的操作

        while True:
            #让文件持续运行

            self._check_events()
            #检测用户是否点了取消
            self.ship.update()
            #让船的位置一直变化
            self._update_bullet()
            #更新子弹数据
            self._update_screen()
            #持续刷新图像
            self.clock.tick(120)
            #设置帧率



    def _check_events(self):
        #对玩家按键经行检测

        for event in pygame.event.get():
            #一个循环，判断是否运行

            if event.type == pygame.QUIT:
                #如果用户取消了游戏
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                #如果用户没有取消的同时点击了键盘
                self.check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                #如果不是取消的同时，松开了键盘
                self.check_keyup_event(event)


                
    def check_keydown_events(self,event):
        #响应按下

        if event.key == pygame.K_RIGHT:
            #如果用户对右键操作
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            #如果用户对左键操作
            self.ship.moving_left = True

        elif event.key == pygame.K_UP:
            #如果用户对上键操作
            self.ship.moving_up = True

        elif event.key == pygame.K_DOWN:
            #如果用户对下键操作
            self.ship.moving_down = True

        elif event.key == pygame.K_ESCAPE:
            #如果用户点击“esc”，可以取消了游戏
            sys.exit()

        elif event.key == pygame.K_SPACE:
            #点击空格就开火
            self.fire_bullet()



    def check_keyup_event(self,event):
        #如果按键上来了

        if event.key == pygame.K_RIGHT:
            #如果用户对右键操作
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            #如果用户对左键操作
            self.ship.moving_left = False

        elif event.key == pygame.K_UP:
            #如果用户对上键操作
            self.ship.moving_up = False

        elif event.key == pygame.K_DOWN:
            #如果用户对下键操作
            self.ship.moving_down = False



    def fire_bullet(self):
        #开火的操作

        if len(self.bullet) < self.settings.bullet_allowed:
            #如果在场子弹多于设计值

            new_bullet = Bullet(self)
            #给一个新的子弹
            self.bullet.add(new_bullet)
            #子弹对象加一个新的



    def _update_screen(self):
            #实时更新屏幕的图片
            
            self.screen.fill(self.settings.bg_color)
            #画出背景颜色
            self.keyi.blitme()
            #给出背景图片
            for bullet in self.bullet.sprites():
                #如果子弹是被定义的
                bullet.draw_bullet()
                #就画一个新的
            self.aliens.draw(self.screen)
            #画出外星人
            self.ship.blitme()
            #持续绘画飞船
            pygame.display.flip()
            #显示绘制的图案




    def _update_bullet(self):
        #删除子弹多余

        self.bullet.update()
        #执行子弹数据更新
        for bullet in self.bullet.copy():
            #对每一个被定义的子弹
            if bullet.rect.bottom <= 0:
                #如果子弹位置超过限制
                self.bullet.remove(bullet)
                #让他消失
    


    def _create_fleet(self):
        #创造外星人

        alien = Alien(self)
        #创建对象
        alien_width , alien_height = alien.rect.size
        current_x = alien_width
        current_y = alien_height
        while current_y < (self.settings.screen_height - 3*alien_height):
            while current_x < (self.settings.screen_width - 2*alien_width):
                self._create_alien(current_x,current_y)
                current_x += 2*alien_width
            current_x = alien_width
            current_y += 2 * alien_height

    
    def _create_alien(self,x_position,y_position):

        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)



if __name__ == "__main__":
    ai = AlienInvasion()
    #创建一个对象
    ai.run_game()
    #对他执行运行操作

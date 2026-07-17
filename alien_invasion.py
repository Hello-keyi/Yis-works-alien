import sys

import pygame

from button_again import Button_again
from settings import Settings
from ship import Ship
from keyi import Keyi
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from time import sleep
from button import Button
from scoreboard import Scoreboard
import read_score
import os
#引用模块

#我要吐槽，蟒蛇书给的一堆有的没的方法，我看不懂，给一点注释吧
#因为我还不熟练，就每一行都注释，以后不会了

def resource_path(relative_path):
    #开发/打包后都能找到资源文件

    if hasattr(sys, '_MEIPASS'):
        # 打包后的临时解压目录
        return os.path.join(sys._MEIPASS, relative_path)
    
    return os.path.join(os.path.abspath("."), relative_path)
    # 开发时的项目目录

class AlienInvasion():

    def __init__(self):
        #第一个函数是初始化

        pygame.init() 
        self.game_active = False
        #游戏活动状态初始设置
        self.suspend = False
        #暂停状态初始设置
        pygame.display.set_caption("柯忆大王的外星人小游戏")
        #文字说明


        #给pygame进行初始化操作，确保他正常运行，毕竟，这么大的模块没有初始化也不太合理对吧
        self.settings = Settings()
        #这个东西包含set的内容，实际上是页面的数据，包括长，宽和颜色
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width , self.settings.screen_height)
        )
        #这里面的数据利用了set，定义了screen，装下set的数据
        self.stats = GameStats(self)
        #创建存储统计数据的实例
        self.sb = Scoreboard(self)
        #创建实例
        self.ship = Ship(self)
        #赋予属性，这个属性是一个类
        self.keyi = Keyi(self)
        #给他一个背景类
        self.play_button = Button(self,"Play")
        #创建一个按钮对象
        self.again_button = Button_again(self,"Play Again")
        #创建一个“再玩一次”按钮对象
        self.bullet = pygame.sprite.Group()
        #给pygame管理
        self.aliens = pygame.sprite.Group()
        #外星人给他
        self._create_fleet()
        #创建外星人并且加入组

        self.clock = pygame.time.Clock()
        #这个东西主管时间吧



    def run_game(self):
        #运行的操作

        while True:
            #让文件持续运行

            self._check_events()
            #检测用户是否点了取消

            if self.game_active:
                #如果游戏活动状态为True

                self.ship.update()
                #更新飞船数据
                self._update_bullet()
                #更新子弹数据
                self._update_aliens()
                #更新外星人数据
                self.winover()
                #如果把外星人都干掉了就外星人加速

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
                self.game_over()
                #游戏结束操作
                self.game_over_print
                #打印数据提示
                sys.exit()
                #退出游戏

            elif event.type == pygame.KEYDOWN:
                #如果用户没有取消的同时点击了键盘
                self.check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                #如果不是取消的同时，松开了键盘
                self.check_keyup_event(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                #如果用户点击了鼠标
                mouse_pos = pygame.mouse.get_pos()
                #获取鼠标位置
                self._check_play_button(mouse_pos)
                #检查鼠标是否点击了"开始游戏"按钮
                self._check_again_button(mouse_pos)
                #检查鼠标是否点击了“再玩一次”按钮


                
    def check_keydown_events(self,event):
        #响应按下

        if event.key == pygame.K_d:
            #如果用户对右键操作
            self.ship.moving_right = True
            #把状态改成真

        elif event.key == pygame.K_a:
            #如果用户对左键操作
            self.ship.moving_left = True
            #把状态改成真

        elif event.key == pygame.K_w:
            #如果用户对上键操作
            self.ship.moving_up = True
            #把状态改成真

        elif event.key == pygame.K_s:
            #如果用户对下键操作
            self.ship.moving_down = True
            #把状态改成真

        elif event.key == pygame.K_KP_0:
            #如果用户点击了0
            self.fire_bullet()
            #就开火

        elif event.key == pygame.K_ESCAPE:
            #如果用户点击“esc”，重新游戏
            self.game_over()
            #游戏结束
            self.game_over_print()
            #打印游戏结束提示

        elif event.key == pygame.K_p:
            #如果用户点击了“p”，开始游戏
            if self.suspend:
                #如果暂停状态为True
                self.game_active = True
                #游戏活动状态改为True
                self.suspend = False
                #暂停值改变
            elif not self.suspend:
                #如果暂停状态为False 
                self.game_active = True
                #游戏活动状态改为True

        elif event.key == pygame.K_q:
            #如果用户点击了“q”,游戏暂停
            if not self.suspend and self.game_active:
                #如果暂停状态为False 并正在游戏
                self.game_active = False
                #游戏活动状态为False
                self.suspend = True
                #暂停值改变
                print("Game Paused")
                #提示



    def check_keyup_event(self,event):
        #如果按键上来了

        if event.key == pygame.K_d:
            #如果用户对右键操作
            self.ship.moving_right = False
            #把状态改成假

        elif event.key == pygame.K_a:
            #如果用户对左键操作
            self.ship.moving_left = False
            #把状态改成假

        elif event.key == pygame.K_w:
            #如果用户对上键操作
            self.ship.moving_up = False
            #把状态改成假

        elif event.key == pygame.K_s:
            #如果用户对下键操作
            self.ship.moving_down = False
            #把状态改成假



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

            self.sb.show_score()
            #显示得分和等级
            self.aliens.draw(self.screen)
            #画出外星人
            self.ship.blitme()
            #持续绘画飞船
            self.sb.perp_score()
            #更新数据

            

            if not self.game_active and not self.suspend:
                #如果游戏活动状态为False并且暂停状态为False
                self.play_button.draw_button()
                #就画出“开始游戏”按钮

            elif not self.game_active and self.suspend:
                #如果游戏活动状态为False并且暂停状态为True
                self.again_button.draw_button_again()
                #就画出“再玩一次”按钮

                
            pygame.display.flip()
            #显示绘制的图案



    def _update_bullet(self):
        #删除已经消失的子弹

        self.bullet.update()
        #执行子弹数据更新


        for bullet in self.bullet.copy():
            #对每一个被定义的子弹
            if bullet.rect.bottom < 1:
                #如果子弹位置超过限制
                self.bullet.remove(bullet)
                #让他消失
            colisiobs = pygame.sprite.groupcollide(
                self.bullet,self.aliens,True,True
            )
            #子弹碰到外星人就删除，并且生成一个关于子弹和外星人的字典

            if colisiobs:
                #如果字典不为空,就是子弹碰撞之后

                self.settings.dead_alien_number += 1
                #如果外星人被消灭了，外星人数量加一
                self.stats.score += self.settings.alien_prints
                #统计数据更新
                self.settings.alien_prints += 1
                #每一次更难应该更多分
                self.sb.perp_score()
                #拿到分数数据
                print(f"dead alien number is {self.settings.dead_alien_number}")
                #打印提示



    def _create_fleet(self):
        #创造外星人队伍

        alien = Alien(self)
        #创建对象
        alien_width , alien_height = alien.rect.size
        #给出大小，包括长宽
        current_x = alien_width
        current_y = alien_height
        #当前坐标
        self._create_alien(current_x,current_y)
        #创建外星人
        


        while current_y < (self.settings.screen_height - 8*alien_height):
            #边界判断，是纵轴边界
            while current_x < (self.settings.screen_width - 2*alien_width):
                #边界判断，是横轴边界
                self._create_alien(current_x,current_y)
                #创建外星人
                current_x += 2*alien_width
                #改变横轴坐标位置
            

            current_x = alien_width
            #重置x坐标
            current_y += 2 * alien_height
            #外星人纵坐标加上，继续遍历
        

    
    def _create_alien(self,x_position,y_position):
        #创建外星人

        new_alien = Alien(self)
        #创建新对象
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        #给出外星人的坐标，包括横坐标和纵坐标
        self.aliens.add(new_alien)
        #加上新的外星人



    def _check_fleet_edge(self):
        #检查外星舰队边缘


        for alien in self.aliens.sprites():
            #对每一个创建的外星人
            if alien.check_edges():
                #如果外星人碰到了边界
                self._change_fleet_direction()
                #就改变外星人的方向
                break

    

    def _change_fleet_direction(self):
        #改变外星人的方向


        for alien in self.aliens.sprites():
            #对每一个已经创建的外星人
            alien.rect.y += self.settings.alien_drop_speed
            #外星人的y坐标改变

        self.settings.fleet_direction *= -1
        #外星人方向改变



    def _update_aliens(self):
        #更新外星人数据

        self._check_fleet_edge()
        #检查是否碰到边界
        self.aliens.update()
        #外星人前进
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            #如果外星人碰到了飞船
            print("Ship hit!!!")
            #打印提示
            self.ship_hit()
            #响应飞船被撞击
        self._check_aliens_bottom()
        #检查外星人是否到达了底部



    def ship_hit(self):
        #响应外星人和飞船的碰撞

        if self.stats.ship_limit > 0:
            #如果飞船还有剩余次数

            self.stats.ship_limit -= 1
            #飞船的剩余数量减一
            self.bullet.empty()
            #清空子弹
            self.aliens.empty()
            #清空外星人
            self._create_fleet()
            #重新创建外星人舰队
            self.ship.center_ship()
            #重新创建飞船
            self.sb.perp_score()
            #显示数据


        elif self.stats.ship_limit <= 0:
            #如果飞船没有剩余
            self.game_over()
            #游戏结束了
            self.game_over_print()
            #打印游戏结束提示
        


    def _check_aliens_bottom(self):
        #检查外星人是否到达了底部

        for alien in self.aliens.sprites():
            #对每一个外星人
            if alien.rect.bottom >= self.settings.screen_height:
                #如果外星人的底部坐标大于屏幕的底部坐标
                self.ship_hit()
                #响应飞船被撞击
                break
                #结束循环



    def aliens_speedup(self):
        #外星人加速

        self.settings.alien_speed *= self.settings.alien_speedup_scale
        #外星人速度乘以加快速度的比例
        self.settings.bullet_speed *= self.settings.bullet_speedup_scale
        #子弹速度乘以加速比例
        self.settings.ship_speed_x *= self.settings.ship_speedup_scale
        #飞船的x方向速度变化加快

    

    def winover(self):
        #如果把外星人都干掉了就外星人加速

        if not self.aliens:
            #如果外星人被消灭了
            self.bullet.empty()
            #清空子弹
            self._create_fleet()
            #重新生成外星人
            self.ship.center_ship()
            #让飞船回到初始位置
            self.aliens_speedup()
            #让外星人加速
            self.settings.ship_level += 1
            #飞船等级加一
            print(f"ship level is {self.settings.ship_level}")
            #提示飞船等级
            self.suspend = False
            #暂停状态初始设置
            self.sb.perp_score()
            #显示分数
    


    def game_over_print(self):
        #游戏结束提示

            print("Game Over")
            #打印提示
            print(f"ship level is {self.settings.ship_level}")
            #提示飞船等级
            print(f"dead alien number is {self.settings.dead_alien_number}")
            #提示被消灭的外星人数量



    def _check_play_button(self,mouse_pos):
        #检查鼠标是否点击了按钮

        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        #如果鼠标点击了按钮
        if button_clicked and not self.game_active:
            #如果游戏活动状态为False并且点击了按钮
            if self.suspend:
                #如果暂停状态为True
                self.game_active = True
                #游戏活动状态改为True
                self.suspend = False
                #暂停值改变
            elif not self.suspend:
                #如果暂停状态为False 
                self.game_active = True
                #游戏活动状态改为True



    def _check_again_button(self,mouse_pos):
        #检查鼠标是否点击了“再玩一次”按钮

        button_clicked = self.again_button.rect.collidepoint(mouse_pos)
        #如果鼠标点击了“再玩一次”按钮
        if button_clicked and not self.game_active:
            #如果游戏活动状态为False并且点击了“再玩一次”按钮
            self.game_active = True
            #游戏活动状态为True
            self.check_suspend()
            #暂停值改变



    def game_over(self):
        #游戏结束

        read_score.save_score(self.stats.score)
        #存储数据
        self.stats.reset_stats()
        #重置统计数据
        self.game_active = False
        #游戏活动状态为False
        self.aliens.empty()
        #清空外星人
        self.bullet.empty()
        #清空子弹
        self._create_fleet()
        #重新创建外星人舰队
        self.ship.center_ship()
        #让飞船回到初始位置



if __name__ == "__main__":
    #监测是否是直接文件

    ai = AlienInvasion()
    #创建一个对象
    ai.run_game()
    #对他执行运行操作

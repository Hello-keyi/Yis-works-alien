class GameStats:
    #跟踪游戏的统计数据

    def __init__(self,al_game):
        #初始化统计数据

        self.settings = al_game.settings
        #给他一个属性，缓存设置
        self.reset_stats()
        #重置分数
        self.high_score = 0
        #设置高分


    def reset_stats(self):
        #重新设置游戏统计数据

        self.ship_limit = self.settings.ship_limit
        #飞船的数量恢复初始
        self.settings.alien_speed = 1.0
        #外星人速度恢复初始值
        self.settings.ship_level = 1
        #飞船等级恢复初始值
        self.settings.dead_alien_number = 0
        #被消灭的外星人数量恢复初始值
        self.score = 0
        #设置初始分数

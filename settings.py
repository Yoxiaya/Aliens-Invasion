class Settings:
    """储存游戏中所有设置类"""

    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # 飞船设置
        self.ship_speed = 10.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed = 10.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 10

        # 外星人设置
        self.fleet_drop_speed = 20

        # 加快游戏节奏速度
        self.speedup_scale = 1.1
        # 外星人分数的提高速度
        self.score_scale = 1.5

        self.initiakilze_dynamic_settings()
        

    def initiakilze_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1

        # 计分
        self.alien_points = 50

    
    def increase_speed(self):
        """提高速度设置和外星人分数"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
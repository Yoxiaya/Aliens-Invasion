import sys
from settings import Settings
import pygame


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源。"""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        #设置背景色
        self.bg_color = (230,230,230)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            #监视键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #每次循环都重新绘制屏幕
            self.screen.fill(self.settings.bg_color)

            #让最近绘制的屏幕可见。
            pygame.display.flip()


if __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()

import sys
from settings import Settings
from ship import Ship
import pygame


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源。"""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        #设置背景色
        self.bg_color = (230,230,230)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_event()
            #监视键盘和鼠标事件
            self._update_screen()
            self.ship.update()

    def _check_event(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self,event):                
        """响应按下"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left =True


    def _check_keyup_events(self,event):
        """响应松开"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left =False


    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""

        #每次循环都重新绘制屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        #让最近绘制的屏幕可见。
        pygame.display.flip()


if __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
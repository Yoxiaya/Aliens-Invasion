
import sys
from settings import Settings
from bullet import Bullet
from aline import Alien
from ship import Ship
import pygame


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源。"""
        pygame.init()

        self.settings = Settings()
        
        #全屏运行删除以下三个注释
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #设置背景色
        self.bg_color = (230,230,230)


    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_event()
            # 监视键盘和鼠标事件
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_screen()


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
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self,event):
        """响应松开"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left =False



    def _fire_bullet(self):
        """创建一个子弹，并将其加入编组bullets中"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """更新子弹位置并删除消失子弹。"""
        # 更新子弹位置
        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))


    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""

        #每次循环都重新绘制屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)


        #让最近绘制的屏幕可见。
        pygame.display.flip()

    def _create_fleet(self):
        """创建外星人群"""
        # 创建一个外星人
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        self.aliens.add(alien)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # 计算屏幕可以容纳多少个外星人
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - ( 3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # 创建外星人群
        for row_number in range(number_rows):
            # 创建第一行外星人
            for alien_number in range(number_aliens_x):
            # 创建一个外星人并将其加入当前行当
                self._create_alien(alien_number,row_number)

    def _create_alien(self,alien_number,row_number):
        """创建一个外星人并将其放在当前行"""
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

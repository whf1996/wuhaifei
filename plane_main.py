import pygame
from plane_sprites import *


class Game_plane(object):
    """飞机主游戏"""
    #　游戏初始化
    def __init__(self):
        print("游戏初始化．．．")
        # 1. 创建一个窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #2. 创建时钟
        self.clock = pygame.time.Clock()
        #3. 调用私有方法创建精灵和精灵组
        self.__create_sprinte()
        #4. 设置定时器事件－创建敌人飞机－1S
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        #5.　设置定时器事件－创建子弹－0.5s
        pygame.time.set_timer(CREATE_BULLET_EVENT, 500)
    def __create_sprinte(self):
        # 创建背景精灵对象
        bg1 = BackGround()
        bg2 = BackGround(True)
        # 创建背景组精灵对象
        self.back_group = pygame.sprite.Group(bg1, bg2)
        # 创建敌人精灵组
        self.enemy_group = pygame.sprite.Group()
        # 创建我方飞机精灵对象
        self.hero = Hero()
        # 创建我方飞机精灵组对象
        self.hero_group = pygame.sprite.Group(self.hero)

    # 游戏开始
    def game_start(self):
        print("游戏开始．．．")
        while True:

            #1.设置刷新帧
            self.clock.tick(TIMER)
            # 2.事件监听
            self.__event_handle()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新／绘制精灵组
            self.__update_sprites()
            # 5.更新显示
            pygame.display.update()



    def __event_handle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game_plane.__game_over()
            elif event.type == CREATE_BULLET_EVENT:
                self.hero.fire()
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌人出现了．．．")
                enemy = Enemy()
                self.enemy_group.add(enemy)
                # 第一种方式－不支持连按
            #elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:

                # 第二种方式－支持连按
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2

        elif key_pressed[pygame.K_LEFT]:
            self.hero.speed = -2


        elif key_pressed[pygame.K_UP]:
            self.hero.speedy = -2


        elif key_pressed[pygame.K_DOWN]:
            self.hero.speedy = 2


        else:
            self.hero.speed = 0
            self.hero.speedy = 0
    def __check_collide(self):
        # 1.敌人飞机精灵组和子弹精灵组碰撞，true为销毁
        pygame.sprite.groupcollide(self.hero.bullet_group,self.enemy_group,True,True)
        # 2.英雄精灵和敌方飞机精灵组碰撞
        enemy_list = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        # 对返回值进行判断
        if len(enemy_list) > 0:
            #杀死英雄飞机对象
            self.hero.kill()
            # 游戏结束
            Game_plane.__game_over()
    def __update_sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)
    @staticmethod
    def __game_over():
        print("结束游戏．．．")
        pygame.quit()
        exit()




if __name__ == '__main__':
    game = Game_plane()
    game.game_start()
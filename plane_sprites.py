import random
import pygame
#屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
#刷新帧常量
TIMER = 60
#创建敌人定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 创建子弹定时器常量
CREATE_BULLET_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
    """游戏精灵"""
    def __init__(self, image_name, speed=1):

        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

class BackGround(GameSprite):
    """背景精灵"""
    def __init__(self,is_alt= False):
        #1. 继承父类的初始化
        super().__init__("./images/background.png")
        #2. 判断是否要交替
        if is_alt:
            self.rect.y = -self.rect.height


    def update(self):
        # 1.继承父类的ｕｐｄａｔｅ
        super().update()
        # 2.判断是否出界
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height

class Enemy(GameSprite):
    """敌人精灵"""
    # 继承父类初始化并重写
    def __init__(self):
        super().__init__("./images/enemy1.png")
    # 1.重写速度
        self.speed = random.randint(1,3)
    # 2.重写位置
        max_rect = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_rect)
        self.rect.bottom = 0
    # 继承父类更新方法并重写
    def update(self):
        super().update()
        # 出界判断并敌人删掉对象
        if self.rect.y >= SCREEN_RECT.height:
            #print("敌人对象要被删除")
            self.kill()

            #　此方法用于检测是否成功删掉对象
    def __del__(self):
        #print("敌人挂了　%s" %self.rect)
        pass


class Hero(GameSprite):
    """飞机精灵"""
    def __init__(self):
        super().__init__("./images/me1.png", 0)
        self.rect.y = SCREEN_RECT.height - 300
        self.rect.x = (SCREEN_RECT.width - self.rect.width)/2
        self.speedy = 0
        # 创建我方飞机子弹精灵组对象
        self.bullet_group = pygame.sprite.Group()

    def update(self):
        # 每次按键都加个ｓｐｐｅｄ
        self.rect.x += self.speed
        self.rect.y += self.speedy
        # 边界检测
        if self.rect.x >= SCREEN_RECT.width - self.rect.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y >= SCREEN_RECT.bottom:
            self.rect.y = SCREEN_RECT.bottom
    def fire(self):
        for i in (0, 20, 40):
            bullet = Bullet()
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.bottom = self.rect.y - i
            self.bullet_group.add(bullet)

class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./images/bullet1.png",2)



    def update(self):
        # 子弹往上飞行
        self.rect.y -= self.speed
        if self.rect.bottom <= 0:
            self.kill()

    def __del__(self):
        #print("删除子弹")
        pass
import pygame
from plane_sprites import *

#　游戏的初始化

#　初始化pygame里所有模块
pygame.init()

#　创建窗口并返回窗口
screen = pygame.display.set_mode((480,700))

# 绘制图像到窗口
# 1.load加载图像数据到内存
bg = pygame.image.load("./images/background.png")
# 2.blit图片到窗口
screen.blit(bg, (0, 0))
# 3.update更新窗口图片
# pygame.display.update()

# 绘制我方飞机图像到窗口
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (180,400))
pygame.display.update()

# 定义时钟对象
clock = pygame.time.Clock()
#　记录飞机的初始位置
hero_rect = pygame.Rect(180, 400, 102, 126)

#　创建敌方精灵对象
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png",2)

# 创建敌方精灵组对象
enemy_group = pygame.sprite.Group(enemy, enemy1)

#　游戏的开始
while True:

    # 　60次可以产生连续效果不错的动画
    clock.tick(60)

    #　捕获用户事件并作出发应
    event_list = pygame.event.get()
    for event in  event_list:
        if event.type == pygame.QUIT:
            print("退出游戏")
            pygame.quit()
            exit()

    hero_rect.y -=1
    if hero_rect.y + hero_rect.height <= 0:
        hero_rect.y = 700

    screen.blit(bg, (0, 0))
    # blit可以传入元组，也可以是矩形对象
    screen.blit(hero, hero_rect)

    #　更新精灵组所有精灵对象位置
    enemy_group.update()
    #把精灵组所有对象描绘到屏幕上
    enemy_group.draw(screen)

    pygame.display.update()
    #　用定时器控制while循环内部频率

# 退出pygame里所有模块(退出窗口)，释放内存空间
pygame.quit()
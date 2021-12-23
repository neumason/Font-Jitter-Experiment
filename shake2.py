#1--导入模块
import pygame
import sys
import datetime

#2--初始化
pygame.init()

size=(600,400)
x,y=173,82
#3--设置窗口
screen=pygame.display.set_mode(size)#以元组的方式传入屏幕的宽高
#设置这个题目
pygame.display.set_caption("模拟震动实验")

img=pygame.image.load("./image/background.png").convert()

zitiimg=pygame.image.load("./image/yong.png").convert()
clock=pygame.time.Clock()

#抖动的轨迹数组，可以自定义频率和方向
step = [-1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1]
i = 0
isShot = False
starttime = datetime.datetime.now()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    x += step[i]
    y += step[i]
    i += 1
    i %= 20
    screen.blit(img, (0, 0))
    screen.blit(zitiimg, (x, y))
    clock.tick(1000)
    pygame.display.update()  # 更新整个屏幕显示
    endtime = datetime.datetime.now()
    if (endtime - starttime).seconds == 15:
        if not isShot:
            pygame.image.save(screen, "./image/screenshot.jpg")
            isShot = True
from Map import *
import pygame
import sys
from Mmap import map
from me import  Me


if __name__ == '__main__':
    screen = pygame.display.set_mode((550,350)) #设置窗口大小为550*350
    pygame.display.set_caption('简易魔塔')
    me = Me()    #初始化玩家角色
    n = 0        #
    lastimg = 0  #玩家图像状态（面向：上下左右）的标志
    pygame.init()  #创建一个game框体
    m = list(map[me.floor]) #读取列表中的楼层

    pygame.font.init()
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #退出
                pygame.quit()  
                sys.exit()
            elif event.type == pygame.KEYDOWN: #当按下键
                if event.key == pygame.K_UP:  #当按下上键
                    me.myd = 0
                    lastimg = 0

                elif event.key == pygame.K_RIGHT: #当按下右键
                    me.myd = 1
                    lastimg = 3


                elif event.key == pygame.K_DOWN: #当按下下键
                    me.myd = 2
                    lastimg = 1

                elif event.key == pygame.K_LEFT: #当按下左键
                    me.myd = 3
                    lastimg = 2

                else:
                    me.myd = 4 
        load(m,screen,me)        #刷新
        screen.blit(me.meimg[lastimg],(me.myx,me.myy)) #绘图
        m = me.updateMe(m,screen)
        pygame.display.update()



import pygame
from time import sleep

ADDENEMY = pygame.USEREVENT +1

class Guaiwu(object):
    def __init__(self,name,hp,att,defend,money,jingyan,image):
        self.name = name  #怪物名
        self.hp = hp  #血量
        self.att = att  #攻击力
        self.defend = defend  #防御力
        self.money = money   #击杀后掉落的金钱数
        self.jingyan = jingyan   #击杀后获得的经验值
        self.img = pygame.image.load('images/%s.jpg' % image)  #该怪物对应的图片
        self.image = str(image)   


    def attack(self,me,screen,changex,changey): #战斗模块
        img1 = pygame.image.load('images/player_2.jpg')  #获取玩家图片
        img2 = pygame.image.load('images/%s.jpg' % self.image) #获取怪物图片
        font = pygame.font.SysFont("SimHei", 20)     #字体设置为黑体

        while True :
            self.hp -= me.att-self.defend   #玩家先攻，减少怪物血量
            me.hp -= self.att-me.defend    #怪物攻击，减少玩家血量

            pygame.draw.rect(screen, (0, 0, 0), (0, 80, 352, 160))  #绘制一个框体放攻击画面

            screen.blit(img1, (95, 170))   #玩家形象以及数值
            screen.blit(font.render('生命:' + str(me.hp), 1, (253, 177, 6)), (85, 90))
            screen.blit(font.render('攻击:' + str(me.att), 1, (253, 177, 6)), (85, 115))
            screen.blit(font.render('防御:' + str(me.defend), 1, (253, 177, 6)), (85, 140))

            screen.blit(img2, (270, 170))  #怪物形象以及数值
            screen.blit(font.render('生命:' + str(self.hp), 1, (253, 177, 6)), (260, 90))
            screen.blit(font.render('攻击:' + str(self.att), 1, (253, 177, 6)), (260, 115))
            screen.blit(font.render('防御:' + str(self.defend), 1, (253, 177, 6)), (260, 140))


            if me.hp <1 :   #如果玩家血量小于1，玩家死亡，游戏结束
                pygame.quit()
            else:
                if self.hp < 1 :
                    me.myy += changey * 32
                    me.myx += changex * 32
                    me.y += changey
                    me.x += changex
                    me.jingyan += self.jingyan
                    me.money += self.money
                    return me.money,me.jingyan
                elif self.hp < me.att - self.defend:
                    self.hp = 0
                    pygame.display.update()
                    pygame.time.wait(500)
                else:
                    pygame.display.update()
                    pygame.time.wait(500)




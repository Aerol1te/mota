import pygame
from Mmap import guailist
from Mmap import map

class Me(object):
    def __init__(self):
        self.me = pygame.Rect(160,320,30,30)
        self.meimg = [
            pygame.image.load('images/player_1.jpg'),
            pygame.image.load('images/player_2.jpg'),
            pygame.image.load('images/player_3.jpg'),
            pygame.image.load('images/player_4.jpg')
        ]
        self.myx = 160
        self.myy = 320
        self.myd = 4   #0上 1右 2下 3左
        self.y = 10
        self.x = 5
        self.floor = 2 #层数
        self.yellow = 1 #黄钥匙
        self.red = 1  #红钥匙
        self.blue = 1  #蓝钥匙
        self.level = 1 #等级
        self.money = 0  #钱
        self.jingyan = 0
        self.hp = 1500  #生命
        self.att = 20  #攻击
        self.defend = 20  #防御



    def updateMe(self,map,screen):
        self.map = map
        if self.myd == 0 :
          if self.y > 0:
               next = self.map[self.y-1][self.x]
               changex = 0
               changey = -1
               self.move(next, changex, changey,screen)
          else:
              next = 0
        elif self.myd == 1:
            if self.x < 10:
                next = self.map[self.y][self.x + 1]
                changex = 1
                changey = 0
                self.move(next, changex, changey, screen)
            else:
                next = 0
        elif self.myd == 2:
            if self.y < 10:
                next = self.map[self.y + 1][self.x]
                changex = 0
                changey = 1
                self.move(next, changex, changey, screen)
            else:
                next = 0

        elif self.myd == 3:
            if self.x > 0:
                    next = self.map[self.y][self.x-1]
                    changex = -1
                    changey = 0
                    self.move(next, changex, changey, screen)
            else:
                    next = 0
        else :
            pass
        self.myd = 4


        return self.map

    def choosef(self,f,down=False):
      if not down :
        if f == 1 :
            self.myx = 160
            self.myy = 320
            self.y = 10
            self.x = 5

        elif f == 2 :
            self.x = 5
            self.y = 9
            self.myx = 160
            self.myy = 288

        elif f == 3:
            self.x = 0
            self.y = 1
            self.myx = 0
            self.myy = 32

      else:
          if f == 1:
              self.myx = 160
              self.myy = 32
              self.y = 1
              self.x = 5

          elif f == 2:
              self.x = 1
              self.y = 0
              self.myx = 32
              self.myy = 0

    def move(self,next,changex,changey,screen):
        if next == 509:#地板
                self.myy += changey*32
                self.myx += changex*32
                self.y += changey
                self.x += changex
        elif next == 507:#向上楼梯
            self.floor += 1
            self.choosef(self.floor)
            self.map = list(map[self.floor])
        elif next == 508:#向下楼梯
            self.floor -= 1
            self.choosef(self.floor,True)
            self.map = list(map[self.floor])
        elif next == 303:#红钥匙
            self.myy += changey * 32
            self.myx += changex * 32
            self.y += changey
            self.x += changex
            self.map[self.y][self.x] = 509
            self.red += 1
        elif next == 302:#蓝钥匙
            self.myy += changey * 32
            self.myx += changex * 32
            self.y += changey
            self.x += changex
            self.map[self.y][self.x] = 509
            self.blue += 1
        elif next == 301:#黄钥匙
            self.myy += changey * 32
            self.myx += changex * 32
            self.y += changey
            self.x += changex
            self.map[self.y][self.x] = 509
            self.yellow += 1
        elif next == 307:#蓝宝石
            self.myy += changey * 32
            self.myx += changex * 32
            self.y += changey
            self.x += changex
            self.map[self.y][self.x] = 509
            self.defend += 20
        elif next == 308:#红宝石
            self.myy += changey * 32
            self.myx += changex * 32
            self.y += changey
            self.x += changex
            self.map[self.y][self.x] = 509
            self.att += 20 
        elif next == 309:#蓝药水
            self.myy += changey * 32
            self.myx += changex * 32
            self.y += changey
            self.x += changex
            self.map[self.y][self.x] = 509
            self.hp += 1000
        elif next == 310:#红药水
            self.myy += changey * 32
            self.myx += changex * 32
            self.y += changey
            self.x += changex
            self.map[self.y][self.x] = 509
            self.hp += 500
        elif next == 311:#神秘之书
            self.myy += changey * 32
            self.myx += changex * 32
            self.y += changey
            self.x += changex
            self.map[self.y][self.x] = 509
            self.att += 300
            self.defend += 100
            self.hp += 5000
        elif next == 312:#绿宝石
            self.myy += changey * 32
            self.myx += changex * 32
            self.y += changey
            self.x += changex
            self.map[self.y][self.x] = 509
            self.att += 15
            self.defend += 15
        elif next == 313:#屠龙宝刀
            self.myy += changey * 32
            self.myx += changex * 32
            self.y += changey
            self.x += changex
            self.map[self.y][self.x] = 509
            self.att += 50
        elif next == 305:#蓝门
            if self.blue > 0:
                self.myy += changey * 32
                self.myx += changex * 32
                self.y += changey
                self.x += changex
                self.blue -= 1
                self.map[self.y][self.x] = 509
        elif next == 304:#黄门
            if self.yellow > 0:
                self.myy += changey * 32
                self.myx += changex * 32
                self.y += changey
                self.x += changex
                self.yellow -= 1
                self.map[self.y][self.x] = 509
        elif next == 306:#红门
            if self.red > 0:
                self.myy += changey * 32
                self.myx += changex * 32
                self.y += changey
                self.x += changex
                self.red -= 1
                self.map[self.y][self.x] = 509
        elif (next>=0) and (next < 14):
            self.money,self.jingyan = guailist[next].attack(self,screen,changex,changey)
            self.map[self.y][self.x] = 509


import pygame

awidth = 32
aheight = 32



def load(map,screen,me):
        x = 0
        y = 0
        for i in map:
            for j in i :
                img = pygame.image.load('images/%s.jpg' % str(j)) #读取该坐标对应物体的图片
                screen.blit(img,(y*32,x*32))  #绘图
                y += 1 #y轴坐标+1读取下一个
            y = 0   #将坐标初始化为0继续下一列
            x += 1  #读取下一列

        img = pygame.image.load('images/509.jpg') #读取地板图片
        for i in range(5):
            for j in range(11):
                screen.blit(img, (372+i*32,j*32))  #画地板

        font = pygame.font.SysFont("SimHei", 20)   #字体设置为黑体
        y = 0
        text = '第'+str(me.floor)+'层'               
        surf = font.render(text, 1, (253, 177, 6))
        screen.blit(surf, (382, 20 + y * 30))

        y += 1
        text = '等级：'+str(me.level)
        surf = font.render(text,1,(253,177,6))
        screen.blit(surf,(382,20+y*30))

        y += 1
        text = '生命：' + str(me.hp)
        surf = font.render(text, 1, (253, 177, 6))
        screen.blit(surf, (382, 20 + y * 30))

        y += 1
        text = '攻击：' + str(me.att)
        surf = font.render(text, 1, (253, 177, 6))
        screen.blit(surf, (382, 20 + y * 30))

        y += 1
        text = '防御：' + str(me.defend)
        surf = font.render(text, 1, (253, 177, 6))
        screen.blit(surf, (382, 20 + y * 30))

        y += 1
        text = '金币：' + str(me.money)
        surf = font.render(text, 1, (253, 177, 6))
        screen.blit(surf, (382, 20 + y * 30))

        y += 1
        text = '经验：' + str(me.jingyan)
        surf = font.render(text, 1, (253, 177, 6))
        screen.blit(surf, (382, 20 + y * 30))

        y += 1
        text = '黄钥匙：' + str(me.yellow)
        surf = font.render(text, 1, (253, 177, 6))
        screen.blit(surf, (382, 20 + y * 30))

        y += 1
        text = '蓝钥匙：' + str(me.blue)
        surf = font.render(text, 1, (253, 177, 6))
        screen.blit(surf, (382, 20 + y * 30))

        y += 1
        text = '红钥匙：' + str(me.red)
        surf = font.render(text, 1, (253, 177, 6))
        screen.blit(surf, (382, 20 + y * 30))




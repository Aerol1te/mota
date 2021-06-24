from guaiwu import Guaiwu


map = {#地图绘制
    1:[
    [501,506,506,506,506,507,506,506,506,506,501],
    [501,506,506,506,506,509,506,506,506,506,501],
    [501,506,506,506,506,509,506,506,506,506,501],
    [501,506,506,506,506,509,506,506,506,506,501],
    [501,506,506,506,506,509,506,506,506,506,501],
    [501,506,506,506,506,509,506,506,506,506,501],
    [501,501,506,506,506,509,506,506,506,501,501],
    [501,501,501,501,501,304,501,501,501,501,501],
    [505,501,505,501,601,509,312,501,505,501,505],
    [505,505,505,505,505,509,505,505,505,505,505],
    [505,505,505,505,505,509,505,505,505,505,505]
    ],
    2:[
    [507,509,301,0  ,1  ,0  ,509,509,509,509,509],
    [501,501,501,501,501,501,501,501,501,501,509],
    [310,509,4  ,304,509,501,310,301,310,501,509],
    [310,4  ,308,501,509,501,310,301,310,501,509],
    [501,304,501,501,509,501,501,501,2  ,501,509],
    [301,5  ,307,501,509,304,6  ,0  ,3  ,501,509],
    [309,312,302,501,509,501,501,501,501,501,509],
    [501,304,501,501,509,509,509,509,509,509,509],
    [311,5  ,307,501,501,306,501,501,501,304,501],
    [310,309,301,501,303,509,509,501,301,7  ,302],
    [310,308,301,501,509,508,509,501,301,301,301]
    ],
    3: [
    [508,501,509,12 ,509,501,308,307,301,303,501],
    [509,501,307,501,309,501,308,307,301,302,501],
    [509,501,301,501,301,501,308,307,301,11 ,501],
    [509,501,301,501,301,501,501,501,501,304,501],
    [509,501,509,501,509,509,509,304,509,509,501],
    [509,501,304,501,501,304,501,501,304,501,501],
    [509,504,509,509,509,509,501,509,11 ,509,501],
    [509,501,304,501,501,305,501,510,501,510,501],
    [509,501,301,501,309,310,501,312,501,312,501],
    [509,501,301,501,309,310,501,509,501,509,501],
    [507,501,308,501,309,310,501,603,501,604,501]
  ],
    4:[
    [313,1  ,301,501,502,605,503,501,501,501,501],
    [1  ,301,312,501,509,509,509,501,509,3  ,509],
    [301,4  ,509,501,501,304,501,501,509,501,509],
    [501,304,501,501,509,4  ,509,501,301,501,1  ],
    [509,509,509,501,501,501,509,501,301,501,3  ],
    [0  ,501,509,3  ,1  ,3  ,509,501,301,501,1  ],
    [0  ,501,501,501,501,501,509,509,509,501,509],
    [509,509,509,509,509,501,501,304,501,501,509],
    [501,501,501,501,3  ,501,1  ,509,0  ,501,509],
    [509,509,509,509,509,501,307,3  ,301,501,509],
    [508,501,501,501,501,501,308,309,301,501,507]
  ],
    5:[
    [509,13  ,509,501,509,602,509,501,509,2  ,509],
    [304,501,304,501,509,312,509,501,304,501,304],
    [509,501,509,501,501,510,501,501,509,501,509],
    [509,501,4  ,501,8  ,9 ,8  ,501,4  ,501,509],
    [3  ,501,310,501,307,8  ,308,501,310,501,3  ],
    [3  ,501,310,501,501,306,501,501,310,501,3  ],
    [1  ,501,509,501,7  ,10 ,7  ,501,509,501,1  ],
    [509,501,509,501,307,7  ,308,501,509,501,509],
    [509,501,509,501,501,305,501,501,509,501,509],
    [509,501,509,501,301,509,301,501,509,501,509],
    [507,501,509,2  ,509,509,509,2  ,509,501,508]]
}

guailist = {}#怪物列表{名称，生命值，攻击力，防御值，获取金钱，获取经验，编号}

i = 0
guailist[i] = Guaiwu('小史莱姆',110,14,2,3,3,i)
i += 1
guailist[i] = Guaiwu('红史莱姆',140,18,4,4,4,i)
i += 1
guailist[i] = Guaiwu('黑史莱姆',300,52,33,18,18,i)
i += 1
guailist[i] = Guaiwu('小蝙蝠',150,14,5,8,7,i)
i += 1
guailist[i] = Guaiwu('骷髅兵',183,28,10,14,13,i)
i += 1
guailist[i] = Guaiwu('骷髅剑士',330,72,40,27,20,i)
i += 1
guailist[i] = Guaiwu('初级法师',200,122,20,21,16,i)
i += 1
guailist[i] = Guaiwu('木乃伊',650,220,140,40,30,i)
i += 1
guailist[i] = Guaiwu('大蝙蝠',340,90,50,27,20,i)
i += 1
guailist[i] = Guaiwu('吸血蝙蝠',900,550,220,50,40,i)
i += 1
guailist[i] = Guaiwu('石头怪',1550,425,400,54,44,i)
i += 1
guailist[i] = Guaiwu('初级卫兵',750,350,120,40,35,i)
i += 1
guailist[i] = Guaiwu('骑士卫兵',1450,710,500,63,48,i)
i += 1
guailist[i] = Guaiwu('魔王',20000,1000,600,300,200,i)

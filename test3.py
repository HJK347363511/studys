#-*- codeing = utf-8 -*-
#@time : 2021/6/7 0007 16:44
#@author : HJK
#@file : test3.py
#@softwoare : PyCharm

'''
    购物商城：
        需求：购物商城
        1.商品
        2.金钱
        3.购物车

        买东西需求：
            看这个商品是不是存在
                 若存在，
                    您的余额是否够买这个东西
                        将自己的余额减去商品的价格
                        将这个商品添加购物车。
                    余额不够：提示您的余额，穷鬼！选其他商品！
            若不存在：提示，您要的商品不存在。
            是否是Q，q：
                结算，打印购物小条。
有十张优惠券，系统初始化就会随机抽取一张优惠券。最后计算的时候进行打折。
1.进入商城时候，随机抽奖某个商品的优惠券。
优惠券如下：
		10张辣条优惠券：满600减300
		20张Lenovo电脑优惠券：半折甩卖
2.结算时，添加购物积分功能
10元1个积分。
'''

# 准备必备商品
import random
prices_list = [["联想电脑",0.5],["Iphone 16x plus",0.3],["PS5游戏机",0.7],["老于妈",0.1],["老于妈",0.5]
               ,["卫龙辣条",1],["HUA WEI watch",0.8],["MAC PC",0.5]]
#随机生成一张优惠券
random_num = random.randint(0,6)
print(random_num)
#优惠的商品
youhui_goods = prices_list[random_num]
shop=[
    ["联想电脑",6000],
    ["Iphone 16x plus",15000],
    ["PS5游戏机",3500],
    ["老干妈",7.5],
    ["老于妈",5.5],
    ["卫龙辣条",10],
    ["HUA WEI watch",1200],
    ["MAC PC",15000]
]
# 空的购物车
mycart = []
money = 0
sale_money = 0
all_apeed = 0
man = 0
while True:
    money = input("请输入你的余额：")
    if money.isdigit():
        money = int(money)
        break
    else:
        print("输入有误，请重新输入")
new_price = 0
while True:
    for i,j in enumerate(shop):
        print(i,j)
    id = input("请输入要购买商品的编号：")
    if id.isdigit():
        id = int(id)
        if id > len(shop)-1 or id < 0:
            print("输入的编号有误，请重新输入")
        else:
            if youhui_goods[0] == shop[id][0]!= "卫龙辣条":
                new_price = shop[id][1] * youhui_goods[1]
                if  money >= new_price:
                    mycart.append(shop[id][0])
                    money = money - new_price
                    sale_money += new_price
                    all_apeed+= new_price
                    print("购买成功,余额还剩￥:",money)
                else:
                    print("余额只剩：",money,"请购买其他商品")
            elif youhui_goods[0]  == "卫龙辣条":
                if  money >= shop[id][1]:
                    mycart.append(shop[id][0])
                    money = money - shop[id][1]
                    print("满减前还剩",money)
                    sale_money += shop[id][1]
                    all_apeed  +=shop[id][1]
                    print("满减前花了",sale_money)
                    if sale_money // 600 > 0:
                        nums = sale_money//600
                        money += 300*int(nums)
                        print("满减后还剩", money)
                        all_apeed -= 300*int(nums)
                        sale_money = 0
                        print("满减后花了", all_apeed)
                else:
                    print("余额只剩：",money,"请购买其他商品")
            else:
                if  money >= shop[id][1]:
                    mycart.append(shop[id][0])
                    money = money - shop[id][1]
                    all_apeed += shop[id][1]
                    print("购买成功,余额还剩￥:",money)
                else:
                    print("余额只剩：",money,"请购买其他商品")
    elif id == "q" or id == "Q":
        print("成功退出系统")
        break
    else:
        print("输入的编号有误，请重新输入")
print("-----------您购买的商品信息如下-----------")
zidian = {}
for i in range(len(mycart)):
    if mycart[i] not in zidian:
        zidian[mycart[i]] = 1
    else:
        zidian[mycart[i]] += 1
print(zidian)
for key,values in zidian.items():
    print(key,values)
old_fen = 0
new_fen = all_apeed // 10
print("您的积分为%d"%(old_fen+new_fen))
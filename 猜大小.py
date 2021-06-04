#-*- codeing = utf-8 -*-
#@time : 2021/6/4 0004 16:17
#@author : HJK
#@file : 猜大小.py
#@softwoare : PyCharm

import random
#添加随机数0-150
money = 5000
fail_count = 0
while True:
    random_num = random.randint(0, 150)
    nums = input("请输入您猜的数字：")
    if nums.isdigit():
        nums = int(nums)
        if nums > random_num:
            print("猜的数字太大了")
            money -= 500
            fail_count += 1
        elif nums < random_num:
            print("猜的数字太小了")
            money -= 500
            fail_count += 1
        else:
            print("恭喜您猜对了")
            money += 3000
            fail_count = 0
    else:
        print("请输入0-150之间的整数")
    if fail_count == 15:
            print("连败次数已为15次，系统锁定")
            break
    if money <= 0:
            print("金币已近输光了")
            break
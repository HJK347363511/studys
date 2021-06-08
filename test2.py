#-*- codeing = utf-8 -*-
#@time : 2021/6/4 0004 20:28
#@author : HJK
#@file : test2.py
#@softwoare : PyCharm
# 实现输入10个数字，并打印10个数的求和结果
# i = 0
# sum = 0
# while i < 10:
#     a = int(input("请输入第%d个正整数："%(i+1)))
#     sum = sum + a
#     i += 1
# print(sum)



# 从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
# max = 0
# i = 0
# sum = 0
# while i < 10:
#     a = int(input("请输入第%d个正整数："%(i+1)))#
#     if a > max:
#         max = a
#     sum = sum + a
#     i += 1
# avg = sum / 10
# print("和为：",sum,"平均值为：",avg,"最大值为:",max)




# 使用random模块，如何产生 50~150之间的数？
# import random
# random_num = random.randint(50,150)
# print(random_num)




# 从键盘输入任意三边，判断是否能形成三角形，若可以，
# 则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
# a = int(input("请输入a边："))
# b = int(input("请输入b边："))
# c = int(input("请输入c边："))
# if a>0 and b>0 and c>0 and a+b>c and a+c >b and b+c >a and a-b<c and a-c <b and b-c <a:
#     if a==c!=b or a== b!=c or b==c!=a:
#         print("等腰三角形")
#     elif a==b==c:
#         print("等边三角形")
#     elif a**2+c**2==b**2 or a**2+b**2==c**2 or b**2+c**2==a**2:
#         print("直角三角形")
#     else:
#         print("普通三角形")
# else:
#     print("不能构成三角形")

#


# 有以下两个数，使用+，-号实现两个数的调换。
# A=56
# B=78
# 实现效果：
# A=78
# B=56
# A = 56
# B = 78
# C = 0
# C = A+B
# A = C - A
# B = C - B
# print(A,B)

# B = A+B
# A = B - A
# B = B - A



# 实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
# name = "root"
# password = "admin"

# username = "root"
# admin = "admin"
# #
# i = 3
# while True:
#     name = input("请输入用户名：")
#     passwd = input("请输入密码：")
#     if name == username and passwd == admin:
#         print("登陆成功")
#         break
#     else:
#          i = i - 1
#          if i == 0:
#              print("机会用光，系统锁定")
#              break
#          print("密码错误，还有%d次机会" % i)



# 使用while编程实现求1~100以内的数的和！
# i = 1
# sum = 0
# while i<=100:
#     sum += i
#     i += 1
# print(sum)


# 一只青蛙掉在井里了，井高20米，青蛙白天往上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
# b = 3
# h = 2
# sum = b-h
# days = 1
# while True:
#     b += 3
#     sum = b - h
#     days += 1
#     if sum >= 20:
#         break
#     h += 2
# print(days)








# 有一个列表，[“北京”,”上海”,”广东”]
# 1)将中国所有省会城市添加到上述列表中
# 2)广东成为第二大发达城市，将广东排在上海前面
# 3)[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
# 这是中国GDP排名前8的城市的GDP数值，请统计前8城市的GDP总和，平均GDP。
# list = ["北京","上海","广东"]
# list1 = ["南京","昆明","成都","广州","武汉","石家庄","沈阳","哈尔滨","杭州","福州","济南","兰州","台北","西宁","西安","郑州"
#          ,"太原","合肥","长沙","贵阳","长春","南昌","海口","天津","重庆","拉萨","银川","乌鲁木齐","呼和浩特","香港","澳门"]
# list  = list + list1
# list[1] = "广东"
# list[2] = "上海"
# new_list = [36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
# avg = 0
# sum = 0
# for i in new_list:
#     sum += i
# avg = sum / len(new_list)
# print(sum,avg)




# 有以下一个列表，求其中是5的倍数的和
# a = [1,5,21,30,15,9,30,24]

# sum = 0
# a = [1,5,21,30,15,9,30,24]
# for i in a:
#     if i % 5 ==0:
#         sum += i
# print(sum)

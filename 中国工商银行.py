#-*- codeing = utf-8 -*-
#@time : 2021/6/9 0009 15:50
#@author : HJK
#@file : 中国工商银行.py
#@softwoare : PyCharm
import random

all_user_dict = {}
def str_int(some):
    if some.isdigit():
        some = int(some)
        return some
    else:
        print("请输入正确的整数")
#界面显示
def Interface_display():
    print("********************************************")
    print("*            中国工商银行                   *")
    print("*            账户管理系统                   *")
    print("*                V1.0                      *")
    print("********************************************")
    print(" ")
    print("*1.开户                                    *")
    print("*2.存钱                                    *")
    print("*3.取钱                                    *")
    print("*4.转账                                    *")
    print("*5.查询                                    *")
    print("*6.BYE!                                    *")
    print("********************************************")


def swith_structure():
    while True:
        Interface_display()
        num = input("请输入你的选项")
        num = str_int(num)
        if num == 1:
            nums = add_user()
            if nums == 1:
                print("添加成功")
                print(all_user_dict)
            elif nums == 2:
                print("该账户已经被使用，请重新输入")
            elif nums == 3:
                print("用户库已满")
            else:
                pass
        elif num == 2:
            boolean = Save_money(all_user_dict)
            if boolean == False:
                print("存钱失败,该账号不存在")
        elif num == 3:
            nums = Withdraw_money(all_user_dict)
            if nums == 0:
                print("取钱成功")
            elif nums == 1:
                print("账号不存在")
            elif nums == 2:
                print("密码不对")
            elif nums == 3:
                print("钱不够")
            else:
                pass
        elif num == 4:
            nums =  transfer_accounts(all_user_dict)
            if nums == 0:
                print("转账成功")
                print(all_user_dict)
            elif nums == 1:
                print("账号不对")
            elif nums == 2:
                print("密码不对")
            elif nums == 3:
                print("钱不够")
            else:
                pass
        elif num == 5:
            RETURNS = query_accounts(all_user_dict)
            if RETURNS == None:
                print("密码错误")
            elif RETURNS == 1:
                print("用户不存在")
            elif RETURNS == 0:
                print("查询成功")
        elif num == 6:
            print("成功退出系统")
            break
        else:
            print("输入正确的编号")


#存款余额
#添加用户
def add_user():
    one_user_list = []
    # a)用户：账号（str：系统随机产生8位数字）、姓名(str)、密码(int: 6
    # 位数字)、地址、存款余额(int)、开户行（银行的名称（str））
    #生成随机八位账户
    account_number = str(random.randint(10000000,99999999))
    print(account_number)
    name           = input("请输入姓名：")
    passwd         = input("请输入密码：")
    passwd = str_int(passwd)
    bank_name = "中国工商银行北京分行"
    #存款余额
    Deposits = 0
    country = input("请输入国家：")
    Province = input("请输入省份：")
    street = input("请输入街道：")
    House_number = input("请输入门牌号：")
    one_user_list = one_user_list+[name,passwd,bank_name,Deposits,country,Province,street,House_number]
    if account_number in all_user_dict:
        return 2
    if len(all_user_dict) > 100:
        return 3
    all_user_dict[account_number] = one_user_list
    return  1



# 2.存钱（传入值：用户的账号、存取的金额。返回值：布尔类型值）
def  Save_money(all_user_dict):
    user_account_number = input("请输入用户账号：")
    if user_account_number in all_user_dict:
        money = input("请输入要存的金额：")
        money = str_int(money)
        all_user_dict[user_account_number][3] += money
        print(user_account_number,all_user_dict[user_account_number])
    else:
        return False


# 3.取钱（传入值：用户的账号，用户密码，取钱金额。返回值：整型值（0：正常，1：账号不存在，2：密码不对，3：钱不够））
def  Withdraw_money(all_user_dict):
    user_account_number = input("请输入用户账号：")
    passwd = input("请输入密码：")
    passwd = str_int(passwd)
    if user_account_number in all_user_dict:
        if passwd == all_user_dict[user_account_number][1]:
                qu_money = input("请输入要取的金额：")
                qu_money = str_int(qu_money)
                if qu_money <= all_user_dict[user_account_number][3]:
                     all_user_dict[user_account_number][3] -= qu_money
                     print(user_account_number,all_user_dict[user_account_number])
                else:
                    return 3
        else:
            return 2
    else:
        return 1
# 4.转账（传入值：转出的账号，转入的账号，转出账号的密码，转出的金额。返回值：0：正常，1：账号不对，2密码不对，3钱不够）
def transfer_accounts(all_user_dict):
    user_account_number_out = input("请输入转出账号：")
    user_account_number_in  = input("请输入转入账号：")
    if user_account_number_out in all_user_dict and user_account_number_in in all_user_dict:
            passwd = input("请输入转出账号密码：")
            passwd = str_int(passwd)
            if passwd == all_user_dict[user_account_number_out][1]:
                    transfer_money = input("请输入要转的金额：")
                    transfer_money = str_int(transfer_money)
                    if transfer_money <= all_user_dict[user_account_number_out][3]:
                         all_user_dict[user_account_number_out][3] -= transfer_money
                         all_user_dict[user_account_number_in][3]  += transfer_money
                         print(user_account_number_out,all_user_dict[user_account_number_out])
                         print(user_account_number_in,all_user_dict[user_account_number_in])
                    else:
                        return 3
            else:
                return 2
    else:
        return 1
# 查询账户功能（传入值：账号，账号密码，返回值：空）
def query_accounts(all_user_dict):
    user_account_number_query = input("请输入用户账号：")
    if user_account_number_query in all_user_dict:
        passwd = input("请输入用户密码：")
        passwd = str_int(passwd)
        if passwd == all_user_dict[user_account_number_query][1]:
            print("当前账号:",user_account_number_query,
                  "密码:",all_user_dict[user_account_number_query][1],
                  "余额：",all_user_dict[user_account_number_query][3],
                  "用户居住地址:",all_user_dict[user_account_number_query][4]+
                                 all_user_dict[user_account_number_query][5]+
                                 all_user_dict[user_account_number_query][6]+
                                 all_user_dict[user_account_number_query][7],
                  "当前账户的开户行：",all_user_dict[user_account_number_query][2])
        else:
            return None
    else:
        return 1
    return 0

if __name__ == '__main__':
        swith_structure()

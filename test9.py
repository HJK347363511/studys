#-*- codeing = utf-8 -*-
#@time : 2021/6/17 0017 16:01
#@author : HJK
#@file : test9.py
#@softwoare : PyCharm
import xlrd
import xlwt

wb    = xlrd.open_workbook(r"D:\Python自动化测试\专题项目\专题2\python1\day09\任务\12月份衣服销售数据.xlsx",encoding_override=True)
sheet = wb.sheet_by_index(0)
#获取行
rows = sheet.nrows
cols = sheet.ncols
sum_price = 0.0#总销售额
all_sale = 0#总销售量


avg_day_sale = 0#平均日销售量
Down_Jacket_all = 0#羽绒服销售量
Furs_all        = 0#皮草销售量
Jeans_all       = 0#牛仔裤销售量
Windbreaker_all = 0#风衣销售量
Shirt_all       = 0#衬衫销售量
T_blood_all     = 0#T恤销售量

Down_Jacket_all_price = 0#羽绒服总销售额
Furs_all_price        = 0#皮草总销售量额
Jeans_all_price       = 0#牛仔裤总销售量额
Windbreaker_all_price = 0#风衣总销售量额
Shirt_all_price       = 0#衬衫总销售量额
T_blood_all_price     = 0#T恤总销售量额

for row in range(rows):
    if  row > 0:
        prices = sheet.cell_value(rowx=row, colx=2)
        nums = sheet.cell_value(rowx=row, colx=4)
        everyday_sale = sheet.cell_value(rowx=row, colx=4)
        sum_price += prices*nums
        all_sale  += everyday_sale
        Clothes_name = sheet.cell_value(rowx=row, colx=1)
        if Clothes_name == "羽绒服":
            Down_Jacket_all += everyday_sale
            Down_Jacket_all_price += prices*nums
        elif Clothes_name == "皮草":
            Furs_all += everyday_sale
            Furs_all_price += prices * nums
        elif Clothes_name == "牛仔裤":
            Jeans_all += everyday_sale
            Jeans_all_price += prices * nums
        elif Clothes_name == "风衣":
            Windbreaker_all += everyday_sale
            Windbreaker_all_price += prices * nums
        elif Clothes_name == "衬衫":
            Shirt_all += everyday_sale
            Shirt_all_price += prices * nums
        else:
            T_blood_all += everyday_sale
            T_blood_all_price += prices * nums
avg_day_sale = int(all_sale / (rows-1))
Down_Jacket_Percentage = Down_Jacket_all / all_sale *100#羽绒服销售量占比
Furs_Percentage        = Furs_all        / all_sale *100#皮草销售量占比
Jeans_Percentage       = Jeans_all       / all_sale *100#牛仔裤销售量占比
Windbreaker_Percentage = Windbreaker_all / all_sale *100#风衣销售量占比
Shirt_Percentage       = Shirt_all       / all_sale *100#衬衫销售量占比
T_blood_Percentage     = T_blood_all     / all_sale *100#T恤销售量占比

Down_Jacket_price_Percentage = Down_Jacket_all_price / sum_price *100#羽绒服销售额占比
Furs_price_Percentage        = Furs_all_price        / sum_price *100#皮草销售额占比
Jeans_price_Percentage       = Jeans_all_price       / sum_price *100#牛仔裤销售额占比
Windbreaker_price_Percentage = Windbreaker_all_price / sum_price *100#风衣销售额占比
Shirt_price_Percentage       = Shirt_all_price       / sum_price *100#衬衫销售额占比
T_blood_price_Percentage     = T_blood_all_price     / sum_price *100#T恤销售额占比

workbook = xlwt.Workbook(encoding="UTF-8")
sheets = workbook.add_sheet("销售统计数据")
for row in range(rows):
    for col in range(cols):
        sheets.write(row,col,label=sheet.cell_value(rowx=row, colx=col))
list_price = [Down_Jacket_price_Percentage,Furs_price_Percentage,Jeans_price_Percentage,Windbreaker_price_Percentage,
        Shirt_price_Percentage, T_blood_price_Percentage]
list_num = [Down_Jacket_Percentage,Furs_Percentage,
            Jeans_Percentage,Windbreaker_Percentage,
            Shirt_Percentage, T_blood_Percentage]

list1_price = ["羽绒服本月销售额占比","牛仔裤本月销售额占比","风衣本月销售额占比","皮草本月销售额占比","T血本月销售额占比","衬衫本月销售额占比"]
list1_num = ["羽绒服本月销售量占比","牛仔裤本月销售量占比","风衣本月销售量占比","皮草本月销售量占比","T血本月销售量占比","衬衫本月销售量占比"]

for i ,j in enumerate(list_price):
    sheets.write(r = row+i+1,c = 8 ,label="%s：，%.2f%%"%(list1_price[i],j))
for i ,j in enumerate(list_num):
    sheets.write(r = row+i+1,c = 4 ,label="%s：，%.2f%%"%(list1_num[i],j))

sheets.write(r = row+1,c = 0 ,label="总销售额:%.2f元"%(sum_price))
sheets.write(r = row+2,c = 0 ,label="总销售量:%.2f件"%(all_sale))
sheets.write(r = row+3,c = 0 ,label="平均日销售量:%.2f件"%(avg_day_sale))

add = "D:\Python自动化测试\专题项目\专题2\python1\day09\统计数据.xlsx"
workbook.save(add)

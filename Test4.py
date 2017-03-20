#coding:utf-8
#输入年月日判断这是那一天

days = [0,31,59,90,120,151,181,212,243,273,304,334]
#省略了判断条件
flag = 0
count = 0
year = int(raw_input("年份:"))
month = int(raw_input("月份:"))
day = int(raw_input("日:"))
if ((year%4==0)and(year%100!=0)) or((year%400==0)):
    flag = 1
if(month>2):
    count = flag
count += days[month-1]+day
print count

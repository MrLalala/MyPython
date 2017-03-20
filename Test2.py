#coding : utf-8
i = int(raw_input("please input money"))

arr = [1000000,600000,4000000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]

money = 0
for m in range(0,6):
    if(i>arr[m]):
        money = money + (i-arr[m])*rat[m]
        i = arr[m]
print money
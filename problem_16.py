num=2**1000
str_num=str(num)
length=len(str_num)
sum_total=0
for i in range(0,length):
    sum_total=int(str_num[i])+sum_total

print(sum_total)
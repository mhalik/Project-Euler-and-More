number=1
for i in range(1,100):
    number=number*i

number_str=str(number)
length=len(number_str)
sum_total=0
for i in range(0,length):
    sum_total=sum_total+int(number_str[i])
    
print(sum_total)


reach=100

def decimalrepeat(n):
    decimal=[0]
    remainder=10
    for i in range(0,reach):
        decimal[i]=int(round(remainder/n,1))
        remainder=(remainder % n)*10
        decimal.append(0)
    
    return(decimal)    
repeat_length=[0,0]
iteration=0
for i in range(1,10):
    decimallist=decimalrepeat(i)
    start_spot=0
    repeating=False
    for j in range(1,8):
        for k in range(0,reach,2):
            term_one=sum(decimallist[k:j])
            term_two=sum(decimallist[(k+j):(k+j+j)])
            if term_one==term_two:
                repeating=True
                break
        if repeating==True:
            break   
        
               
    print(j)
           
#     if sum(decimallist)==0:
#         repeat_length[i]=j
#         repeat_length.append(0)
#         iteration=iteration+1
#     elif sum(decimallist)>0:
#         repeat_length[i]=0
#         repeat_length.append(0)
#         iteration=iteration+1

print(repeat_length)
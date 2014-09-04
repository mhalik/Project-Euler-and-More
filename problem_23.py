import time

def factorlist(n):
    factorlist=[]
    limit=int(round(n**.5))+1
    iteration=0
    for i in range(1,limit):
        if n % i ==0:
            factorlist.append(0)
            factorlist[iteration]=i
            iteration=iteration+1
            if n / i != i:
                factorlist.append(0)
                factorlist[iteration]=int(n/i)
                iteration=iteration+1
            
            
    factorlist.remove(n)
    return factorlist
    print(factorlist)
    

factor_list=0
def abundant(n):
    factor_list=factorlist(n)
    factor_sum=sum(factor_list)
    if factor_sum > n:
        return n
    
    elif factor_sum < n:
        return 0
    
    elif factor_sum==n:
        return 0


start=time.time()
abundant_list=[0]
iteration=0
for i in range (1,28123):
    abundant_test=abundant(i)
    if abundant_test!=0:
        abundant_list[iteration]=abundant(i)
        abundant_list.append(0)
        iteration=iteration+1

abundant_list.remove(0)

integer_list=[0]
for j in range(0,28124):
    integer_list[j]=j
    integer_list.append(0)

# print(abundant_list)
length=len(abundant_list)-1
for k in range(0,length):
    for l in range(0,length):
        spot=abundant_list[k]+abundant_list[l]
        if spot<=28123 :
            integer_list[spot]=0
    
answer=sum(integer_list)

print(answer)
elapsed=time.time()-start
print(elapsed)
   
    





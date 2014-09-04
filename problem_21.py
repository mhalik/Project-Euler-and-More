import time
def amicable(n):
    limit=round((n**.5))
    factorlist=[0]
    iteration=0
    for i in range(1,limit):
        if n % i ==0:
            factorlist[iteration]=i
            factorlist.append(0)
            iteration=iteration+1
            factorlist[iteration]=int(n/i)
            factorlist.append(0)
            iteration=iteration+1
#     print(factorlist)
    factorlist.remove(0)
    p=sum(factorlist)-n
    return p

start=time.time()

amicable_list=[0]
iteration=0
for j in range(4,10000):
    z=amicable(j)
    v=amicable(z)
    if j==v and j!=z:
        amicable_list[iteration]=j+z
        amicable_list.append(0)
        iteration=iteration+1

length=len(amicable_list)
for k in range(1,length):
    recent=k-1
    if amicable_list[k]==amicable_list[recent]:
        amicable_recent=0


answer=int(sum(amicable_list)/2)

print(answer)

elapsed=time.time()-start
print(elapsed)
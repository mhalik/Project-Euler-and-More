import time

start=time.time()

fib=[0,1]
for i in range(2,100000):
    fib.append(0)
    fib[i]=fib[i-1]+fib[i-2]
    fib_length=len(fib)-1
    fib_last=fib[fib_length]
    str_fib_last=str(fib_last)
    last_length=len(str_fib_last)
    if last_length>=1000:
        break
        



end=time.time()

elapsed=end-start

print(fib_length)
print(elapsed)


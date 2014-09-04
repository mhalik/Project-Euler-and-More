def factorlist(n):
    factorlist=[]
    limit=int(round(n**.5))+1
    iteration=0
    for i in range(1,limit):
        if n % i ==0:
            factorlist.append(0)
            factorlist[iteration]=i
            iteration=iteration+1
            factorlist.append(0)
            factorlist[iteration]=int(n/i)
            iteration=iteration+1
    print(factorlist)
        
# prints a list of factors for the number, including itself and one

# if you want to exclude the value, uncomment the following line

# factorlist.remove(n)

# if you want to exclude "one", uncomment the following line

# factorlist.remove(1)
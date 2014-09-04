maximum = 1000000
chain_length=[0]
for num in range(1,maximum):
    number=num
    chain=[0]
    while number > 1:
        if number % 2 == 0:
            number = number/2
            chain.append(0)
        elif number % 2 !=0:
            number = 3*number + 1
            chain.append(0)
    chain_length.append(0)
    chain_length[num]=len(chain)

max(chain_length)
        
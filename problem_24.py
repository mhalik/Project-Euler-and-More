count=(9*8*7*6*5*4*3*2) #0....

count=count*2  #1....

print(count)

count=count+(8*7*6*5*4*3*2) #10....

count=count+(8*7*6*5*4*3*2) #1203....

print(count)

count=count+(8*7*6*5*4*3*2)*4 #1302, #1402, #1502, 1602...

print(count)

count=count+(7*6*5*4*3*2) #1620...

count=count+(7*6*5*4*3*2)*5 #1630, 1640, 1650, 1670,1680

print(count)

count=count+(6*5*4*3*2)*2 #16820, 16830

print(count)

count=count+(5*4*3*2)*5 #168320, 168340, 168350, 168370, 168390

print(count)

count=count+(4*3*2) #1683920

print(count)

count=count+(3*2)*2 #16839240, 16839250

print(count)

count=count+(2)*2 #1683925704

print(count)





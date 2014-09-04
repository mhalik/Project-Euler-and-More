
import csv
import string
with open('C:\\Users\\Max\\Desktop\\names.csv', 'r') as f:
    reader=csv.reader(f)
    for column in reader:
        name_list=column

length=len(name_list)

alphabet=string.ascii_uppercase
numeric=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
name_numbers=[0]
for i in range(0,length):
    name_length=len(name_list[i])
    name_numbers.append(0)
    total=0
    for j in range(0,name_length):
        letter=name_list[i][j]
        location=alphabet.index(letter)
        value=numeric[location]
        total=total+value
    name_numbers[i]=total*i
   
    

answer=sum(name_numbers)

print(answer)
            
        
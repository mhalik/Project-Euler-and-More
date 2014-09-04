number_string=input('What is the dimension of one side? ')
number=int(number_string)

top=(2*number)
numerator=1
for i in range (1,top):
    numerator=numerator*i


denominator=1
topping=number+1
for j in range(1,topping):
    denominator=denominator*j

denominator=(denominator**2)/(2*number)

answer=int(numerator/denominator)
answer_string=str(answer)
answer_string_2='The answer is '
answer_string_final=answer_string_2+answer_string

print (answer_string_final)


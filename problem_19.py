number_of_sundays=0
year=1900
leap_year=False
day=1
month=1
day_of_the_week=1
while year < 2000:
    day=day+1
    day_of_the_week=day_of_the_week+1
    if year % 4 ==0 and year!=1900:
        leap_year=True
    if year % 4!=0:
        leap_year=False
    if day==31 and month==1: 
        month=month+1
        day=0
    if day==31 and month==3: 
        month=month+1
        day=0
    if day==31 and month==5: 
        month=month+1
        day=0
    if day==31 and month==7: 
        month=month+1
        day=0
    if day==31 and month==8: 
        month=month+1
        day=0
    if day==31 and month==10: 
        month=month+1
        day=0
    if day==30 and month==4: 
        month=month+1
        day=0
    if day==30 and month==6: 
        month=month+1
        day=0
    if day==30 and month==9: 
        month=month+1
        day=0
    if day==30 and month==11:
        month=month+1
        day=0
    if month==2 and day==28 and leap_year==False:
        month=month+1
        day=0
    if month==2 and day==29 and leap_year==True:
        month=month+1
        day=0
    if month==12 and day==31:
        year=year+1
        month=1
        day=0
    
    day_v_day=[day,day_of_the_week]
#     print(day_v_day)
    if day_v_day==[1,7]:
        number_of_sundays=number_of_sundays+1
    if day_of_the_week==7:
        day_of_the_week=0
number_of_sundays=number_of_sundays-1
print(number_of_sundays)
    
   
    
    
    
    
    
    
    
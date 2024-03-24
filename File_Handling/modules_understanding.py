# import datetime as dt #Datetime is nothing but a python file consiting of many lines of code 
# #we imported the datetime file as an object
# print(dt.datetime.now())

#Calculator app using modules
import basic_calculator as basic_calc

x=int(input('Enter var 1: '))
y=int(input('Enter var 2: '))

output_sum=basic_calc.addition_of_2_numbers(x,y)
print(f'sum of {x},{y} is {output_sum}')

output_diff=basic_calc.difference(x,y)#difference function
print(f'sum of {x},{y} is {output_diff}')

#Task: Implement this code
# my_birthday=#get a date from user
# days_left=basic_calc.calculate_days_left(my_birthday)
# print(f'{days_left} to your birthday')



#Do it for product and divitions

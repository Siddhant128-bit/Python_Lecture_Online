'''
functions has 2 parts 
1. defintion declaration 
2. call 

initially we have to define a function
then we call that function

function_name(parameters/argements) #call a specific function

y= f(x)

1. Predefined functions: 
    native functions present in python
    print(), input()

2. Custom Functions: 
    Developed by coders themself

    rule: 
        define a function with input parameters and return type 
        call that function whenever we need to use it
'''

#1. Define a function

def random_function_name(a,b,c,d):
    print(a,b,c,d)

#2. Call a function
#random_function_name(1,2,3)


# 1. Return type function

def add_these_numbers(a,b,c,d):
    #print(int(a+b+c+d))
    return int(a+b+c+d)    

# 2. Non Return type function
def multiplication_table(a):
    for i in range(1,11,1):
        print(f'{a} x {i} = {a*i}')

#sum_of_numbers=add_these_numbers(1,2,3,5)
#print(f'Multiplication Table of {sum_of_numbers} is: ')
#multiplication_table(sum_of_numbers)

'''
Default arguments: 
1. an argument value that is always there by default.
2. That can be modified or updated if user specifically adjustes it. 
'''

def multiplication_table_untill_n(number_to_muliply,multiply_upto=10):
    for i in range(1, multiply_upto+1):
        print(f'{number_to_muliply} x {i} = {number_to_muliply * i}')

# multiplication_table_untill_n(1)
# multiplication_table_untill_n(2,15)


'''
arguments type
    we can put any kind of datatype as arguments and those will be recieved by the function 
'''

#print(max([1,12,3,4,5]))

def return_maximum_number(random_argument_type):
    return max(random_argument_type)

#list_of_numbers=[1,2,100,10,150,300]
#maximum_return_number=return_maximum_number(list_of_numbers)
#print(f'Maximum number in {list_of_numbers} is {maximum_return_number} ')
#multiplication_table_untill_n(maximum_return_number)


'''
Args ra kwargs

Args = takes in muptiple arguements maybe 1 in a case maybe 15 in another case and process it like nothing happened.
kwargs= converts into dictionary other then that all same as args 

'''

def display_upto_n(*bunch_of_numbers):
    # print(bunch_of_numbers)
    print(bunch_of_numbers)
    for number in bunch_of_numbers:
        print(number)

#display_upto_n(1,2,3,4,10)


'''
Task 1. Take n from user, collect n numbers of variables and display the maximum number and also sum of all the numbers
'''
def max_of_all_numbers_and_sum_of_all_numbers(*bunch_of_inputs):
    bunch_of_inputs=bunch_of_inputs[0]
    print(f'Total elements: {bunch_of_inputs}')
    print(f'Max element: {max(bunch_of_inputs)} \nSum of elements: {sum(bunch_of_inputs)}')


n=int(input('Enter how many numbers to operate on: '))
bunch_of_inputs=[]
for i in range(n):
   bunch_of_inputs.append(int(input(f'Enter {i+1} value: ')))

max_of_all_numbers_and_sum_of_all_numbers(bunch_of_inputs)


'''
Kwargs example: 
calling kwargs should be with **
'''

# def display_kwargs(**kwarg_parameter):
#     print(kwarg_parameter)

# display_kwargs(a=1,b=2,c=3,d=4,e=5)



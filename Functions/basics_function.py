'''
In mathematics
    y=f(x)
    x= input of a function 
    y= output of a function

    int function_name(int1,int2)
    {
        return int1+int2;
    }

#1 function definition: 
    defining function and its actions
#2 function call:
    calling that specific function

'''
#print(a+b)
#range(0,10)

#No return type functions
#Function def inition: 
# def name_of_function (arguments/parameters)
def sum_of_2_numbers(a,b):
    print(a+b)

#Function call

#sum_of_2_numbers(1,2)

'''
create a function named calculations
calculations arguments= a,b, flag 
if flag=1, a+b, flag=2 a-b flag=other then 1 and 2 print cant perform random 
operation
'''
'''
#Simran Tamang's Code
def calculations(a,b,flag)
   if(flag == 1):
        print(a + b)
    elif(flag == 2):
        print(a - b)
    else:
        print("Cant perform random operation")

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
flag = int(input("Enter 1 for add and 2 for subtarction: "))
calculations(a, b, flag)
'''
#Anu Sapkota's Code 
def calculations(a, b, flag):
  if (flag==1):
    print(f'Sum: {a+b}')
  elif (flag==2):
    print(f'Difference: {a-b}')
  else:
    print('Cant perform random operation')

# x=int(input('Enter first number: '))
# y=int(input('Enter second number: '))
# z=int(input('Enter flag: '))
# calculations(x, y, z)
    

#Return cases:
'''
y=f(x) f(x),
int main()
{
    return 0;
}

'''
#sum of  2 numbers but this time return results to the main program

def sum_of_2_numbers(a,b):
  #sum=a+b
  #return sum
  return a+b

# addition works as y in the case of y=f(x), so it gets the value a+b
addition=sum_of_2_numbers(1,2)
#print(a+b)

'''
take input from user, 
convert that string to integer by creating a function convert_to_integer
then add the 2 numbers passing to another function named addition_of_2_numbers

convert_to_integer(any)-> int
addition_of_2_numbers(int,int)-> None (Prints output inside the function only)

'''
'''
def convert_to_integer(a):
  return int(a)

def addition_of_2_numbers(a,b):
  print(a+b)

'''


# x=convert_to_integer(input('Enter first number: '))
# y=convert_to_integer(input('Enter Second number: '))
# addition_of_2_numbers(x,y)

'''
#Shraddha Pahari's Code
def addition_of_2_numbers(a,b):
    sum=a+b
    print(f"Addition of {a} and {b} is {sum}")

def convert_to_integer(a,b):
    a=int(a)
    b=int(b)
    addition_of_2_numbers(a,b)


a=input("Enter the first number:")
b=input("Enter the second number:")
convert_to_integer(a,b)
'''



#Nested Function:
'''
g(x)=h(y)
z=g(y)
function within a function
#define funtion first 
def addition_of_2_numbers(a,b):
    #Nested Function Definition
    def another_function(c):
        return int(c)
    #Nested Function Call
    another_function()
    print(a+b)
#then call function
addition_of_2_numbers(1,2)
    
addition_of_2_numbers(a,b)
{
    convert_to_integer(x)
    {
        return int(x)
    }
    a=convert_to_integer(a)
    b=convert_to_integer(b)
    print(a+b)
}
convert this pseudo code into python code 
convert_to_integer(any) -> integer type
addition_of_2_numbers(any,any) -> None (displays sum of 2 numbers )
'''
#Parent Function definition
def addition_of_2_numbers(a,b):
  
  #Nested Child Function Definition
  def convert_to_integer(x):
    return int(x)
 
  #Nested Child Function Call
  a=convert_to_integer(a)
  b=convert_to_integer(b)
  print(a+b)

# a1=input('Enter first number: ')
# #Understanding the scope of convert_to_integer()
# #a1=convert_to_integer(a1)

# a2=input('Enter second number: ')
# addition_of_2_numbers(a1,a2)


'''
learn about lamda functions
learn about args and kwargs,
learn about default arguemnts setup
'''
'''
Lamba function: inline function

def function_name(arguments):
  operations
  return final_value

functioN_name(parameter)

In single line can we call define a function and also call it 
'''
#x_function=lambda x:x.replace(' ','-') #function_lambda(x): return x.replace(' ','-')
#print(x_function('Siddhant Sharma'))


#Write a lambda function to give a square of a particular number:
''''
square_it_function(any)-> int (int= (int(any))**2) (^,**)
It should be lambda function
'''
# square_it=lambda x: (int(x))**2
# x_input=int(input('Enter x: '))
# x_squared=square_it(x_input)
# print(x_squared)

'''
Advantage: 

Effective reuse of variables, and function
Can save multiple lines of code

Disadvantage:

difficult to use for very complex functions
'''

'''
Task 1: Create a lambda function to take 2 argumments and return the sum of 2 arguments:
sum_lambda(x(int),y(int)) -> int (operation = x+y)
'''
#Anyone trying to debug this please solve it 
# sum_of_2_number = lambda x,y: int(x+y)
# a= input("Enter a:")
# b= input("Enter b:")
# print(sum_of_2_number(int(a),int(b)))

'''
Task 2: Create a lambda function to take 1 argument and return 1 if its even, 0 if its odd
check_even(x(int)) -> int/bool (opeartion = check if even)
'''

# check_even=lambda x: True if (x%2==0) else False
# print(check_even(int(input('Enter any number: '))))

'''
check_even = lambda x: x % 2 == 0
check_odd = lambda x: x % 2 != 0


print(check_even(4))  
print(check_odd(5))

'''

def check_even(x=10):
  print(x)
  if x%2==0:
    return True
  else: 
    return False

#x_input=int(input('Enter variable: '))
#check_even(x_input)
#check_even(15)

'''
Task: Create a function display_multiplication_table that takes an arugement and displays multiplication table of that arugment
if nothing is passed that function should show the multiplication table of 5

display_mul_table(10):

10 x 1 = 10
10 x 2 = 20
10 x 3 = 30
.
.
10 x 10 = 100
'''

def display_multiplication_table(argument_value=5,multiply_till=10):
  for i in range(1,multiply_till+1):
    print(f'{argument_value} x {i} = {argument_value*i}')

#display_multiplication_table(8,5)

'''
Args: 
send as many parameters as tuple so we want and our system should be able to handle it 

kwargs: 
send as many parameters as dictionary so we want and our system should be able to handle it 

#for these usecases args and kwargs are best

def random_function(a,b,c=3):
  pass

random_function(1,2,3,4,5,6,7,8,9,)

'''

'''
Task 1: 
let's have a function named counter
counter(n number of input) -> total odds and total evens
'''
def counter(*x):
  odd_counter=0
  even_counter=0
  for number in x: 
    if number%2==0:
      even_counter+=1
    else:
      odd_counter+=1
  
  return even_counter,odd_counter
    

#total_even_numbers,total_odd_numbers=counter(1,2,3,4,5)
#print(f'total even numbers: {total_even_numbers}\ntotal odd numbers: {total_odd_numbers}')



'''
Task 2 let's have a function named adder
adder(n number of input) -> total sum of all numbers
'''

def adder(*x):
  total_sum=0
  for number in x:
    total_sum+=number

  return total_sum

print(adder())

'''
kwargs= key word arguments 
try it out yourself 
** x

'''
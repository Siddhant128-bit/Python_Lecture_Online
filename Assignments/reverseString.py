'''
Reverse a String: Write a function that takes a string as input and returns the string reversed. 
For example, if the input is "hello", the output should be "olleh".

reverse_string_approach_1(any)  -> None (display)
reverse_string_approach_2(any)  -> None (display)

approach 1 using loop
approach 2 not using loop (look up from internet)

'''

#approach 1 using loop

def reverse_string_approach_1(input_string):
  temp=""
  for i in input_string :
    temp=i+temp
  return temp
      
input_string=input("Enter an string:")
result=reverse_string_approach_1(input_string)

print(f"Using Approach 1:\nOriginal String:{input_string} \nReversed String:{result}")

# approach 2 not using loop (look up from internet)
result=input_string [::-1]
print(f"\nUsing Approach 2:\nOriginal String:{input_string} \nReversed String:{result}")

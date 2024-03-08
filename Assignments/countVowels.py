'''
Count Vowels in a String: Write a function that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string. 
For example, if the input is "hello", the output should be 2.
using loop
'''
vowels=["a","e","i","o","u"]

def countVowels(input_string,v):
  count=0
  for i in input_string :
    for j in v:
     if (i==j):
       count+=1
  return count
      
input_string=input("Enter an string:").lower()
result=countVowels(input_string,vowels)
print(f"IN given string:{input_string}\n number of vowels:{result}")

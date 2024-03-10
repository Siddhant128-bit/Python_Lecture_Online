'''
Check Palindrome: Write a function that checks if a given string is a palindrome. 
A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward. 
For example, "radar" is a palindrome.
'''

def palindrome(input_string):
  temp=input_string [::-1]
  if temp==input_string:
    return 1
      
input_string=input("Enter an string:")
result=palindrome(input_string)
print(f"Given string:{input_string} ")
print(f" IS Palindrome "if result==1 else " Not Palindrome")
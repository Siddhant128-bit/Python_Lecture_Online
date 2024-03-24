'''
Reverse a String: Write a function that takes a string as input and returns the string reversed. 
For example, if the input is "hello", the output should be "olleh".
reverse_string_approach_1(any)  -> None (display)
reverse_string_approach_2(any)  -> None (display)

approach 1 using loop
approach 2 not using loop (look up from internet)

Reverse a String: Write a function that takes a string as input and returns the string reversed. 
For example, if the input is "hello", the output should be "olleh".


def reverse_string(input_string):
    temp = ''
    for s in range(len(input_string)-1,-1,-1):
        temp = temp + input_string[s]
    return temp

input_string = input("Enter string to reverse: ") 
# print(f"Reverse string of {input_string} is {reverse_string(input_string)}") 

# approach 2
print(f"Reverse string of {input_string} is {input_string[::-1]}") 

'''

'''

Count Vowels in a String: Write a function that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string. 
For example, if the input is "hello", the output should be 2.
using loop


def count_vowels(input_string) :
    vowels = 0
    for s in input_string.lower():
        if(s == 'a' or s =='e' or s=='i' or s=='o' or s=='u'):
            vowels += 1
    return vowels

input_string = input("Enter a string: ")
print(f"Number of vowels in {input_string} is {count_vowels(input_string)}")

'''

'''

Check Palindrome: Write a function that checks if a given string is a palindrome. 
A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward. 
For example, "radar" is a palindrome.


def check_palindrome(input_string):
    reverse_string = input_string[::-1]

    if(input_string.lower() == reverse_string.lower()):
        return "True"
    else:
        return False

input_string = input("Enter a string: ")
print("Yes, the string is Palindrome " if(check_palindrome(input_string)) else "No, string is not")
'''
'''

String Anagrams: Write a function that checks if two strings are anagrams of each other. 
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once. 
For example, "listen" and "silent" are anagrams.
"eye", "yee"


def check_anagrams(input_string1,input_string2) -> bool:
    if(sorted(input_string1) == sorted(input_string2)):
        return True
    else:
        return False
    
input_string1 = input("Enter first  Strings: ").lower()
input_string2 = input("Enter Second  Strings: ").lower()

if(check_anagrams(input_string1, input_string2)):
    print(f"{input_string1} and {input_string2} are anagrams")
else:
    print(f"{input_string1} and {input_string2} are not anagrams")




'''
'''
#Optional Try your best
Longest Substring Without Repeating Characters: Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating characters in "abcabcbb" is "abc", 
which has a length of 3.
'''

def cal_substring(input_string):
    maxLen = 1
    substring= ''
    for char in input_string:
      if substring.count(char)==0:
        substring = substring + char
      else:
         pass
    print(f'The longest substring of the given text is: {substring}')


input_string = input("Enter a string: ")
cal_substring(input_string)






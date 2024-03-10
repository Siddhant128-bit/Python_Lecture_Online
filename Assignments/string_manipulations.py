# Question 1

'''
Reverse a String: Write a function that takes a string as input and returns the string reversed. 
For example, if the input is "hello", the output should be "olleh".

reverse_string_approach_1(any)  -> None (display)
reverse_string_approach_2(any)  -> None (display)

approach 1 using loop
approach 2 not using loop (look up from internet)
'''
#Approach 1
def reverse_string_approach_1(input_str):
    reversed_str = " "            #to store empty reversed string
    for char in input_str:
        reversed_str = char + reversed_str
    print("The reverse string is:", reversed_str)

input_str = input("Enter Your Input: ")
print("The given string is: ",input_str)
print("The reverse string is: ",reverse_string_approach_1(input_str))


#Approach 2
# put extended slice in a function

def reverse_string_approach_2(input_str):
    reversed_str =  input_str[::-1]            # “-1” denotes starting from the end and stop at the start
    print("The reverse string is:", reversed_str)

input_str = input("Enter Your Input: ")
print("The given string is: ",input_str)
print("The reverse string is: ",reverse_string_approach_2(input_str))


# Question 2
''''
Count Vowels in a String: Write a function that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string. 
For example, if the input is "hello", the output should be 2.
using loop
'''

def count_vowels(input_str):
    vowels = ['a','e','i','o','u']
    count = 0
    
    for char in input_str.lower():
        if char in vowels:
            count += 1
            
    return count

input_str = input("Enter a string: ")
print("You have entered: ",input_str)
number = count_vowels(input_str)
print("The number of vowels in given string is: ",number)
        


# Question 3
'''
Check Palindrome: Write a function that checks if a given string is a palindrome. 
A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward. 
For example, "radar" is a palindrome.
'''

def is_Palindrome(input_str):
    return input_str == input_str[::-1]    #checks from last to first & compare

input_str = input("Enter a string: ")
if is_Palindrome(input_str):
    print(f"{input_str} is a palindrome.")
else:
    print(f"{input_str} is not a palindrome.")


# Question 4
'''
String Anagrams: Write a function that checks if two strings are anagrams of each other. 
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once. 
For example, "listen" and "silent" are anagrams.
'''

def are_anagrams(string1, string2):
 
        if sorted(string1) == sorted(string2):
            return True
        else:
            return False
 
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_anagrams(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")


# Question 5
#Optional Try your best
'''
Longest Substring Without Repeating Characters: Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating characters in "abcabcbb" is "abc", 
which has a length of 3.
'''
def longest_substring_without_repeating(s):
    l = r = 0
    longest_substring = ""
    current_substring = ""
    last_char_index = {}

    while r < len(s):
        if s[r] not in last_char_index or last_char_index[s[r]] < l:
            last_char_index[s[r]] = r
            current_substring += s[r]
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
            r += 1
        else:
            l = last_char_index[s[r]] + 1
            current_substring = ""

    return len(longest_substring), longest_substring


input_str = input("Enter a string: ")
length, result = longest_substring_without_repeating(input_str)
print("Length of the longest substring without repeating characters:", length)
print("The longest substring without repeating characters is:", result)

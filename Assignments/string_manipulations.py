#\queston 1
'''
Reverse a String: Write a function that takes a string as input and returns the string reversed. 
For example, if the input is "hello", the output should be "olleh".



reverse_string_approach_1(any)  -> None (display)
reverse_string_approach_2(any)  -> None (display)

approach 1 using loop

#reverse string using loop
'''

def reverse_string_approach_1(input_string):
    reversed_str=''
    
    for char in input_string:
        reversed_str=char + reversed_str
    return reversed_str
    
string='kaskikot'
reversed_str=reverse_string_approach_1(string)
print(reversed_str)
    
''' 
approach 2 not using loop (look up from internet)
'''
#without using loop

def reverse_string_approach_2(input_string):
  return input_string[::-1]

string="kaskikot"
reversed_str=reverse_string_approach_2(string)
print(reversed_str)

#questionNo.2
'''
Count Vowels in a String: Write a function that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string. 
For example, if the input is "hello", the output should be 2.
using loop
'''

def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

input = "Shequal project"
vowel_count = count_vowels(input)
print(" Total number of vowels are:", vowel_count)  

'''
Check Palindrome: Write a function that checks if a given string is a palindrome. 
A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward. 
For example, "radar" is a palindrome.
'''
def is_palindrome(input_string):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    # Compare cleaned string with its reverse
    return cleaned_string == cleaned_string[::-1]

string_input = "madam"
print(is_palindrome(string_input))  

'''String Anagrams: Write a function that checks if two strings are anagrams of each other. 
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once. 
For example, "listen" and "silent" are anagrams.
'''
def string_anagrams(string1, string2):
    # Removing non-alphanumeric characters and convert to lowercase
    cleaned_str1 = ''.join(char.lower() for char in string1 if char.isalnum())
    cleaned_str2 = ''.join(char.lower() for char in string2 if char.isalnum())
    
    return sorted(cleaned_str1) == sorted(cleaned_str2)

str1 = "listen"
str2 = "silent"
print(string_anagrams(str1, str2)) 


# By  take input from user

def string_anagrams(string1, string2):
 
    cleaned_str1 = ''.join(char.lower() for char in string1 if char.isalnum())
    cleaned_str2 = ''.join(char.lower() for char in string2 if char.isalnum())
    
    return sorted(cleaned_str1) == sorted(cleaned_str2)

def check_anagrams():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    if string_anagrams(str1, str2):
        print("The strings are anagrams of each other.")
    else:
        print("The strings are not anagrams of each other.")

check_anagrams()


'''#Optional Try your best
Longest Substring Without Repeating Characters: Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating characters in "abcabcbb" is "abc", 
which has a length of 3.
'''
def longest_substring_length(input_string):
    # Initialize variables
    max_length = 0
    start = 0
    char_index_map = {}

    # Iterate through the string
    for i, char in enumerate(input_string):
        # If the character is already in the map and its index is after the start of the current substring
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1

        # Update the index of the current character
        char_index_map[char] = i

        # Calculate the length of the current substring
        current_length = i - start + 1

        # Update the maximum length
        max_length = max(max_length, current_length)

    return max_length


input_str = "abcabcbb"
print(longest_substring_length(input_str))  

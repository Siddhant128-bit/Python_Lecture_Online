#Question1:
'''
Reverse a String: Write a function that takes a string as input and returns the string reversed. 
For example, if the input is "hello", the output should be "olleh".

reverse_string_approach_1(any)  -> None (display)
reverse_string_approach_2(any)  -> None (display)

approach 1 using loop
approach 2 not using loop (look up from internet)
'''

#Approach 1:
print('REVERSE YOUR TEXT(APPROACH 1)')
u_input1 = input('Enter your text: ')

def reverseStringApproach1(any):
  reversedString = ''
  for x in any:
    reversedString = x + reversedString
  print(f'Reversed string: {reversedString}')

reverseStringApproach1(u_input1)
 
#Approach 2:
print('REVERSE YOUR TEXT(APPROACH 2)')
u_input2 = input('Enter your text: ')

def reverseStringApproach2 (str):
   print(f'Reversed string: {str[::-1]}')

reverseStringApproach2(u_input2)

#Question2:
'''
Count Vowels in a String: Write a function that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string. 
For example, if the input is "hello", the output should be 2.
using loop
'''
print('COUNT THE VOWELS IN YOUR TEXT')
u_input3 = input('Enter your text: ').lower()

def vowelCounter(any):
  vowels = ['a', 'e', 'i', 'o', 'u']
  NumberOfVowels = 0
  for vowel in vowels:
    if vowel in any:
      NumberOfVowels+= any.count(vowel)
  
  print(f'Number Of Vowels: {NumberOfVowels}')

vowelCounter(u_input3)

#Question3: 
'''
Check Palindrome: Write a function that checks if a given string is a palindrome. 
A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward. 
For example, "radar" is a palindrome.
'''
print('CHECK IF TWO TEXTS ARE PALINDROME')
u_input4 = input('Enter your text: ')

def checkPalindrome(any):
  reversedString = ''
  for x in any:
    reversedString = x + reversedString
  if reversedString == any:
    print(f'{any} is a Palindrome')
  else:
    print(f'{any} is not a Palindrome')

checkPalindrome(u_input4)

#Question4:
'''
String Anagrams: Write a function that checks if two strings are anagrams of each other. 
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once. 
For example, "listen" and "silent" are anagrams.
'''
print('CHECK IF THE TWO TEXTS ARE ANAGRAMS')
u_input5 = input('Enter your first text: ')
u_input6 = input('Enter your second text: ')

def checkAnagram(any1, any2):
  any1 = any1.lower()
  any2 = any2.lower()

  if len(any1) != len(any2):
    print(f'{any1} is not an Anagram of {any2}')
    return
  
  charCountAny1 = {}
  charCountAny2 = {}

  for char in any1 :
    charCountAny1[char] = any1.count(char)

  for char in any2:
    charCountAny2[char] = any2.count(char)

  if charCountAny1==charCountAny2:
    print(f'{any1} is an Anagram of {any2}')
  else:
    print(f'{any1} is not an Anagram of {any2}')
   
checkAnagram(u_input5, u_input6)

#Question5:
'''
#Optional Try your best
Longest Substring Without Repeating Characters: Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating characters in "abcabcbb" is "abc", 
which has a length of 3.
'''
print('FIND THE LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS')
u_input7 = input('Enter your text: ')

def longestSubstring(any):
  substring= ''
  for char in any:
    if substring.count(char)==0:
     substring = substring + char
    else:
      pass
  print(f'The longest substring of the given text is: {substring}')

longestSubstring(u_input7) 

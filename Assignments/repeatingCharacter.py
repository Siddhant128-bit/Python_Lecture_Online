'''
#Optional Try your best
Longest Substring Without Repeating Characters: Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating characters in "abcabcbb" is "abc", 
which has a length of 3.
'''

def longestSubstring(input_string):
  substring= ''
  for char in input_string:
    # print(substring.count(char))
    if substring.count(char)==0:
     substring = substring + char
  return substring

input_string=input("Enter an string:")
result=longestSubstring(input_string) 
print(f'The longest substring without repeating characters in {input_string} is: {result}.which has a length of {len(result)}.')

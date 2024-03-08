'''
String Anagrams: Write a function that checks if two strings are anagrams of each other. 
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once. 
For example, "listen" and "silent" are anagrams.
'''

'''
def anagrams(input_string1,input_string2):
  count1 = {}
  count2 = {}
  for i in input_string1:
    count1[i] = count1.get(i, 0) + 1
  for j in input_string2:
    count2[j] = count2.get(j, 0) + 1
  if len(input_string1) != len(input_string2):
    return 0
  if count1==count2:
    return 1
'''

def anagrams(input_string1,input_string2):
   if sorted(input_string1) == sorted(input_string2):return 1

input_string1=input("Enter an 1st string:").lower().replace(" ", "")
input_string2=input("Enter an 2nd string:").lower().replace(" ", "")

result=anagrams(input_string1,input_string2)
print(f"Given string:{input_string1} and {input_string2}")
print(f" IS Anagrams "if result==1 else " Not Anagrams")

# Another method
    # if sorted(input_string1) == sorted(input_string2):return 1

'''
String handling deals with taking string input
iteratiing over string input 
modifying string input and so on
'''
'''
storage_string='My name is Siddhant'
print(storage_string)

'''
storage_string_input=input('Enter Storage String: ')
print(storage_string_input)

# converting string to list: 

#Approach 1, character wise conversion: 

#storage_string_input=list(storage_string_input)
#print(storage_string_input)

#Approach 2, word wise conversion: 
'''
storage_string_input=storage_string_input.split('-')
print(storage_string_input)
'''

#Task 1: From any user input calculate total number of characters and words:
# len(list_val) -> total number of elements of list

user_input=input('Enter your text: ')

#without conversion to list: 
#print(len(user_input))

#with conversion to list: 
print(f'Number of characters: {len(list(user_input))}')


#total number of words in string: 
print(f'Number of words: {len(user_input.split(' '))}')

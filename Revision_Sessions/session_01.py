'''
list operations

list ma add garna append use garinxa 
it adds at the end of the list 
list are denoted using []
'''

# list_of_elements=[1,2,3,4,5,7,9]
# print(list_of_elements)

'''
accessing any element in list is done using index 0,1,2,3,4,5
list_of_elements[5]
index can be accessed in reverse order -1,-2,-3,-4,-5
'''

# print(f"First Element: {list_of_elements[0]}")
# print(f"Last Element: {list_of_elements[-1]}")

'''
Loop over a list titled 
list_of_elements=[1,2,3,4,5]
add each element with their index value

[1,2,3,4,5] -> [1+0,2+1,3+2,4+3,5+4]
[0,1,2,3,4]
'''

# list_of_elements=[1,2,3,4,5]
# output_list=[]
# print(list_of_elements)

# for index in range(0,len(list_of_elements)):
#     output_list.append(index+list_of_elements[index])

# print(output_list)


'''
Task 1: Write a program that takes input from user as n
and loops over a list titled list_of_elements=[1,2,3,4,5]
if n< list_of_elements: print(sum of all elements upto nth element)
else print(invalid)
'''
# Approach 1 Looping approach:

list_of_elements=[1,2,3,4,5]
# n=int(input('Enter value of n: '))

# if n>=len(list_of_elements): 
#     print('Invalid')
# else:
#     sum_of_elements=0
#     for index in range(0,n):
#         sum_of_elements=sum_of_elements+list_of_elements[index]
    
#     print(f'Looping approach sum of all elements upto {n}: {sum_of_elements}')


#Approach 2 List Slicing approach
# print('Slicing Results: ')
# print(sum(list_of_elements[0:n]))    

#Inbuilt operator in python
# sum(collection_of_variables)-> int sum of all elements 

'''
Task 2: Take n from user and display all the elements upto nth term or nth index using index slicing 
'''
# list_of_elements=[1,2,3,4,5]
# print(list_of_elements)
# n_th_term=int(input('Enter nth term: '))
# print(list_of_elements[0:n_th_term])

# print(list_of_elements[0:n_th_term+1])


'''
Dictionary: 
{
    'keys_1' : "values_1",
    'keys_2' : "values_2",
    'keys_3' : "values_3",
    'keys_4' : "values_4",
}

dictionary is denoted with 'curly braces'
'''

traditional_dictionary={
    'apple': 'A red colored fruit which is good for health',
    'aeroplane': 'A manmade object that can fly',
    'ball': "a round object that can be used as play thing",
    "cat": "An animal that makes meow sound"
}


# print(traditional_dictionary['apple'])
# print(traditional_dictionary['ball'])
# print(traditional_dictionary['cat'])

'''
traditional_dictionary_dynamic jasma hamile word dinxam tesko meaning dinxam ani affai euta dictionary banxa 
word kati ota diney vanera chahi nth word
'''
# calender={}
# n_th_word=int(input('Enter how many events to be stored in dictionary: '))

# for i in range(n_th_word):
#     key_event=input(f'Enter {i+1}th event: ')
#     event_date=input(f'Enter {key_event} word date: ' )
#     #how to add on empty dictionary: 
#     calender[key_event]=event_date

# print(calender)
# searching_event=input('Enter event you are searching: ')

# if searching_event in calender.keys():
#     print('event Found')
#     print(calender[searching_event])
# else:
#     print('Not Found ')

'''
Task 3: WAP, first collect important events for you, then it takes in corresponding dates put it in dictionary 
then look up specific event and get me that event's date
'''

print("how's you ?")

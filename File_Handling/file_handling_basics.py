'''
File Handling 
-> Think of it as a bucket.
-> Running water is just a running code.
-> Lite Database or Database itself.

File Handling Consists of 2 parts 
1. Dumping information to a file for later use.
2. Retrieving information from a file in later use.

Suppose you have created an app where there is sing up page.
You dont want same user to sign up again and again.
So you can save the sign up users somewhere where it won't be deleted
then you can just retrieve the stored information to validate if its the same user.
'''



#Use case 1. take username and password during sign up and use it for sign in purposes.
import getpass

def sign_up():
    user_name=input('Enter username to register: ')
    password=getpass.getpass('Enter password:')
    birthday=input('Enter your birthday: ')
    #Approach 1 (Old Style not much used these days)
    #File handling core code starts here.
    # database_file=open('database.txt','w') #write, read, append
    # database_file.write(user_name+' '+password+' '+birthday)
    # database_file.close()
    #File handling core code ends here.

    #Approach 2 (New and Standard approach)
    #Dumping of file
    with open('data_base.txt','a') as f:
        f.writelines(user_name+' '+password+' '+birthday+'\n')
    
def sign_in():

    #Retrieving from file 
    #File handling core code starts here
    with open('data_base.txt','r') as f:
        database_info=f.readlines()
    #File handling core code ends here
        
    print(database_info)
    check_user_name=input('Enter username: ')
    check_pass_word=input('Enter password: ')
    if (check_user_name in database_info) and (check_pass_word in database_info):
        print('User Found')
        #Also print that user's birthday
    else: 
        print('Not Found')
    
choice=int(input('Enter choice: \n1. Sign Up: \n2. Sign In:  '))
infromation_account=[]
if choice==1:
    sign_up()
else: 
    sign_in()


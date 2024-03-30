import json,getpass
# Sign up with multiple users.
'''
json file should be something like this :
{
    'user_1/username':{
        'name': username,
        'password': password,
        .
        .
        .
    },
    'user_2/username': {
        .
        .
        .

    }
}
'''
def sign_up():
    #load previous json file here as entire_database variable
    #Loaded Previous json File: 
    try:
        with open('json_database.json','r') as f:
            entire_database=json.load(f)
    except:
        entire_database={}

    name_of_user=input('Enter name of user: ')
    password=getpass.getpass('Enter password: ')
    dob=input('Enter your date of birth: ')
    fav_color=input('Enter your fav color: ')
    
    sign_up_dictionary={
        'name': name_of_user,
        'password': password,
        'DOB': dob,
        'fav-color': fav_color,   
    }
    # dictionary update signup dictionary onto the entire_database variable
    entire_database.update({f'{name_of_user}': sign_up_dictionary})
    with open('json_database.json','w') as f:
        json.dump(entire_database,f)
        #save the updated entire_database variable
    print('Sign up Successful')

#Scan through the entire json file and lookout the username and password and repeat the same process.
def sign_in():
    with open('json_database.json','r') as f:
        entire_database=json.load(f)
    user_name=input('Enter your username: ')
    password=getpass.getpass('Enter your password')
    
    all_users=entire_database.keys()
    if user_name in all_users: 
        data_database=entire_database[user_name]
        if password==data_database['password']:
            print("login successful")
            name=data_database['name']
        color=data_database['fav-color']
        print(f'Hello {name} \nYour Fav Color is {color}')
    else: 
        print('Unathourized entry ')
    
if __name__=='__main__':
    print('Welcome to our app: Enter 1 for sign up and 2 for sign in')
    choice=int(input('>> '))
    if choice==1: 
        sign_up()
    else: 
        sign_in()





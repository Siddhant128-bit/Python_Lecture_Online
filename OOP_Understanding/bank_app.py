'''
Replicate online banking system

Create a banking app, In which you can register an account with your information
1. take username, dob and balance that he/she has 
2. Create a skeleton Banking App, That can be used to create different accounts
'''
import getpass

class Bank_APP:
    def __init__(self,user_name_parameter,password_parameter,dob_parameter,balance_parameter):
        self.user_name=user_name_parameter
        self.password=password_parameter
        self.dob=dob_parameter
        self.bank_balance=balance_parameter
    

    def deposit_amount(self,deposited_amount_information):
        self.bank_balance+=float(deposited_amount_information)

    def withdraw_amount(self,withdrawn_account_information):
        self.bank_balance-=withdrawn_account_information

def create_users(all_accounts_list=[]):
    N_users=int(input('Enter N: '))
    for i in range(N_users):
        user_name_dyanmic=input('Enter username: ')
        password=getpass('Password: ')
        DOB_dynamic=input('Enter Date of Birth: ')
        balance_dynamic=float(input('Enter Balance: '))
        all_accounts_list.append(Bank_APP(user_name_dyanmic,password,DOB_dynamic,balance_dynamic))
    return all_accounts_list

def authenticate_and_Account_Page(all_info):
    '''
    Project Code here Make it so a person with correct username and password logs into the account
    Also each user must have unique greeting page and also should have their unique balance number shown
    Allow the feature to transfer money to someone else's account. 
    Enter username of someone whom you want to send money 
    Enter amount and based on the amount 
    withdraw from sender's account and deposit to reciever's account.
    '''
    pass


def main_app():
    print('Welcome to XYZ Bank')
    choice_main=int(input('Enter your choice: \n1.Create Users (Admin): \n2.Login to your account: \n3.Quit Account: '))
    all_users=[]
    if choice_main==1:
        all_users=create_users(all_users)
    elif choice_main==2:
        authenticate_and_Account_Page(all_users)
    elif choice_main==3:
        return False

if __name__=='__main__':
    while True:
        flag=main_app()
        if flag==False: 
            break

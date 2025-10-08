# design a bank system where a person can open bank account with following attributes: firstname,lastname,age,balance=0. method: check_balance() 
# deposit_balance():check for negative value,withdraw_balance():check_insufficient_value
# has a interest rate of 12%, check_interest(),update_interest()
# display governments holiday's list
# write code to implement above class

class BankAccount:
    __interest_rate = 12

    def __init__(self,first_name,last_name,age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__balance = 0

    def check_balance(self):
        return self.__balance
    
    def deposit_balance(self,balance):
        if balance > 0 :
            self.__balance = balance
        else:
            print("The deposit must be more than 0.")
    
    def withdraw_balance(self,withdrawal_amount):
        if withdrawal_amount <= self.__balance and withdrawal_amount>0:
            self.__balance -= withdrawal_amount
            print(f"You have successfully withdrawed {withdrawal_amount}")
        elif withdrawal_amount < 0:
            print("You have entered invalid amount")
        else:
            print(f"You have insufficient amount.")
    
    @classmethod
    def check_interest_rate(cls):
        return cls.__interest_rate
    
    @classmethod
    def update_interest_rate(cls, rate):
        cls.__interest_rate = rate
    
    @staticmethod
    def display_holidays():
        try:
            holidays = open('holidays_file.txt')
            print("*"*50)
            print("The holidays are: ")
            for lines in holidays.readlines():
                print(lines.strip())
            
        except FileNotFoundError:
            print("The file doesnt exist")

    def add_record(self):
        try:
            account_record = open('record.txt','r+')
            for lines in account_record.readlines():
                account = lines.split(';')
                if self.__first_name==account[0] and self.__last_name == account[1]:
                    raise Exception("The account already exists")
            info = f'\n{self.__first_name};{self.__last_name};{self.__age};{self.__balance}'
            account_record.write(info)
            print(f'You have successfully created an bank account! Congratulations {self.__first_name} {self.__last_name}.')
            account_record.close()
        except Exception as e:
            print(e)

    def update_record(self):
        
            info = ''
            account_record = open('record.txt','r')
            for lines in account_record.readlines():
                account = lines.split(';')
                if self.__first_name!=account[0] or self.__last_name != account[1]:
                    info = info+ f'{account[0]};{account[1]};{account[2]};{account[3]}'
            info = info+ f'{self.__first_name};{self.__last_name};{self.__age};{self.__balance}' 
            print(info) 
            account_record.close()
            account_record = open('record.txt','w')
            account_record.write(info)
            account_record.close()
        




        
menu = True
while menu:
    print('*'*25+'MENU'+'*'*25)
    print('1. Register')
    print('2. Sign in')
    print('3. Quit')
    print('*'*50)
    option = input('Enter a choice: ')
    if option not in ['1','2','3']:
        print("Invalid Option")
    elif option == '1':
        first_name = input("Enter your first name: ").lower().capitalize()
        last_name = input("Enter your last name: ").lower().capitalize()
        while True:
            age = int(input("Enter your age: "))
            if age>18:
                break
            elif age>0:
                print("You are not eligible for a bank account")
                menu = False
                break
            else:
                print("You have provided an invalid age! ")
        account = BankAccount(first_name,last_name,age)
        account.add_record()
        amount = int(input("Please enter the amount of money you want to deposit: "))
        account.deposit_balance(amount)
        account.update_record()
        del(account,amount,first_name,last_name)
        while True:
            answer = input('Would you like to quit?(Y/N)').lower() 
            if answer == 'y':
                menu = False
                break
            elif answer == 'n':
                break
            elif answer != 'n':
                print("Invalid Choice!!")
    elif option == '2':
        try:
            account_record = open('record.txt')
            print("*"*50)
            f_n = ((input("Please enter your first name :")).lower()).capitalize().strip()
            l_n = ((input("Please enter your last name :")).lower()).capitalize().strip()
            account= None
            account_record = open('record.txt','r+')
            authentication = False
            for lines in account_record.readlines():
                account = lines.split(';')
                if f_n==account[0] and l_n == account[1]:
                    authentication = True
                    break
            user_account = BankAccount(account[0],account[1],int(account[2]))
            user_account.deposit_balance(int(account[3]))
            if not authentication:
                print("No such user!!")
            
            
            while authentication:
                print(f'Hello {f_n} {l_n}')
                print('*'*25+'MENU'+'*'*25)
                print('1. Withdraw Money')
                print('2. Check Balance')
                print('3. Deposit Money')
                print('4. Go to main menu')
                print('*'*50)
                option = input('Enter a choice: ')
                if option not in ['1','2','3','4']:
                    print("Invalid Option")
                elif option == '1':
                    user_account.withdraw_balance(int(input('Please enter the amount you want to withdraw: ')))
                elif option == '2':
                    print(f'You currently have Rs.{user_account.check_balance()}')
                elif option == '3':
                    amount = int(input('Please enter the amount you want to deposti: '))
                    user_account.deposit_balance() 
                    print(f"You have successfully deposited {amount}")  
                elif option == '4':
                    break

            
        except FileNotFoundError:
            print("The file doesnt exist")
        
          




        

    




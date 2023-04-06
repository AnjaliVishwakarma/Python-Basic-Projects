class ATM:
    __key = '12345'
    __list = []

    def __init__(self):

        # constructor
        self.__pin = ''
        self.__balance = 0
        self.__name = ''
        self.__mobile = ''
        # ATM.list.append(self)

    def create_pin(self):
        self.__pin = input('Enter your pin: ')
        self.__balance = int(input('Enter balance: '))
        self.__name = input('Enter Name: ')
        self.__mobile = input('Enter mobile: ')
        ATM.__list.append(self)
        # return 'pin created successfully'

    def deposit(self):
        flag = False
        temp = input('Enter your pin: ')
        for i in ATM.__list:
            if temp == i.__pin:
                amount = int(input('Enter the amount: '))
                i.__balance = i.__balance + amount
                print('Deposit Successfully')
                flag=True
        else:
            if flag == False:
                print('Invalid pin')

    @classmethod
    def set_pin(cls):
        flag=False
        name = input('Your name: ')


        for i in ATM.__list:
            if name == i.__name:
                mobile = input('Your mobile number: ')
                if mobile == i.__mobile:
                    new_pin = input('Enter new pin: ')
                    i.__pin=new_pin
                    print('Successful pin update')
                    flag=True
                else:
                    flag=True
                    print('invalid mobile number')
        else:
            if flag==False:
                print('name not exist')

    @classmethod
    def get_pin(cls):
        flag = False

        name = input('Your name: ')

        for i in ATM.__list:
            if name == i.__name:
                mobile = input('Your mobile number: ')
                if mobile == i.__mobile:
                    print('your pin:',i.__pin)
                    flag =True
                else:
                    print('invalid mobile number')
                    flag = True

        else:
            if flag==False:
                print('no name exist')




    def withdraw(self):
        flag=False
        temp = input('Enter your pin: ')
        for i in ATM.__list:
            if i.__pin == temp:
                amount = int(input('Enter the amount: '))
                if amount < i.__balance:
                    i.__balance = i.__balance - amount
                    print( 'Operation Successful')
                else:
                    print('insufficient fond')
            flag = True
        else:
            if flag == False:
                print('Invalid pin')


    def check_balance(self):
        flag=False
        temp = input('Enter your pin: ')
        for i in ATM.__list:
            if i.__pin == temp :
                print( 'Balance: '+str(i.__balance))
            flag = True
        else:
            if flag == False:
                print('Invalid pin')

    @classmethod
    def see_all(cls):
        key = input('Enter passkey:')
        if ATM.__key == key:
            for i in ATM.__list:
                print('pin:', i.__pin, 'balance:', i.__balance)





def menu():
    # print('Hello World')
    while True:
        ob = ATM()
        ch = input('''
        Hello! How would you like to proceed?
        1. Enter 1 to create pin
        2. Enter 2 to deposit
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to check balance
        6. Enter 6 for get pin
        7. Enter 7 for set pin
        8. Enter 8 to exit:
        ''')

        if ch == '1':
            ob.create_pin()
            print('pin created successfully')

        elif ch == '2':
            ob.deposit()

        elif ch == '3':
            ob.withdraw()

        elif ch == '4':
            ob.check_balance()

        elif ch == '5':
            ATM.see_all()

        elif ch == '6':
            ATM.get_pin()

        elif ch == '7':
            ATM.set_pin()

        elif ch == '8':
            print('Bye')
            break

        else:
            pass


menu()






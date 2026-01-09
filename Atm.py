class Atm:
    def __init__(self):
        self.pin=''
        self.balance=1000000
        self.menu()

    def menu(self):
        user_input=input("""
        welcome to RBL Bank
        1.Press 1 to create pin
        2.Press 2 to check balance
        3.Press 3 to change the pin
        4.Exit
        Enter your choice: """)

        if user_input=='1':
            self.create_pin()
        elif user_input=='2':
            #change the pin
            self.check_balance()
        elif user_input=='3':
            #check balance
            pass
        else:
            #exit
            pass
    def create_pin(self):
        user_pin=input('Please enter your pin')
        self.pin=user_pin
        print('Pin created successfully')
        self.menu()
    def check_balance(self):
        print(f'Your balance is {self.balance}')
        self.menu()


f=Atm()
print(f.pin)
        
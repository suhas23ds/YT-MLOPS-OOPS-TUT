class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=''
        self.menu()

    def menu(self):
        user_input=input("welcome to chatbook\n1. Sign Up\n2. Log In\n3. write a post\n4. to messages\n5. exit\n")
    
        if user_input=='1':
            self.sign_up()
        elif user_input=='2':
            self.log_in()
        elif user_input=='3':
            pass
        elif user_input=='4':
            pass
        else:
            exit()

    def sign_up(self):
        email=input("Please enter your email: ")
        password=input("Please enter your password: ")
        self.username=email
        self.password=password
        print("Sign up successful!") 
        self.menu()

    def log_in(self):
        email=input("Enter your email: ")
        password=input("Enter your password: ")
        if email==self.username and password==self.password:
            self.loggedin=True
            print("Log in successful!")
        else:
            print("Invalid credentials.")
        self.menu()
obj=chatbook()
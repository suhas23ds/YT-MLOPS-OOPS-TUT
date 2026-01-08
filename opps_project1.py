class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=''
        self.menu()

    def menu(self):
        user_input=input("welcome to chatbook\n1. Sign Up\n2. Log In\n3. write a post\n4. to messages\n5. exit\n")
    
        if user_input=='1':
            pass
        elif user_input=='2':
            pass
        elif user_input=='3':
            pass
        elif user_input=='4':
            pass
        else:
            exit()

obj=chatbook()
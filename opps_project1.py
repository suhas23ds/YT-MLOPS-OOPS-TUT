class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False   # FIXED
        self.menu()

    def menu(self):
        user_input = input(
            "Welcome to Chatbook\n"
            "1. Sign Up\n"
            "2. Log In\n"
            "3. Write a post\n"
            "4. Messages\n"
            "5. Exit\n"
        )

        if user_input == '1':
            self.sign_up()
        elif user_input == '2':
            self.log_in()
        elif user_input == '3':
            self.write_post()
        elif user_input == '4':
            self.messages()
        else:
            self.exit()   # FIXED

    def sign_up(self):
        self.username = input("Please enter your email: ")
        self.password = input("Please enter your password: ")
        print("Sign up successful!")
        self.menu()

    def log_in(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if email == self.username and password == self.password:
            self.loggedin = True
            print("Log in successful!")
        else:
            print("Invalid credentials.")

        self.menu()

    def write_post(self):
        if self.loggedin:
            post = input("Write your post: ")
            print("Post submitted!")
        else:
            print("Please log in to write a post.")

        self.menu()

    def messages(self):
        if self.loggedin:
            print("You have no new messages.")
        else:
            print("Please log in to view messages.")

        self.menu()

    def exit(self):
        print("Exiting the application. Goodbye!")
        quit()
if __name__ == "__main__":
    chatbook()

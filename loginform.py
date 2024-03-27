class LoginPage:
    def __init__(self):
        self.users = {}

    def register(self, user_name, id, pw, email):
        if user_name in self.users:
            print("Username already exists. Please choose a different username.")
            return False
        self.users[user_name] = {'id': id, 'pw': pw, 'email': email}
        print("Registration successful.")
        return True

    def login(self, user_name, pw):
        if user_name in self.users:
            if self.users[user_name]['pw'] == pw:
                print("Login successful.")
                return True
            else:
                print("Wrong password.")
                return False
        else:
            print("Username not found. Please register.")
            return False

    def details(self, user_name):
        if user_name in self.users:
            user_info = self.users[user_name]
            print("User Name:", user_name)
            print("ID:", user_info['id'])
            print("Email:", user_info['email'])
        else:
            print("User not found.")

    def logout(self):
        print("Logged out successfully.")

    def display_or_logout(self):
        choice = input("Enter 'display' to see details or 'logout' to logout: ").lower()
        if choice == "display":
            user_name = input("Enter your username: ")
            self.details(user_name)
        elif choice == "logout":
            self.logout()
        else:
            print("Invalid choice.")

# Example usage:
login_page = LoginPage()

# Attempt to login with a non-existing user
user_name = input("Enter your username: ")
pw = input("Enter your password: ")
if login_page.login(user_name, pw):
    login_page.display_or_logout()

# Register a new user
if not login_page.login(user_name, pw):
    id = input("Enter ID: ")
    pw = input("Enter password: ")
    email = input("Enter email: ")
    if login_page.register(user_name, id, pw, email):
        login_page.login(user_name, pw)
        login_page.display_or_logout()

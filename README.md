# Simple Login Page

This is a simple login page implementation in Python. It allows users to register, login, view their details, and logout.

## Features

- **Registration:** Users can register with a unique username, ID, password, and email.
- **Login:** Registered users can login with their username and password.
- **Details Display:** After login, users can choose to display their details, including username, ID, and email.
- **Logout:** Users can logout from their session.

## How to Use

1. **Run the Program:** Run the Python script `login_page.py`.
2. **Registration:** If you are a new user, choose the option to register and provide your details.
3. **Login:** After registration or if you are an existing user, login with your username and password.
4. **Display Details:** After successful login, you can choose to display your details.
5. **Logout:** You can logout from your session anytime.

## Sample Usage

```python
login_page = LoginPage()

# Register a new user
login_page.register("user1", "123", "password123", "user1@example.com")

# Login with registered user
login_page.login("user1", "password123")

# Get details of the user
login_page.details("user1")

# Logout
login_page.logout()

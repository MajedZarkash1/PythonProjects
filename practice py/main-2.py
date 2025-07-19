import os

def main():
    print("Sign in [1]")
    print("Sign up [2]")

    sign_input = input("Enter a number: ")

    filename = "users.txt"

    if sign_input == '1':
        if os.path.exists(filename):
            with open(filename, "r") as file:
                content = file.read()

            username = input("Enter your username: ")
            password = input("Enter your password: ")

            # Check if username and password match
            if f"{username}:{password}" in content:
                print("✅ Sign in successful!")
            else:
                print("❌ Invalid username or password.")
        else:
            print("File not found. No users have signed up yet.")

    elif sign_input == '2':
        username = input("Create a username: ")
        password = input("Create a password: ")

        with open(filename, "a") as file:
            file.write(f"{username}:{password}\n")

        print("✅ Sign up successful!")

    else:
        print("❌ Invalid option. Please enter 1 or 2.")

main()

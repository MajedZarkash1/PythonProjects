import os
filename = "users-main4.txt"




def function():
    global filename


    print("Welcome | Sign up [1] or sign in [2]")
    sign = input()

    if sign == '1':
        print("Create a username:")
        username = input()
        
        print("done thank you " + username)
        #storing the value of the username var
        if os.path.exists(filename):
            with open(filename, "a") as file:
                file.write(f"\n username: {username}")
        else:
            print("file not found")

    elif sign == '2':
        print("that what is in the file:")

        if os.path.exists(filename):
            with open(filename, "r") as file:
                content = file.read()
                print(content)
        else:
            print("file not found")

    else:
        print("Please Enter one of the two")
        function()

function()

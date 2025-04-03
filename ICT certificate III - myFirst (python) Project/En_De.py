#the registration form

print ("Welcome in our App")


while True:

    answer = input("Do you have a account with us? (Yes/No): ").strip().lower()
    
    if answer == "yes":
        display = input("do you want to display your account? (yes/no): ")
        break
    elif answer == "no":
        create_account = input("do you want to create a account? (yes/no): ")
        if create_account == "yes":
            username = input("enter your username: ")
            password = input("enter your password: ")
            with open("info.text", "a") as file:
                file.write(("username: ") + username + " | " +("password: ") +  password + "\n")
        else:
            print ("try again")

    else:
        print ("Sorry you should answer by Yes Or No try again")




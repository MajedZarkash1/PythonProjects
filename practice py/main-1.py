age = 20
message = f"your age is {age}"

def function():
    global age
    global message
    print("enter your name down below")

    input1 = input()

    if input1 == 'Majed':
        age = 19
    elif input1 == 'Yehya':
        age = 16
    elif input1 == 'Youssef':
        age = 14
    elif input1 == 'Rim':
        age = 40
    else:
        age = 10
    
    print(f"your age is {age}")
function()





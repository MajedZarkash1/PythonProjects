var = "majed"
print(var)

number = 5
number1 = 5
print(number * number1)

var = 1.5
print(var + number)

print("Enter your name: ")
name = input()

print("your name is " + name)

var = True
print(not True)

var_true = False
print(not False)


def function():
    global var_true

    var_true = not True
    print(var_true)
    print("Hello")

function()

var = function()

def getting_inputs():
    right = "-"
    input1 = input()
    if input1 == '1':
        print("great"+right)
    else:
        print("not right"+right+right)


getting_inputs()

def whileS():
    arrow = "->"
    input2 = input()
whileS()




get = input()
while get != '1':
    print("welcome it is wrong")
    if get == '2':
        break
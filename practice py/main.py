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
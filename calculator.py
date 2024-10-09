def calculator(x,y):
    operator = input("what is the operation?")

    if operator == "+":
        print(x + y)
    elif operator == "-":
        print(x - y)
    elif operator == "x":
        print(x * y)
    elif operator == "/":
        print(x / y)
    return

calculator(6,3)
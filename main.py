def calculator():
    print("This is a calculator to perform addition, subtraction, multiplication and division of two numbers")
    num_1 = int(input("enter the first number: "))
    operand = input("enter the operation name or symbol, e.g 'addition or +': ")
    num_2 = int(input("enter the second number: "))

    if operand == "addition" or operand == "+":
        print(f"the sum of the two numbers is {num_1 + num_2}")
    elif operand == "subtraction" or operand == "-":
        print(f"the difference of the two numbers is {num_1 - num_2}")
    elif operand == "multiplication" or operand == "*":
        print(f"the product of the two numbers is {num_1 * num_2}")
    elif operand == "division" or operand == "/":
        print(f"the quotient of the two numbers is {num_1 / num_2}")
    else:
        print("invalid operand")


calculator()

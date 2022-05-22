def calculator():
    print("This is a calculator to perform addition, subtraction, multiplication and division of two numbers")
    num_1 = int(input("enter the first number: "))
    operator = input("enter the operator name or symbol, e.g 'addition or +': ")
    num_2 = int(input("enter the second number: "))

    if operator == "addition" or operator == "+":
        print(f"the sum of the two numbers is {num_1 + num_2}")
    elif operator == "subtraction" or operator == "-":
        print(f"the difference of the two numbers is {num_1 - num_2}")
    elif operator == "multiplication" or operator == "*":
        print(f"the product of the two numbers is {num_1 * num_2}")
    elif operator == "division" or operator == "/":
        print(f"the quotient of the two numbers is {num_1 / num_2}")
    else:
        print("invalid operator")


calculator()

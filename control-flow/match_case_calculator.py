num1=int('enter your first number:')
num2=int("enter your second number")
operation=input('user chooses btwn(+,-,/,*):')
match operation:
    case '+':
        result = num1 + num2
        print(f"The result of {num1} + {num2} = {result}")
    case '-':
        result = num1 - num2
        print(f"The result of {num1} - {num2} = {result}")
    case '*':
        result = num1 * num2
        print(f"The result of {num1} * {num2} = {result}")
    case '/':
        if num2 == 0:
            print("❌ Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result of {num1} / {num2} = {result}")
    case _:
        print("⚠️ Invalid operation. Please choose from +, -, *, or /.")
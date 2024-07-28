num1 = int(input("Enter num1 please"))
num2 = int(input("Enter num2 please"))

operation = input("Enter the operation").strip()

if operation == '+':
    print(f"{num1} + {num2} = {num1 + num2}")

elif operation == '-':
    print(f"{num1} - {num2} = {num1 - num2}")

elif operation == '*':
    print(f"{num1} * {num2} = {num1 * num2}")


elif operation == '/':
    print(f"{num1} / {num2} = {num1 / num2}")


elif operation == '%':
    print(f"{num1} % {num2} = {num1 % num2}") 

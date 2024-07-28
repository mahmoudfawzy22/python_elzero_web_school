def calculate(num1, num2, operation):
	if operation == '+':
		return num1 + num2
	elif operation == '-':
		return num1 - num2
	elif operation == '/':
		return num1 / num2
	else:
		print("operation not found")

num1, num2, operation = input("Enter 2 numbers and one operation").split()
num1 = int(num1)
num2 = int(num2)
print(calculate(num1, num2, operation))

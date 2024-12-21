num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
operator = input("Enter operator (+, -, *, /): ")
if operator == "+":
    print(f"Your Answer is: {num1 + num2}\n")
elif operator == "-":
    print(f"Your Answer is: {num1 - num2}\n")
elif operator == "*":
    print(f"Your Answer is: {num1 * num2}\n")
elif operator == "/":
    print(f"Your Answer is: {num1 / num2}\n")
else:
    print("Invalid operator\n")

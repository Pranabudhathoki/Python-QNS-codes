a = int(input("Enter a num= "))
b = int(input("Enter a num= "))
op = input("Choose operator:\n1. '+'\n2. '-'\n3. '/'\n4. '*'\nChoice= ")

if op == '1':
    result = a + b
    print(f"Result: {result}")
elif op == '2':
    result = a - b
    print(f"Result: {result}")
elif op == '3':
    if b != 0: 
        result = a / b
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
elif op == '4':
    result = a * b
    print("Result:", result)
else:
    print("Invalid choice. Please choose a valid operator.")

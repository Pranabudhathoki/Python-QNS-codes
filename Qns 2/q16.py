n = int(input("Enter number of students: "))
k = int(input("Enter number of apples: "))
each = k // n
remaining = k % n
print(f"Each student gets {each} apples.")
print(f"Apples remaining in the basket: {remaining}")

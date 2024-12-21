a = int(input("Enter number of students in class 1: "))
b = int(input("Enter number of students in class 2: "))
c = int(input("Enter number of students in class 3: "))
desks = (a + 1) // 2 + (b + 1) // 2 + (c + 1) // 2
print(f"Minimum desks needed: {desks}")
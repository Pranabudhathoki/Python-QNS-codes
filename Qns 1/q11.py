age = int(input("Enter age: "))
if age < 13:
    print("Category: Child")
elif 13 <= age <= 19:
    print("Category: Teenager")
else:
    print("Category: Adult")

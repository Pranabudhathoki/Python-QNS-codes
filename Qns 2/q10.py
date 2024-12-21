grade = int(input("Enter your marks: "))
if grade < 25:
    print("Your grade is: D")
elif 25 <= grade <= 45:
    print("Your grade is: C")
elif 45 < grade <= 50:
    print("Your grade is: B")
elif 50 < grade <= 60:
    print("Your grade is: B+")
elif 60 < grade <= 80:
    print("Your grade is: A")
elif grade > 80:
    print("Your grade is: A+")
else:
    print("Invalid input.")

menu = input("Enter menu option (Pizza, Burger, Pasta): ").capitalize()
if menu == "Pizza":
    print("Price: $10")
elif menu == "Burger":
    print("Price: $7")
elif menu == "Pasta":
    print("Price: $8")
else:
    print("Invalid menu option")

#. Create a Python program that starts by greeting the user with a message
#"Welcome to Treasure Land". Then, prompt the user to choose a direction,
#either "left" or "right". If the user chooses "right", print "Game Over". If the user
#chooses "left", ask whether they want to "swim" or "wait". If they choose
#"swim", print "Game Over". If they choose to "wait", ask them to select a color:
#"red", "blue", or "yellow". If the user picks "blue" or "red", print "Game Over". If
#they select "yellow", print "You Win"

print("Welcome to Treasure Land")
print("Chose you direction")
user=int(input("Choose a direction:\n 1.Left\n 2.Right\n "))
if user==2:
    print("Game over")
elif user==1:
    a=int(input("You want to:\n 1.Swim\n 2.Wait\n "))
    if a==1:
        print("Game over")
    elif a==2:
        b=int(input("Select a color:\n 1.Red\n 2.Bluec\n 3.Yellow\n "))
        if b==1:
            print("Game over")
        elif b==2:
            print("Game over")
        elif b==3:
            print ("You Win")
        else:
            print("Envalid option")
    else :
         print("Envalid option")
else :
     print("Envalid option")


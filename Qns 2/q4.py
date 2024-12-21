#For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative
#and print ‘zero’ if it is 0

a=int(input("Enter a number: "))
if a>0:
    print(f"{a} is a Positive number")
elif a<0:
    print(f"{a} is a Negative number")
else :
    print("The number is zero")
    
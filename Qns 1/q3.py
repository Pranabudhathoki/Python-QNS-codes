a={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
user_input=int(input("Enter a number: "))
if user_input in a:
    result=a[user_input]
    print(result)

else :
    print("Out of range")

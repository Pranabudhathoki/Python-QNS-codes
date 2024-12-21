#WAP which accepts marks of four subjects and display total marks,percentage and grade.
#Hint: more than 70 –> distinction, more than 60 –> first, more than 40 –>pass,less than 40 –> fail

print("Enter marks of four subjects: ")
a=int(input("Subject 1: "))
b=int(input("Subject 2: "))
c=int(input("Subject 3: "))
d=int(input("Subject 4: "))
t=a+b+c+d
p=(t/400)*100
print(f"Total marks = {t} out of 400")
print(f"Total percentage = {p}")
if p>=70:
    print("Distinction")
elif p>=60 & p<70:
    print("First devision")
elif p>=40 & p<60:
    print("Pass")
else :
    print("Fail")
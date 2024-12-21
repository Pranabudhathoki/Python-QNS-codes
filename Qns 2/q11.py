salary = float(input("Enter your salary: "))
service = int(input("Enter your years of service: "))
if service > 10:
    bonus = salary * 0.10
elif 6 <= service <= 10:
    bonus = salary * 0.08
else:
    bonus = salary * 0.05
print(f"Your bonus is: {bonus:.2f}")

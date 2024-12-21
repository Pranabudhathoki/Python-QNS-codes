#Accept the age of 4 people and display the youngest one
#Accept the age of 4 people and display the oldest one

ages = [int(input(f"Enter age of person {i+1}: ")) for i in range(4)]
print(f"Youngest: {min(ages)}")
print(f"Oldest: {max(ages)}")

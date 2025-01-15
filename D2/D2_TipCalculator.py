print("Welcome to the tip calculator!")
total = float(input("What was the total bill?: $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15: "))/100
people = int(input("How many people to split the bill?: "))
bill = (total + total*tip)/5
print(f"Each person should pay: {bill:.2f}")
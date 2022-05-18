#if bill is 150, split by 5 people with 12% tip
#each person should pay (150/5)*1.12
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
people = float(input("How many people are splitting the bill? "))
tip = float(input("What percentage tip would you like to leave? "))

# print(type(bill))
# print(people)
# print(tip)

total = str(round((bill / people) * (1 +(tip/100)),2))



print("Each person should pay " + total)

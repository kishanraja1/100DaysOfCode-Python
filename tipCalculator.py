#if bill is 150, split by 5 people with 12% tip
#each person should pay (150/5)*1.12

bill = float(input("What was the total bill? "))
people = float(input("How many people are splitting the bill? "))
tip = float(input("How much tip would you like to leave? "))

# print(type(bill))
# print(people)
# print(tip)

total = str((bill / people) * (1 +(tip/100)))



print("Each person should pay " + total)

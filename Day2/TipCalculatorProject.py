print("Welcome to the Tip Calculator.")
bill = float(input("What was the total bill?\nR"))
tip = int(input("A tip percentage of 10, 12 or 15?\n"))
people = int(input("How many people to split the bill?\n"))

tip_given = tip / 100 * bill
individual_bill = bill / people + (tip_given / people)
print(f"Each person should pay R{round(individual_bill, 2)}")
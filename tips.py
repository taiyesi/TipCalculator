print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill: R"))
percentage = int(input("What percent would you like to tip? 10,12 or 15?: "))
num_of_people = int(input("How many people will split this bill?: "))
tip = total_bill / 100 * percentage 
bill_and_tip = total_bill + tip
per_person = bill_and_tip / num_of_people
round(per_person, 2)
print(f"Each person must pay R{per_person}")   



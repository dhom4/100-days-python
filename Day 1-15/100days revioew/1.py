"""Tips calculator"""
print("Welcome to the tip calculator!\n")


bill = float(input("What was the total bill? $"))
tip = int(input("How much precent? 20 or 15 or 10: "))
people = int(input("how many pepople: "))

tip_precent = tip / 100
tip_amount = bill * tip_precent
total_bill = tip_amount + bill
bill_per_person = total_bill / people
final_amount = round(bill_per_person,2)

print(f"Each person should pay: ${final_amount}")
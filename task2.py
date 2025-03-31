print("Welcome to tip calculator!")
bill=float(input("what is the bill amount?\n"))
tip=int(input("what is the percentage of the tip?\n"))
people=int(input("how many people want to split the bill amount\n"))
tip_as_percentage=tip/100
total_tip_amount=bill*tip_as_percentage
bill_per_people=bill+total_tip_amount
final_amount=bill_per_people/people
print(final_amount)
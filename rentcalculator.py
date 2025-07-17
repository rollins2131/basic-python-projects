# Inputs we need from the user 
# Total rent
# Total food ordered for snacking
# electricity units spend
# charge per unit
# No of persons

## Output
# Total amount you've to pay is ..


rent= int(input("Enter your flat rent: "))
food =int(input("Enter the amount for food ordered: "))
electricity = int(input("enter the electricity units: "))
charge_per_unit = int(input("Enter the charge per unit: "))
persons = int(input("enter the number of persons leaving the room for flat: "))
total_amount = rent+food+(electricity*charge_per_unit)/persons

print("You have to pay ",total_amount)
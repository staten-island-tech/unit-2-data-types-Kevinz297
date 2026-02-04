def discount(age, is_number, is_resident):
    if age >= 12 or age <= 65:
        print("Not eligible for discount")
    elif age <=12 or age>=65:
        print("Eligible for 20% discount")
    elif is_number or is_resident == True:
        print("Eligible for 30% discount")
    else:
        print("Not eligible for discount")
        return

age = 30
is_number = True
is_resident = False

discount(age, is_number, is_resident)

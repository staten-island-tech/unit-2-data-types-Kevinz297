def discount(age, is_number, is_resident):
    if age >= 12 and age <= 65:
        print("Not eligible for discount")
    elif age <=12 or age>=65:
        print("Eligible for discount")
        return

    elif is_number or is_resident == True:
        print("Eligible for full discount")
    elif is_number == True:
        print("Eligible for discount")
    elif is_resident == True:
        print("Eligible for discount")
    else:
        print("Not eligible for discount")
        return

age = 30
is_number = True
is_resident = False

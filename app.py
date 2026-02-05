def discount(age, is_number, is_resident):
    age = int(input("How old are you?"))
    if age >= 12 and age <= 65:
        print("Not eligible for discount")
    elif age <= 12 or age >= 65:
        print("Eligible for $20 discount")
        return
    is_number = input("Are you a member of the club? (yes/no) ")
    is_resident = input("Are you a resident? (yes/no) ")
    if is_number == "yes" or is_resident == "yes":
        print("Eligible for $30 discount")
    else:
        print("Not eligible for discount")
        return

age = 30
is_number = "yes"
is_resident = "no"

discount(age, is_number, is_resident)

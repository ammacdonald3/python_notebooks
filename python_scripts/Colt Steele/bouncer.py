# ask for age
age = input("How old are you? ")

# check to confirm that user input an age value
if age:

    # convert age to an int format
    age = int(age)

    # 18-21 wristband required
    if age >= 18 and age < 21:
        print("You can enter, but you need a wristband")

    # 21+ allowed to drink, normal entry
    elif age >= 21:
        print("You can enter and drink")

    # otherwise, too young
    else:
        print("You are too young and cannot enter")

# otherwise, return a command that user must enter a valid age
else:
    print("Please enter a valid age")

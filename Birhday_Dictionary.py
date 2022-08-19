# Create a dictionary (in your file) of names and birthdays.
# When you run your program, it should ask the user to enter a name
# and return the birthday of that person back to them.

bd_dict = {'vishal':'2001-06-01', 'ram':'1999-08-18', 'shyam':'2021-01-01'}
while True:
    name = input("Enter the name of a person to search or Type 'None' to cancel:  ")
    if name.lower() == "none":
        break
    if name.lower() in bd_dict:
        print("Birthday is:", bd_dict[name.lower()])
    else:
        print("Not in records")
        order = input("Would you like to add it a new record (Y OR N)?  ")
        if order.lower() == 'y':
            birthday = input("Enter the birthday of the person (YEAR-MONTH-DATE eg: 1990-02-12): ")
            bd_dict[name.lower()] = birthday
            print(bd_dict)
        else:
            print("Thank you for searching")
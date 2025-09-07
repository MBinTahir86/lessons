age_input = input("Enter your age: ")

try:
   
    age = int(age_input)
    if age < 0 or age > 130:
        print("Value Error: Age entered is not realistic.")
    else:
        print("Age accepted.")
        if age % 2 == 0:
            print("Your age is even.")
        else:
            print("Your age is odd.")
except ValueError:
    print("Value Error: Please enter a valid integer age (no decimals, letters, or special characters).")
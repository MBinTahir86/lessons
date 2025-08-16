
char = input("Enter a character: ")
if len(char) == 1:
    if char.isalpha():
        print(f"'{char}' is an alphabet.")
    else:
        print(f"'{char}' is not an alphabet.")
else:
    print("Please enter only a single character.")
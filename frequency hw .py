
test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

print("The test dictionary is:", test_dict)

try:
    k = int(input("Enter the value to check its frequency: "))

    frequency = 0
    for key in test_dict:
        if test_dict[key] == k:
            frequency += 1

    print(f"The frequency of value {k} is: {frequency}")

except ValueError:
    print("Please enter a valid integer.")

 

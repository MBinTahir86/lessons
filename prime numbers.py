def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))


if lower > upper:
    print("Invalid range: Lower range should be less than or equal to upper range.")
else:
    print(f"\nPrime numbers between {lower} and {upper} are:\n")
    for num in range(lower, upper + 1):
        if is_prime(num):
            print(num, end=' ')

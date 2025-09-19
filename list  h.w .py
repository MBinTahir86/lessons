

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))


numbers = list(range(start, end + 1))


even_numbers = []
odd_numbers = []


for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)


print("All numbers:", numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

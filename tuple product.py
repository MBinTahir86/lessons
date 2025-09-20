
numbers = (2, 3, 4, 5) 


def multiply_tuple_elements(tup):
    product = 1
    for num in tup:
        product *= num
    return product


result = multiply_tuple_elements(numbers)
print("Product of all elements in the tuple:", result)

def first_last(numbers):
    print("Given list:", numbers)
    first_element = numbers[0]
    last_element = numbers[-1]
    if first_element == last_element:
        return True
    else:
        return False
numbers_x = [10,20,30,40,10]
print("result is",first_last(numbers_x))

numbers_y = [75,65,35,75,30]
print("result is",first_last(numbers_y))



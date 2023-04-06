def multiply(num1, num2):
    result = num1 * num2
    if num1 * num2 <= 1000:
        return result
    else:
        print(num1 + num2)


x = multiply(40,30)
print(x)
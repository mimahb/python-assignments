user_input = input(str("enter word "))
print(user_input)
for i in range(0, len(user_input)):
    if(i%2 == 0):
        print(user_input[i])

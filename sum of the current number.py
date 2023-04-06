current_number = 0
sum = 0
previous_number = 0
for i in range(10):
    sum = current_number + previous_number
    current_number = i
    previous_number = i
    print("current number ",current_number, "previous number ", previous_number,"sum: ",sum)
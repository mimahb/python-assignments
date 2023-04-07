previous_number = 0

for i in range(10):
    sum = previous_number + i
    print("current number ", i, "previous number ", previous_number,"sum: ",sum)
    previous_number = i

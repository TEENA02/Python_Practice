# sol 1
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
y=0
for x in numbers:
    if x < 0:
        y+=1
print("The number of negative numbers in the list is:", y)
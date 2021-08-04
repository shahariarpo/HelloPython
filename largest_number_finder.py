numbers = [1, 5, 6, 7, 10]
largest_num = numbers[0]
for number in numbers:
    if number > largest_num:
        largest_num = number
print(largest_num)
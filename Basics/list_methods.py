num = [2, 10, 3, 5, 2, 1, 10]
unique_num = []
for number in num:
    if number not in unique_num:
        unique_num.append(number)
print(unique_num)
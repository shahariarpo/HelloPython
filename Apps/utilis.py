def find_max_number (numbers):
    largest_num = numbers[0]
    for number in numbers:
        if number > largest_num:
            largest_num = number
    return largest_num
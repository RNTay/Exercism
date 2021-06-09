#!/usr/bin/env python3

def is_valid(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False

    try:
        first_9 = [int(digit) for digit in isbn[:9]]
    except ValueError:
        return False

    check_character = isbn[-1]
    if check_character not in list('0123456789X'):
        return False

    numbers_10_to_2 = [num for num in range(2, 11)][::-1]

    check_sum = [a*b for (a, b) in zip(first_9, numbers_10_to_2)]
    check_sum = sum(check_sum)

    try:
        check_sum += int(check_character)
    except ValueError:
        check_sum += 10

    if check_sum % 11 == 0:
        return True
    else:
        return False

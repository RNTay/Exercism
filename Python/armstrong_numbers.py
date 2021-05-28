#!/usr/bin/env python3

def is_armstrong_number(number):
    original_number = number
    number_of_digits = len(str(number))
    sum_of_digit_powers = 0
    while number != 0:
        sum_of_digit_powers += (number % 10) ** number_of_digits
        number = number // 10
    return sum_of_digit_powers == original_number

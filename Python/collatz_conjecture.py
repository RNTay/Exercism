#!/usr/bin/env python3

def steps(number: int) -> int:
    if number < 1:
        raise ValueError('Number must be at least 1')
    number_of_steps = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            number_of_steps += 1
        else:
            number = (3*number + 1) // 2
            number_of_steps += 2
    return number_of_steps

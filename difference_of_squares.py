#!/usr/bin/env python3

def square_of_sum(number):
    sq_of_sum = 0
    for n in range(1, number+1):
        sq_of_sum += n
    sq_of_sum = sq_of_sum ** 2
    return sq_of_sum


def sum_of_squares(number):
    sum_of_sq = 0
    for n in range(1, number+1):
        sum_of_sq += n**2
    return sum_of_sq


def difference_of_squares(number):
    return abs(sum_of_squares(number) - square_of_sum(number))

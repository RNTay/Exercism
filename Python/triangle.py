#!/usr/bin/env python3


def is_triangle(sides):
    a, b, c = sides[0], sides[1], sides[2]
    return ((a > 0) and (b > 0) and (c > 0)) and ((a + b > c) and (a + c > b) and (b + c > a))


def equilateral(sides):
    a, b, c = sides[0], sides[1], sides[2]
    return is_triangle(sides) and (a == b == c)


def isosceles(sides):
    a, b, c = sides[0], sides[1], sides[2]
    return is_triangle(sides) and ((a == b) or (a == c) or (b == c))


def scalene(sides):
    a, b, c = sides[0], sides[1], sides[2]
    return is_triangle(sides) and (a != b != c)

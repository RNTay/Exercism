#!/usr/bin/env python3

def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strand lengths must be equal')

    hamming_distance = 0
    for letter_index in range(len(strand_a)):
        if strand_a[letter_index] != strand_b[letter_index]:
            hamming_distance += 1
    return hamming_distance

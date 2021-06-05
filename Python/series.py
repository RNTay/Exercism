#!/usr/bin/env python3

def slices(series, length):
    if length > len(series):
        raise ValueError('slice length must be less than length of series')
    if length < 1:
        raise ValueError('slice length must be at least 1')
    if length != int(length):
        raise ValueError('slice length must be an integer')

    slices_of_series = []
    for i in range(0, len(series)-length+1):
        slices_of_series.append(series[i:i+length])
    return slices_of_series

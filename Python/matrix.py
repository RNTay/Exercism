#!/usr/bin/env python3

class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(a) for a in b.split()] for b in matrix_string.splitlines()]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [m[index - 1] for m in self.matrix]

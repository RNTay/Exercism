#!/usr/bin/env python3

class Matrix:
    def __init__(self, matrix_string):
        self.rows = [[int(a) for a in b.split()] for b in matrix_string.split('\n')]
        self.columns = [list(_) for _ in list(zip(*self.rows))]

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return self.columns[index - 1]

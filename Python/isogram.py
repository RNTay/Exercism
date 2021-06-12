#!/usr/bin/env python3

def is_isogram(string: str):
    only_letters = string.lower().replace(' ', '').replace('-', '')
    letters_only_once = list(set(only_letters))
    if sorted(only_letters) == sorted(letters_only_once):
        return True
    else:
        return False

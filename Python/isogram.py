#!/usr/bin/env python3

def is_isogram(string: str):
    only_letters = string.lower().replace(' ', '').replace('-', '')
    letters_only_once = set(only_letters)
    return len(only_letters) == len(letters_only_once)

#!/usr/bin/env python3

def find_anagrams(word, candidates):
    anagrams = []
    for c in candidates:
        if sorted(list(c.lower())) == sorted(list(word.lower())):
            if c.lower() != word.lower():
                anagrams.append(c)
    return anagrams

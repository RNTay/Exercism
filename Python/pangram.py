#!/usr/bin/env python3

def is_pangram(sentence):
	letters = 'abcdefghijklmnopqrstuvwxyz'
	sentence = sentence.lower()
	for letter in letters:
		if letter not in sentence:
			return False
	return True

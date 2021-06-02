#!/usr/bin/env python3

def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    top_three = []
    if len(scores) >= 3:
        for _ in range(3):
            top_three.append(max(scores))
            scores.remove(max(scores))
    else:
        while scores != []:
            top_three.append(max(scores))
            scores.remove(max(scores))
    return top_three

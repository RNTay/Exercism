#!/usr/bin/env python3

def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    if len(scores) >= 3:
        top_three = sorted(scores, reverse=True)[:3].copy()
    else:
        top_three = sorted(scores, reverse=True).copy()
    return top_three

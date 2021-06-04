#!/usr/bin/env python3

import random


class Robot:
    robots = []

    def __init__(self):
        while True:
            self.name = ''
            for _ in range(2):
                self.name += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[random.randint(0, 25)]
            for _ in range(3):
                self.name += str(random.randint(0, 9))
            if self.name not in Robot.robots:
                Robot.robots.append(self.name)
                break
            else:
                continue

    def reset(self):
        previous_name = self.name
        while True:
            self.name = ''
            for _ in range(2):
                self.name += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[random.randint(0, 25)]
            for _ in range(3):
                self.name += str(random.randint(0, 9))
            if self.name not in Robot.robots:
                Robot.robots.append(self.name)
                break
            else:
                continue
        Robot.robots.remove(previous_name)

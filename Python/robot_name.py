#!/usr/bin/env python3

import random
import string


class Robot:
    existing_robots = set()

    @staticmethod
    def generate_robot_name():
        while True:
            new_name = ''.join(random.choices(string.ascii_uppercase, k=2) +
                               random.choices(string.digits, k=3))
            if new_name not in Robot.existing_robots:
                Robot.existing_robots.add(new_name)
                break
        return new_name

    def __init__(self):
        self.name = Robot.generate_robot_name()

    def reset(self):
        previous_name = self.name
        self.name = Robot.generate_robot_name()
        Robot.existing_robots.remove(previous_name)

from itertools import permutations
import unittest
from pathlib import Path


class Triangle():
    def __init__(self, a, b, c):
        self.sides = (a, b, c)

    def is_valid(self):
        return all([x < y + z for x, y, z in permutations(self.sides)])

def count_possible_triangles():
    possible = 0
    with (Path(__file__).parent / 'three_input.txt').open() as f:
        for triangle in f:
            t = Triangle(*map(int, triangle.split()))
            if t.is_valid():
                possible += 1
    return possible


class TestTriangle(unittest.TestCase):
    def test_valid(self):
        triangle = Triangle(5, 5, 5)
        self.assertTrue(triangle.is_valid())

    def test_not_valid(self):
        triangle = Triangle(5, 10, 25)
        self.assertFalse(triangle.is_valid())

    def test_task_one(self):
        possible = 0
        with (Path(__file__).parent / 'three_input.txt').open() as f:
            for triangle in f:
                if Triangle(*triangle.split()).is_valid():
                    possible += 1

        print(possible)


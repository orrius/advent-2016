from itertools import permutations, islice
from pathlib import Path
from itertools import chain

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


def count_possible_vertical_triangles():
    possible = 0
    with (Path(__file__).parent / 'three_input.txt').open() as f:
        lines = f.readlines()
        lines = map(str.split, lines)
        lines = list(chain.from_iterable(lines))
        lines = list(map(int, lines))
        first_row = lines[::3]
        second_row = lines[1::3]
        third_row = lines[2::3]
        triangles = chain(first_row, second_row, third_row)
        for x, y, z in zip(triangles, triangles, triangles):
            print(x, y, z)
            if Triangle(x, y, z).is_valid():
                possible += 1
    print(possible)


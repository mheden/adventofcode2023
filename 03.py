from utils import slurp, unpack, assert_eq, Rect, P2d
import re


def parse(s):
    numbers = list()
    symbols = list()
    for y, line in enumerate(unpack(s)):
        for m in re.finditer(r"(\d+)", line):
            numbers.append(
                (int(m.group(1)), Rect(P2d(m.start(), y), P2d(m.end(1) - 1, y)))
            )
        for m in re.finditer(r"([^\d\.])", line):
            symbols.append(
                (m.group(1), Rect(P2d(m.start() - 1, y - 1), P2d(m.start() + 1, y + 1)))
            )
    return numbers, symbols


def part1(s):
    sum_ = 0
    numbers, symbols = parse(s)
    for _, rect in symbols:
        for number, r in numbers:
            if rect.overlap(r):
                sum_ += number
    return sum_


def part2(s):
    sum_ = 0
    numbers, symbols = parse(s)
    for symbol, rect in symbols:
        if symbol != "*":
            continue
        adjacent = []
        for number, r in numbers:
            if rect.overlap(r):
                adjacent.append(number)
        if len(adjacent) == 2:
            sum_ += adjacent[0] * adjacent[1]
    return sum_


filedata = slurp("03.txt")
testdata = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

print("#--- Day 3.1: Gear Ratios:", end=" ")

assert_eq(part1(testdata), 4361)
print(part1(filedata))

print("#--- Day 3.2: Gear Ratios:", end=" ")

assert_eq(part2(testdata), 467835)
print(part2(filedata))

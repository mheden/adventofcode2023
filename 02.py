from utils import slurp, unpack, assert_eq
import re
import math
from collections import defaultdict


def part1(s):
    sum_ = 0
    for game in unpack(s):
        bag = defaultdict(lambda: 0)
        m = re.search(r"Game (\d+): (.+)", game)
        for round_ in m.group(2).split(";"):
            for count, color in re.findall(r"(\d+) (\w+)", round_.strip()):
                bag[color] = max(bag[color], int(count))
        if (bag["red"] <= 12) and (bag["green"]) <= 13 and (bag["blue"] <= 14):
            sum_ += int(m.group(1))
    return sum_


def part2(s):
    sum_ = 0
    for game in unpack(s):
        bag = defaultdict(lambda: 0)
        m = re.search(r"Game (\d+): (.+)", game)
        for round_ in m.group(2).split(";"):
            for count, color in re.findall(r"(\d+) (\w+)", round_.strip()):
                bag[color] = max(bag[color], int(count))
        sum_ += math.prod(bag.values())
    return sum_


filedata = slurp("02.txt")
testdata = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

print("#--- Day 2.1: Cube Conundrum:", end=" ")

assert_eq(part1(testdata), 8)
print(part1(filedata))

print("#--- Day 2.2: Cube Conundrum:", end=" ")

assert_eq(part2(testdata), 2286)
print(part2(filedata))

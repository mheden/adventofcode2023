from utils import slurp, unpack, assert_eq
import math
import re


def parse(line):
    line = line.split(":")[1]
    winning, my = line.split("|")
    winning = set(map(int, re.split(r"\s+", winning.strip())))
    my = set(map(int, re.split(r"\s+", my.strip())))
    return winning & my


def part1(s):
    sum_ = 0
    for line in unpack(s):
        winning = parse(line)
        if len(winning) > 0:
            sum_ += int(math.pow(2, len(winning) - 1))
    return sum_


def part2(s):
    cards = []
    for _ in unpack(s):
        cards.append(1)
    for i, line in enumerate(unpack(s)):
        for n in range(len(parse(line))):
            cards[i + 1 + n] += 1 * cards[i]
    return sum(cards)


filedata = slurp("04.txt")
testdata = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

print("#--- Day 4.1: Scratchcards:", end=" ")

assert_eq(part1(testdata), 13)
print(part1(filedata))

print("#--- Day 4.2: Scratchcards:", end=" ")

assert_eq(part2(testdata), 30)
print(part2(filedata))

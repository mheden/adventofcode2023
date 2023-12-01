from utils import slurp, unpack, assert_eq, digits, rev
import re


def part1(s):
    sum_ = 0
    for line in unpack(s):
        num = digits(line)
        sum_ += num[0] * 10 + num[-1]
    return sum_


numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}


def part2(s):
    first = f"{'|'.join(numbers.keys())}"
    last = rev(first)
    sum_ = 0
    for line in unpack(s):
        f = re.search(f"({first})", line).group(1)
        l = rev(re.search(f"({last})", rev(line)).group(1))
        sum_ += numbers[f] * 10 + numbers[l]
    return sum_


filedata = slurp("01.txt")
testdata1 = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
testdata2 = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

print("#--- Day 1.1:", end=" ")

assert_eq(part1(testdata1), 142)
print(part1(filedata))

print("#--- Day 1.2:", end=" ")

assert_eq(part2(testdata2), 281)
print(part2(filedata))

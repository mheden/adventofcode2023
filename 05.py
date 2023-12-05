from utils import slurp, unpack, assert_eq, numbers, BIGNUM, chunks
import re


# def partx(s):
#     groups = unpack(s, sep="\n\n")
#     seeds =  numbers(groups[0])
#     funcs = []
#     prog = []
#     for map in groups[1:]:
#         map = unpack(map)
#         func = map[0].split(' ')[0].replace('-', '_')
#         funcs.append(func)
#         prog.append(f"def {func}(n):")
#         for m in map[1:]:
#             to_, from_, range_ = numbers(m)
#             prog.append(f"    if {from_} <= n < {from_ + range_}:")
#             prog.append(f"        return n + {to_ - from_}")
#         prog.append("    else:")
#         prog.append("        return n")
#         prog.append("\n\n")

#     result = 0
#     s = '\n'.join(prog) + 'result = min(' + '('.join(reversed(funcs)) + "(n)" + (len(funcs) - 1) * ')' +  f" for n in {seeds})"
#     print(s)
#     exec(s)
#     return result


def fn(seed, map_):
    for m in map_:
        if m[0] <= seed < m[1]:
            return seed + m[2]
    else:
        return seed


def part1(s):
    def fn(seed, map_):
        for from_, to_, offset in map_:
            if from_ <= seed < to_:
                return seed + offset
        else:
            return seed

    data = unpack(s, sep="\n\n")
    maps = []

    for mapping in data[1:]:
        m = []
        for interval in unpack(mapping)[1:]:
            to_, from_, range_ = numbers(interval)
            m.append((from_, from_ + range_, to_ - from_))
        maps.append(m)

    min_ = BIGNUM
    for seed in numbers(data[0]):
        seed_ = seed
        for map_ in maps:
            seed_ = fn(seed_, map_)
        min_ = min(min_, seed_)
    return min_


def part2(s):

    def fn(seed, map_):
        for from_, to_, offset in map_:
            if from_ <= seed < to_:
                return seed + offset
        else:
            return seed

    data = unpack(s, sep="\n\n")
    maps = []

    for mapping in data[1:]:
        m = []
        for interval in unpack(mapping)[1:]:
            to_, from_, range_ = numbers(interval)
            m.append((from_, from_ + range_, to_ - from_))
        maps.append(list(sorted(m)))

    import pprint
    pprint.pprint(maps)

    for start, length in chunks(numbers(data[0]), 2):
        print(start, length)
    
        # generate new ranges after each function
    # example:
    #
    # in: 79, 14 (79, .., 92)
    # call seed-to-soil
    # out: 81, 14 (81, ..., 94)

    return 0


filedata = slurp("05.txt")
testdata = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

print("#--- Day 4.1: If You Give A Seed A Fertilizer:", end=" ")

assert_eq(part1(testdata), 35)
print(part1(filedata))

print("#--- Day 4.2: If You Give A Seed A Fertilizer:", end=" ")

assert_eq(part2(testdata), 46)
# print(part2(filedata))

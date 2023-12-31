from functools import reduce
import sys
from typing import List

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            lines.append(line)

    return lines

def part_one():
    lines = read_lines_to_list()

    times = [int(val) for val in lines[0].split(":")[1].strip().split()]
    records = [int(val) for val in lines[1].split(":")[1].strip().split()]

    races = [(time, distance) for (time, distance) in zip(times, records)]

    num_ways = []

    for time, record in races:
        wins = 0
        for i in range(time + 1):
            if (i * (time - i)) > record:
                wins += 1

        num_ways.append(wins)

    result = reduce((lambda x, y: x * y), num_ways)
    print("Part 1: {}".format(result))

def part_two():
    lines = read_lines_to_list()
    time = int("".join(lines[0].split(":")[1].strip().split()))
    record = int("".join(lines[1].split(":")[1].strip().split()))

    wins = 0
    for i in range(time + 1):
        if (i * (time - i)) > record:
            wins += 1

    print("Part 2: {}".format(wins))

part_one()
part_two()

# Day 3: Gear Ratios
# https://adventofcode.com/2023/day/3
import math, re

file = list(open('input.txt'))
chars = {(index, value): [] for index in range(140) for value in range(140) if file[index][value] not in '0123456789.'}
# print("First: %s", chars)
# 	for c in range(140):
# 		if file[r][c] not in '0123456789.':
# 			chars = (r, c)

for index, row in enumerate(file):
    for n in re.finditer(r'\d+', row):
        edge = {(index, value) for index in (index-1, index, index+1)
                       for value in range(n.start()-1, n.end()+1)}

        for o in edge & chars.keys():
        	chars[o].append(int(n.group()))

# for row, line in enumerate(file):
# 	for n in re.finditer(r'\d+', line):
# 		for row in (row - 1, row, row + 1):
# 			for col in range(n.start() - 1, n.end() + 1):
# 				edge = (row, col)

		# for o in edge & chars.keys():
		# 	chars[o].append(int(n.group()))

part1 = sum(sum(part1) for part1 in chars.values()) 
part2 = sum(math.prod(part2) for part2 in chars.values() if len(part2) == 2)

print("Part1 solution: ", part1)

print("Part2 solution: ", part2)

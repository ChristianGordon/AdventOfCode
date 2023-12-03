# Day 2: Cude Conundrum
# 12 Red, 13 Green, 14 Blue

import sys
from collections import defaultdict

# doc = open(sys.argv[1]).read().strip()
doc = open("input.txt").read().strip()

p1_score = 0
p2_score = 0

for line in doc.split('\n'):
  part_1 = True
  game_num, line = line.split(':')
  values = defaultdict(int)

  for event in line.split(';'):
    for balls in event.split(','):
      number, color = balls.split()
      number = int(number)
      values[color] = max(values[color], number)

      if number > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
        part_1 = False

  score = 1

  for i in values.values():
    score *= i

  p2_score += score

  if part_1:
    p1_score += int(game_num.split()[-1])

print("Part 1 solution: ", p1_score)
print("Part 2 solution: ", p2_score)
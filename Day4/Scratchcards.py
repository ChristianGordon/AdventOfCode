# Day4 : Scratchcards
from collections import defaultdict

file = open("input.txt").read().strip()
lines = file.split('\n')

p1_val = 0
p2_nums = defaultdict(int)
for i,line in enumerate(lines):
  p2_nums[i] += 1
  winning_nums, input_nums = line.split('|')
  id_, card = winning_nums.split(':')
  card_nums = [int(x) for x in card.split()]
  rest_nums = [int(x) for x in input_nums.split()]
  val = len(set(card_nums) & set(rest_nums))
  if val > 0:
    p1_val += 2**(val-1)
  for j in range(val):
    p2_nums[i+1+j] += p2_nums[i]
print(p1_val)
print(sum(p2_nums.values()))
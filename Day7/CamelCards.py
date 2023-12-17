import sys
from collections import Counter

file = open("input.txt").read().strip()
lines = file.split('\n')

def strength(hand, part2):
  hand = hand.replace('T',chr(ord('9')+1))
  hand = hand.replace('J',chr(ord('2')-1) if part2 else chr(ord('9')+2))
  hand = hand.replace('Q',chr(ord('9')+3))
  hand = hand.replace('K',chr(ord('9')+4))
  hand = hand.replace('A',chr(ord('9')+5))

  count = Counter(hand)
  if part2:
    target = list(count.keys())[0]
    for king in count:
      if king != '1':
        if count[king] > count[target] or target == '1':
          target = king
    assert target != '1' or list(count.keys()) == ['1']
    if '1' in count and target != '1':
      count[target] += count['1']
      del count['1']
    assert '1' not in count or list(count.keys()) == ['1'], f'{count} {hand}'

  if sorted(count.values()) == [5]:
    return (10, hand)
  elif sorted(count.values()) == [1,4]:
    return (9, hand)
  elif sorted(count.values()) == [2,3]:
    return (8, hand)
  elif sorted(count.values()) == [1,1,3]:
    return (7, hand)
  elif sorted(count.values()) == [1,2,2]:
    return (6, hand)
  elif sorted(count.values()) == [1,1,1,2]:
    return (5, hand)
  elif sorted(count.values()) == [1,1,1,1,1]:
    return (4, hand)
  else:
    assert False, f'{count} {hand} {sorted(count.values())}'

for part2 in [False, True]:
  H = []
  for line in lines:
    hand, bid = line.split()
    H.append((hand, bid))
  H = sorted(H, key=lambda hb:strength(hb[0], part2))
  ans = 0
  for i,(h,b) in enumerate(H):
    # print(i,h,b)
    ans += (i+1)*int(b)
  print(ans)

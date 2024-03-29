import sys
from typing import List
from dataclasses import dataclass

@dataclass
class Instruction:
  d: str
  n: int

def parseInput(input_: str, part2: bool) -> List[Instruction]:
  ans = []
  for line in input_.split('\n'):
    d, n, hex_ = line.split()
    if not part2:
      ans.append(Instruction(d, int(n)))
    else:
      hex_ = hex_[1:-1]
      d = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}[int(hex_[-1])]
      n = int(hex_[1:-1], 16)
      ans.append(Instruction(d, n))
  return ans

def areaShoelace(cmds: List[Instruction]) -> int:
  V = []
  # x y
  pos = (0,0)
  for cmd in cmds:
    d,n = cmd.d, cmd.n
    if d == 'R':
      pos = (pos[0]+n, pos[1])
    elif d == 'D':
      pos = (pos[0], pos[1]-n)
    elif d == 'L':
      pos = (pos[0]-n, pos[1])
    elif d=='U':
      pos = (pos[0], pos[1]+n)
    V.append(pos)
  area = 0
  for i in range(len(V)):
    area -= V[i][0]*V[(i+1)%len(V)][1]
    area += V[i][1]*V[(i+1)%len(V)][0]
  area //= 2
  return area

def areaGreen(cmds: List[Instruction]) -> int:
  area = 0
  y = 0
  for cmd in cmds:
    if cmd.d=='R':
      area += y*cmd.n
    elif cmd.d=='L':
      area -= y*cmd.n
    elif cmd.d=='U':
      y += cmd.n
    elif cmd.d=='D':
      y -= cmd.n
  return area

D = open("input.txt").read().strip()
for part2 in [False,True]:
  cmds = parseInput(D,part2)
  perimeter = 0
  for cmd in cmds:
    perimeter += cmd.n
  area1 = areaShoelace(cmds)
  area2 = areaGreen(cmds)
  assert area1 == area2, f'shoelace={area1} green={area2}'
  ans = area1 + (perimeter//2) + 1
  print(ans)
from __future__ import annotations
# l = [
#   {"t": 3, "x": 1, "y": 2},
#   {"t": 6, "x": 1, "y": 1},
# ]

N = int(input())
P = []
for i in range(N):
  x = input().split()
  P.append({"t": int(x[0]), "x": int(x[1]), "y": int(x[2])})

def possible(n, plan):
  x = 0
  y = 0
  target_x = plan[0]["x"]
  target_y = plan[0]["y"]
  life = plan[0]["t"]
  p = Person(x, y, life)
  if not p.can_reach(target_x, target_y):
    return "No" 

  for i in range(0, n - 1):
    x = plan[i]["x"]
    y = plan[i]["y"]
    target_x = plan[i + 1]["x"]
    target_y = plan[i + 1]["y"]
    life = plan[i + 1]["t"] - plan[i]["t"]
    p = Person(x, y, life)
    if not p.can_reach(target_x, target_y):
      return "No"

  return "Yes" 

class Person():
  def __init__(self, x: int, y: int, life: int) -> None:
    self.x = x
    self.y = y
    self.life = life

  # 死ぬ前に目標に辿り着けるかどうか
  def can_reach(self, target_x, target_y):
    distance = abs(target_x - self.x) + abs(target_y - self.y)
    #　命が尽きない かつ 折り返して戻ってこれる
    rest_of_life = self.life - distance
    if (rest_of_life < 0): 
      return False
    if (rest_of_life % 2 == 1):
      return False
    return True

print(possible(N, P))
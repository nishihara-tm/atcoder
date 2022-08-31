
#g = ["RDU", "LRU"]
def move(g, h, w):
  x = 0
  y = 0

  trajectory = []
  for i in range(h):
    l = []
    for j in range(w):
      l.append(False)
    trajectory.append(l)

  while True:
    if trajectory[x][y]: 
      return -1

    trajectory[x][y] = True

    if g[x][y] == "U" and x != 0:
      x = x - 1
    elif g[x][y] == "D" and x != (h - 1):
      x = x + 1
    elif g[x][y] == "L" and y != 0:
      y = y - 1
    elif g[x][y] == "R" and y != (w - 1):
      y = y + 1
    else:
      return x + 1, y + 1

  # 問題設定では(1,1)から移動している想定なので
  # return x + 1, y + 1

H, W = [int(i) for i in input().split()]
G = []
for h in range(H):
  G.append(input())
print(move(G, H, W))
from collections import deque
import queue

class Node:
  def __init__(self, index):
    self.index = index
    self.nears = []
    self.sign = -1 #未探索のNodeは-1


N, M = map(int, input().split()) # N個のNode（部屋）とM個の線
edegs = []
links = [list(map(int, input().split())) for _ in range(M)]

nodes = []
for i in range(N + 1):
  nodes.append(Node(i))

for j in range(M):
  edge_start, edge_end = links[j]
  nodes[edge_start].nears.append(edge_end)
  nodes[edge_end].nears.append(edge_start)

queue = deque()
queue.append(nodes[1])

while queue:
  node = queue.popleft()
  nears = node.nears

  for near in nears:
    if nodes[near].sign == -1:
      queue.append(nodes[near])
      nodes[near].sign = node.index

if -1 in [node.sign for node in nodes][2:]:
  print("No")
else:
  print("Yes")

for k in range(2, N + 1):
  print(nodes[k].sign)
# 求め方 
# ノード1からの最短距離の最大値を取るノードを求める
# 最大値を取るノードから各ノードへの距離を求めて最大値＋１が答え 

import collections

INF = -100000000
N = int(input())
A = [INF]
B = [INF]

for i in range(1, N):
  a, b = list(map(int, input().split()))
  A.append(a)
  B.append(b)

# グラフ
# 例。G[from] = [to1, to2, to3]
G = [[INF]] * (N+1) 
for i in range(1, N+1):
  G[i] = []

for i in range(1, N):
  G[A[i]].append(B[i])
  G[B[i]].append(A[i])


def getdist(start):
  dist = [INF] * (N+1)
  q = collections.deque()
  q.append(start)
  dist[start] = 0
  while(len(q) > 0):
    pos = q.pop()
    for to in G[pos]:
      # おとづれたことがない
      if(dist[to] == INF):
        dist[to] = dist[pos] + 1
        q.append(to)
  return dist

d1 = getdist(1)
max_from_1_idx = -1
max_from_1 = -1

for i in range(1, N+1):
  if ( max_from_1 < d1[i]):
    max_from_1 = d1[i]
    max_from_1_idx = i

d2 = getdist(max_from_1_idx)
max_from_n = -1
for i in range(1, N+1):
  if ( max_from_n < d2[i]):
    max_from_n = d2[i]

print(max_from_n + 1)
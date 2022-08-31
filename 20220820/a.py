# No.1
# S = input()
# 
# print(S[(len(S)) // 2])


# No.2
# N = int(input())
# 
# r = N // 998244353 
# x = N - r * 998244353
# 
# print(x)

# No.3
# A = [int(a) for a in input().split()]
# B = [int(b) for b in input().split()]
# C = [int(c) for c in input().split()]
# D = [int(d) for d in input().split()]
# 
# #2点のベクトルを求める
# def vec(a, b):
#     return (a[0] - b[0], a[1] - b[1])
# 
# #点 a,b,cの三角形内にpが入っていれば Trueを返す
# def tri_in(a, b, c, p): 
# 
#     ab = vec(b, a)
#     bp = vec(p, b)
# 
#     bc = vec(c, b)
#     cp = vec(p, c)
# 
#     ca = vec(a, c)
#     ap = vec(p, a)
# 
#     #外積を求める
#     c1 = ab[0] * bp[1]  - ab[1] * bp[0]
#     c2 = bc[0] * cp[1]  - bc[1] * cp[0]
#     c3 = ca[0] * ap[1]  - ca[1] * ap[0]
# 
#     #外積の向き　正負がそろっていれば内側
#     #return (c1 > 0 and c2 > 0 and c3 > 0)or(c1 < 0 and c2 < 0 and c3 < 0)
#     return (c1 >= 0 and c2 >= 0 and c3 >= 0)or(c1 <= 0 and c2 <= 0 and c3 <= 0) #追記　頂点　辺上も内側とする場合はこちらを使う
# 
# 
# if not tri_in(A,B,C,D) and not tri_in(B,C,D,A) and not tri_in(C,D,A,B) and not tri_in(D,A,B,C):
#   print("Yes")
# else:
#   print("No")

# No.4
# N=int(input())
# Tmax=10**5
# X=[0]*(Tmax+1)
# A=[0]*(Tmax+1)
# for _ in range(N):
# 	t,x,a=map(int,input().split())
# 	X[t]=x
# 	A[t]=a
#  
# dp=[[-10**18]*(Tmax+1) for _ in range(5)]
# dp[0][0]=0
#  
# for t in range(1,5):
# 	for i in range(5):
# 		dp[i][t]=dp[i][t-1]
# 		if i!=0: dp[i][t]=max(dp[i][t],dp[i-1][t-1]);
# 		if i!=4: dp[i][t]=max(dp[i][t],dp[i+1][t-1]);
# 	dp[X[t]][t]+=A[t];
# 
# print(max(dp[i][Tmax] for i in range(5)))

# No.5
# ベイズ確率

# No.6
# 
import collections
from typing import *

class UnionFind:
    """
    Class implementation of disjoint-set data structure
    """
 
    # Constructor
    def __init__(self, N: int):
        self._parent: List[int] = [-1 for i in range(N)]
        self._rank: List[int] = [0 for i in range(N)]
        self._size: List[int] = [1 for i in range(N)]
 
    # Return the root of the tree to which x is belonging
    def get_root(self, x: int) -> int:
        if self._parent[x] == -1:
            return x
        else:
            self._parent[x] = self.get_root(self._parent[x])
            return self._parent[x]
 
    # Return true if x and y belong to the same tree
    def is_same(self, x: int, y: int) -> bool:
        return self.get_root(x) == self.get_root(y)
 
    # Merge the group to which x is belonging and the group to which y is belonging
    def unite(self, x: int, y: int) -> bool:
        # Get root of x and y
        rx = self.get_root(x)
        ry = self.get_root(y)
 
        # Do nothing when x and y are already in same group
        if rx == ry:
            return False
 
        # Union by rank
        # Make sure that the rank of ry side is small
        if self._rank[rx] < self._rank[ry]:
            rx, ry = ry, rx
 
        # Make sure that ry is child of rx
        self._parent[ry] = rx
 
        # Compute rank of rx side
        if self._rank[rx] == self._rank[ry]:
            self._rank[rx] += 1
 
        # Compute size of rx side
        self._size[rx] += self._size[ry]
 
        return True
 
    # Return size of the group to which x is belonging
    def get_size(self, x: int) -> int:
        return self._size[self.get_root(x)]

N = int(input())
graph = [[] for i in range(N)]
indegree = [0] * N

for i in range(N):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  graph[u].append(v)
  graph[v].append(u)
  indegree[u] += 1
  indegree[v] += 1

#入次元が２以上だとTrue そうではない場合1=葉っぱ
in_cycle = [len(g) != 1 for i, g in enumerate(graph)]

# loop
# 葉っぱから探索、次のノードとの接合部を切る => 入次元が１以下になった場合in_cycle[node] = Falseにする
# in_cycle[node] = Trueとして残ったものがサイクル内のNode
candidate = collections.deque([i for i, g in enumerate(graph) if len(g) == 1])
while candidate:
  node = candidate.popleft()
  for next_node in graph[node]:
    # 葉っぱから探索するので次のNodeが葉っぱである場合にはスキップする
    if not in_cycle[next_node]:
      continue

    #結合部を切断する
    indegree[next_node] -= 1

    if indegree[next_node] <= 1:
      #次の葉っぱになるからサイクルには属していない
      in_cycle[next_node] = False
      candidate.append(next_node)

uf = UnionFind(N)
cycle = {i for i, b in enumerate(in_cycle) if b }
explored = [False] * N

for start in cycle:
  candidate = collections.deque([start])
  explored[start] = True

  while candidate:
    node = candidate.popleft()

    for next_node in graph[node]:
      if next_node in cycle or explored[next_node]:
        continue

      explored[next_node] = True
      candidate.append(next_node)
      uf.unite(start, next_node)

Q = int(input())
X, Y = map(list, zip(*[list(map(int, input().split())) for i in range(Q)]))

for x, y in zip(X, Y):
  x -= 1
  y -= 1

  if uf.is_same(x, y):
    print("Yes")
  else:
    print("No")
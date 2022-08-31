import numpy as np
from itertools import combinations

H, W =map(int, input().split())
A=np.array([list(map(int, input().split())) for _ in range(H)])

h, w = map(int, input().split())
B=np.array([list(map(int, input().split())) for _ in range(h)])

for hidx in combinations(range(H), h):
  for widx in combinations(range(W), w):
    if np.all(A[hidx, :][:, widx] == B):
      print("Yes")
      exit()
print("No")
N = int(input())
K = int(input())
h = [0]
h += [int(i) for i in input().split()]
print(h)


def a():
  # 足場1からiまで移動するのに必要な移動コストをdp[i]と置く
  dp = [0] * (N + 1)
  dp[1] = 0
  dp[2] = h[2] - h[1]
  for i in range(2, N + 1):
    dp[i] = min((dp[i - 1] + abs(h[i] - h[i - 1])), (dp[i - 2] + abs(h[i] - h[i - 2])))
  
  print(dp)
  return dp[-1]

def b():
  # 足場1からiまで移動するのに必要な移動コストをdp[i]と置く
  dp = [0] * (N + 1)
  dp[1] = 0
  dp[2] = h[2] - h[1]
  for i in range(2, N + 1):
    tmp = []
    for k in range(1, K + 1):
      # i - kからiに到達するまでのコストをk = 1 ~ Kまで算出する
      cost = dp[i - k] + abs(h[i] - h[i - k])
      tmp.append(cost)
    dp[i] = min(tmp)
  
  print(dp)
  return dp[-1]

print(a())
print(b())
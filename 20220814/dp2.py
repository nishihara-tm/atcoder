from pdb import set_trace


N = int(input())
a,b,c = [int(x) for x in input().split()]

# dp[i][0] = max(dp[i - 1][1] + a, dp[i -1][2] + a)
# dp[i][1] = max(dp[i - 1][0] + b, dp[i -1][2] + b)
# dp[i][2] = max(dp[i - 1][0] + c, dp[i -1][1] + c)

dp = [[0] * 3] * (N + 1)
print(dp)

# 初期条件として、0日目の幸福度は0とする
dp[0][0] = 0
dp[0][1] = 0
dp[0][2] = 0

for i in range(1, N + 1):
  dp[i][0] = max(dp[i - 1][1] + a, dp[i -1][2] + a)
  dp[i][1] = max(dp[i - 1][0] + b, dp[i -1][2] + b)
  dp[i][2] = max(dp[i - 1][0] + c, dp[i -1][1] + c)

print(max(dp))
print(max(dp[N]))
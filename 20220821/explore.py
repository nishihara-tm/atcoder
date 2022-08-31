
# i -> i + 1へのmove
def validate(n, t, a, bonus):
  for i in range(1, n):
    if t <= a[i]:
      return "No"
    else:
      t -= a[i]
      t += bonus[i + 1]

  return "Yes"

N,M,T = [int(x) for x in input().split()]
A = [0] + [int(x) for x in input().split()] #N個(0番目に到達する際に消費するエネルギーは0)
BONUS = [0] * (N + 1) #n番目の部屋の追加得点
for i in range(M):
  x, y = [int(a) for a in input().split()]
  BONUS[x] = y
# 
print(validate(N,T,A,BONUS))
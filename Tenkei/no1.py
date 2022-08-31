N, L = list(map(int, input().split()))
K = int(input())
A = [0] + list(map(int, input().split())) #A0 = 0

print("N is ", N)
print("L is ", L)
print("K is ", K)
print("A is ", A)

#答えが長さMの時にK+1個以上の分割ができるかどうか
#できるならTrue できない場合False
def solve(M):
  prev=0
  cnt=0
  for i in range(1, N+1):
    if((A[i] - prev) >= M and (L - A[i]) >= M):
      prev = A[i]
      cnt += 1
  if(cnt >= K):
    return True
  else:
    return False

left = -1
right = L+1
while (right - left > 1):
  # mid = left + (right - left) // 2
  mid = (right + left) // 2
  if(solve(mid)):
    left = mid
  else:
    right = mid

print(mid)
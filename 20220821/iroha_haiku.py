

def validate(n, p, q, r, a):
  #S0 ~ SNを計算しておく
  S = [0]
  for i in range(1, n + 1):
    S.append(sum(a[0:i]))

  #S(R) - S(L) = A(L) + A(L+1) .... +A(R - 1)
  found = False
  for x in range(n - 3):
    y = x + 1
    flag = True
    while True:
      # 適切なyを見つけることができた時
      if S[y] == (S[x] + p):
        break
      # 適切なyを見つけられなかった時
      if y >= n - 2:
        flag = False
        break
      y =  y + 1

    if flag == False:
      continue

    z = y + 1
    while True:
      # 適切なzを見つけることができた時
      if S[z] == (S[y] + q):
        break
      # 適切なzを見つけられなかった時
      if z >= n - 1:
        flag = False
        break
      z =  z + 1

    if flag == False:
      continue

    w = z + 1
    while True:
      # 適切なzを見つけることができた時
      if S[w] == (S[z] + r):
        break
      # 適切なzを見つけられなかった時
      if w >= n:
        flag = False
        break
      w =  w + 1

    if flag == True:
      found = True
      break

  if found == True:
    return "Yes"
  else:
    return "No"

N, P, Q, R = [int(x) for x in input().split()]
A = [int(x) for x in input().split()] #サイズN(0~N-1)
print(validate(N, P, Q, R, A))
N = int(input())
A = list(map(int, input().split()))

a = A[:N]
count = 0
while True:
  if all(map(lambda x: x%2 == 0, a)):
    a = list(map(lambda y: y/2, a))
    count += 1
  else:
    break
    
print(count)
from unittest import result


def some_sums(n_max, a, b):
  result = 0
  for n in range(1, n_max + 1):
    s = sum(list(map(int, list(str(n)))))
    if a <= s and s <= b:
      result += n 
  return result 
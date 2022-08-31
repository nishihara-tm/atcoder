def count_pattern(A, B, C, X):
  count = 0
  for a in range(A + 1):
    for b in range(B + 1):
      for c in range(C + 1):
        if (a * 500 + b * 100 + c * 50 == X):
          count += 1
  return count
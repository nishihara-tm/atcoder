
def get(x, y, n):
  if 3 * x <= y:
    return x * n
  else:
    y_num = (n // 3)
    x_num = n - (y_num * 3)
    return y_num * y + x_num * x
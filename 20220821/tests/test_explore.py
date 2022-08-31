import explore

def test_explore():
  # n, t, a, bonus
  a = [0] + [5, 7, 5]
  bonus = [0] * 5
  bonus[2] = 10
  assert explore.validate(4, 10, [0, 5, 7 ,5], [0, 0, 10, 0, 0]) == "Yes"
  assert explore.validate(4, 10, [0, 10, 7 ,5], [0, 0, 10, 0, 0]) == "No"
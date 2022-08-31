import coin

def test_coin():
  assert coin.count_pattern(2, 2, 2, 100) == 2
  assert coin.count_pattern(5, 1, 0, 150) == 0
  assert coin.count_pattern(30, 40, 50, 6000) == 213
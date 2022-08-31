import apple

def test_get():
  assert apple.get(10, 25, 10) == 85
  assert apple.get(10, 40, 10) == 100
  assert apple.get(100, 100, 2) == 200
  assert apple.get(100, 100, 100) == 3400
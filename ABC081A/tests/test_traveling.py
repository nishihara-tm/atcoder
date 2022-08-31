import traveling

def test_traveling():
  l = [
    {"t": 3, "x": 1, "y": 2},
    {"t": 6, "x": 1, "y": 1},
  ]
  assert traveling.possible(2, l)

  l = [
    {"t": 2, "x": 100, "y": 100}
  ]

  assert traveling.possible(1, l)

  l = [
    {"t": 5, "x": 1, "y": 1},
    {"t": 100, "x": 1, "y": 1}
  ]

  assert traveling.possible(2, l)
import iroha_haiku

def test_validate():
  # n, p, q, r, a
  assert iroha_haiku.validate(
    10, 5, 7, 5, 
    [1, 3, 2, 2, 2, 3, 1, 4, 3, 2]
  ) == "Yes"

  assert iroha_haiku.validate(
    9, 100, 101, 100, 
    [31, 41, 59, 26, 53, 58, 97, 93, 23]
  ) == "No"

  assert iroha_haiku.validate(
    7, 1, 1, 1, 
    [1, 1, 1, 1, 1, 1, 1]
  ) == "Yes"
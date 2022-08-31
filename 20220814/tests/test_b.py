import b

def test_validate():
  assert b.validate(3, 5) == "black"
  assert b.validate(4, 5) == "white"
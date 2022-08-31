import no2

def test_validate():
  assert no2.validate("()()") == True
  assert no2.validate("(()())(())") == True
  assert no2.validate("()()()()()()()()") == True
  assert no2.validate(")(") == False
  assert no2.validate(")))()(((") == False
  assert no2.validate("((((a))))") == False
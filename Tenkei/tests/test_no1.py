import no1

def test_binary_search():
  assert no1.binary_search([1,2,3,4,10], 8) == -1
  assert no1.binary_search([1,4,6,8,10], 8) == 3
  assert no1.binary_search([1,6,8,10], 8) == 2
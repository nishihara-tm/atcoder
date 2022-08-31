import hakutyuumu

def test_validate():
  assert hakutyuumu.main("erasedream") == "YES"
  assert hakutyuumu.main("dreameraser") == "YES"
  assert hakutyuumu.main("dreamerer") == "NO"
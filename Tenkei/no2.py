
def validate(s): 
  q = []
  for c in s:
    if c == "(":
      q.append("(")
    elif c == ")":
      try: 
        q.pop()
      except IndexError as e:
        print(e)
        return False
    else:
      return False

  if len(q) == 0:
    return True
  else:
    return False
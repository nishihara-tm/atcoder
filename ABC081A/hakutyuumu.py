
def validate(s, t):
  options = ['dream', 'dreamer', 'erase', 'eraser']
  words = [t + x for x in options]
  print(words)
  # 次の４つの値に一つでも正解が含まれたら return YES
  if any(w == s for w in words):
    return ["YES"]
  # 次の４つの値の長さが全て正解より長かったら return NO
  if all(len(w) > len(s) for w in words):
    return ["NO"]
  # それ以外の場合はt = t + "コウホ"したものを再帰的に呼ぶ
  ans = [validate(s, t + o) for o in options]
  flatten = lambda x: [z for y in x for z in (flatten(y) if hasattr(y, '__iter__') and not isinstance(y, str) else (y,))]
  flatten_words = flatten(ans)
  return flatten_words

def main(s):
  l = validate(s, "")
  if "YES" in l:
    return "YES"
  else:
    return "NO"
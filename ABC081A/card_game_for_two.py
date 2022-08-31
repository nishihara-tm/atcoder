def card_game(N, a):
  a.sort()
  scores = {"Alice": 0, "Bob": 0}
  is_alice_turn = True
  while len(a) > 0:
    player = "Alice" if is_alice_turn else "Bob"
    scores[player] += a.pop()
    is_alice_turn = not is_alice_turn

  return scores["Alice"] - scores["Bob"]
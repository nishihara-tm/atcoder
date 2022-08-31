import card_game_for_two

def test_card_game():
  assert card_game_for_two.card_game(2, [3, 1]) == 2
  assert card_game_for_two.card_game(2, [2, 7, 4]) == 5
  assert card_game_for_two.card_game(4, [20, 18, 2, 18]) == 18
R,C = map(int, input().split())

def validate(r, c):
  board = []
  for i in range(15):
    row = [True] * 15
    board.append(row)

  # board[0][0] = False

  for i in range(1,14):
    board[i][1] = False 
    board[1][i] = False
    board[13][i] = False
    board[i][13] = False

  for j in range(3,12):
    board[j][3] = False 
    board[3][j] = False 
    board[j][11] = False 
    board[11][j] = False 
#
  for k in range(5,10):
    board[k][5] = False
    board[5][k] = False
    board[k][9] = False
    board[9][k] = False

#
  board[7][7] = False 

  if board[r-1][c-1]:
    return "black"
  else:
    return "white"
  
print(validate(R,C))
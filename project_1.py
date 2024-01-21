import random

### STEP 1

def evaluate (board):
  for i in range(len(board) -2 ):
    if board[i : i+3] == 'xxx':
      print('You win!')
      return 'x'
    elif board[i : i+3] == 'ooo':
      print("The computer wins!")
      return 'o'
  if '-' not in board:
    print('Draw!')
    return '!'

  return'-'


### STEP 2

def move (board, mark, position):
    board[position-1] = mark

def update_board(board, mark, position):
    move(board, mark, position)
    print(board)
    return board

### STEP 3

def player_move(board):
  valid_inputs = list(range(1, 20))


  while True:
    position = int(input('At which position do you want to place your mark? '))

    if position < 0 or position > 19:
      print('Please provide a number between 0 and 19: ')
    elif board[position-1] != '-':
      print('This position is already occupied. Please choose another: ')
    else:
      move(board, 'x', position)
      break
  print('The computer is up next.')
  return board


### STEP 4

def pc_move(board):
  valid_inputs = list(range(1, 20))

  position = random.choice(valid_inputs)
  print('The computer sets its nought at position:', position)

  while True:
    if board[position - 1] == '-':
      move(board, 'o', position)
      break
    else:
      position = random.choice(valid_inputs)
  print('You are up next.')
  return board


### STEP 5
def D1_tictactoe(board):

  while True:
    result = evaluate("".join(board))
    if result == 'x' or result == 'o':
      print(result)
      break
    else:
      board = player_move(board)
      print("".join(board))
      board = pc_move(board)
      print("".join(board))



game_board = list(20*'-')
D1_tictactoe(game_board)
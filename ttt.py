board = [['_','_','_'],
         ['_','_','_'],
         ['_','_','_']]

symbols = ['X', 'O']
turn = 0

# Prints the board
def print_board():
  for row in board:
    for col in row:
      print(col, end=' ')
    print()

# Inserts a move at a given row & column
def make_move(row, col, symbol):
  if not space_taken(row, col):
    board[row][col] = symbol
  else:
    print('Space Already Taken - Try Again')
    r_choice = int(input('Which row would you like to choose? '))
    c_choice = int(input('Which column would you like to choose? '))
    make_move(r_choice, c_choice, symbol)


# Returns true when the game is over 
# Note: Just a stub. Doesn't work yet
def is_game_over():
  return False

# Alternates the turn between 0 and 1
def change_turn():
  global turn
  turn = (turn + 1) % 2

# Prints a title screen for the game
def welcome_screen():
  print('''
d888888b d888888b  .o88b. 
`~~88~~'   `88'   d8P  Y8 
   88       88    8P      
   88       88    8b      
   88      .88.   Y8b  d8 
   YP    Y888888P  `Y88P' 
                          
                          
d888888b  .d8b.   .o88b.  
`~~88~~' d8' `8b d8P  Y8  
   88    88ooo88 8P       
   88    88~~~88 8b       
   88    88   88 Y8b  d8  
   YP    YP   YP  `Y88P'  
                          
                          
d888888b  .d88b.  d88888b 
`~~88~~' .8P  Y8. 88'     
   88    88    88 88ooooo 
   88    88    88 88~~~~~ 
   88    `8b  d8' 88.     
   YP     `Y88P'  Y88888P 
  ''')

# returns true if space at index row, col has been taken
# returns false otherwise
def space_taken(row, col):
  if board[row][col] != '_':
    return True
  else:
    return False
welcome_screen()
while not is_game_over():
  

  # Print the board and whose turn it is
  print_board()
  print('Player {}'.format(turn+1))

  # Get the user input
  row_choice = int(input('Which row would you like to choose? '))
  while (row_choice < 0 or row_choice > 2):
    print("Please choose a number between 0 and 2")
    row_choice = int(input('Which row would you like to choose?')) 
    
  col_choice = int(input('Which column would you like to choose? '))
  while (col_choice < 0 or col_choice > 2):
    print("Please choose a number between 0 and 2")
    col_choice = int(input('Which column would you like to choose? '))

  # Put their move on the board
  make_move(row_choice, col_choice, symbols[turn])

  # Next turn
  change_turn()

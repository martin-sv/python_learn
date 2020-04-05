from IPython.display import clear_output

def start_game(players):
    players[0] = input("Please pick a marker 'X' or 'O': ").upper()
    players[1] = 'X' if players[0] == 'O' else 'O'
    print(f"Player 1 is {players[0]} and Player 2 is {players[1]}")
    return players

def start_game_default(players):
    players[0] = "X"
    players[1] = "Y"
    return players

def display_board(board):
    print(f" {board[7]} | {board[8]} | {board[9]}")
    print(f" {board[4]} | {board[5]} | {board[6]}")
    print(f" {board[1]} | {board[2]} | {board[3]}")

def play(current_player, players, board):
    position = int(input('Please enter a number: '))
    board[position] = 'X' if players[current_player] == 'X' else 'O'

def next_player(current_player):
    return 0 if current_player == 1 else 1

def check_winner(players, board, game_end):
    winning_combinations = [[7,8,9],[4,5,6],[1,2,3],[7,4,1],[8,5,2],[9,6,3],[7,5,3],[1,5,9]]
    for x in winning_combinations:
        if board[x[0]] == board[x[1]] == board[x[2]] and board[x[0]] != ' ':
            return True
    return False

players = [''] * 2]
board = {}
for x in range(1,10):
    board[x] = ' '
game_end = False
winner = ''
current_player = 0

#players = start_game(players)
players = start_game_default(players)
print(players)
display_board(board)

while (not game_end):
    play(current_player, players, board)
    clear_output()
    display_board(board)
    game_end = check_winner(players, board, game_end)
    if game_end: winner = current_player
    current_player = next_player(current_player)
print(f"The Winner is Player {winner+1}")
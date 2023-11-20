from tictactoe import TicTacToe
from players import HumanPlayer


def play_game(game, x_player, o_player):
    while game.empty_squares():
        game.print_board()
        x_move = X_player.make_move()
        x_feedback = game.register_move(x_move)
        if not x_feedback:
            x_player.moves = x_player.moves[:-1]
            continue
        
        if game.available_moves == []:
            game.print_board()
            print('It is a Tie')
            break
        
        o_move = o_player.make_move()
        o_feedback = game.register_move(o_move)
        if not o_feedback:
            o_player.moves = o_player.moves[:-1]
            continue
        
        x_score = game.score(x_player.moves)
        o_score = game.score(o_player.moves)
        
        if x_score:
            print(f'X Wins')
            game.print_board()
            break
        elif o_score:
            print('O Wins')
            game.print_board()
            break
        else:
            continue

game_instance = TicTacToe()
X_player = HumanPlayer('X')
O_player = HumanPlayer('O')
if __name__ == '__main__':
    play_game(game_instance, X_player, O_player)
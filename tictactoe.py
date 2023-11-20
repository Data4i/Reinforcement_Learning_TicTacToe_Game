from positions import WP


class TicTacToe:
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None
        self.available_moves = list(range(9))
        self.winning_moves = WP

    @staticmethod
    def make_board():
        return ['_' for i in range(9)]

    def print_board(self):
        print(f'{self.board[0]} | {self.board[1]} | {self.board[2]}')
        print(f'{self.board[3]} | {self.board[4]} | {self.board[5]}')
        print(f'{self.board[6]} | {self.board[7]} | {self.board[8]}')
        print(f'Available Moves -> {self.available_moves}')

    def register_move(self, L_S):
        letter, square = L_S
        if square not in self.available_moves:
            print(f'{square} is already filled')
            return False
        else:
            self.board[square] = letter
            self.available_moves.remove(square)
            return True

    def score(self, moves):
        recent_moves = set(moves[-3:])
        return True if recent_moves in self.winning_moves else False

    def empty_squares(self):
        return '_' in self.board


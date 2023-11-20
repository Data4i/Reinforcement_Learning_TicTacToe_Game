class Player:
    def __init__(self, letter):
        self.letter = letter

    def make_move(self, ):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        self.moves = list()

    def make_move(self):
        move = int(input(f'{self.letter} Please enter your move from the available moves: '))
        self.moves.append(move)
        return self.letter, move

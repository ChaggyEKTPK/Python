import random
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]
    def make_move(self):
        valor_aleatorio = random.choice(self.moves)
        resultado = tuple(x + y for x, y in zip(self.position, valor_aleatorio))
        self.position = resultado
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    def level_up(self):
        self.moves.extend([(1, 1), (1, -1), (-1, -1), (-1, 1)])
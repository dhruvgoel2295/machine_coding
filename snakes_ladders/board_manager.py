from models.board import Board
from services.board_service import BoardService

class BoardManager(object):
    def __init__(self, board=None, players=None):
        self.board = {}
        self.players = []
        self.player_positions = {}
        self.board_service = BoardService()

    def add_player(self, name):
        self.players.append(name)
        self.player_positions[name] = 0

    def add_board(self, snakes, ladders, cells=100):
        self.board = Board(snakes, ladders, cells)

    def get_player_position(self, player):
        return self.player_positions[player]

    def update_player_position(self, player, new_position):
        self.player_positions[player] = new_position

    def play_turn(self, player, steps):
        curr_position = self.player_positions[player]
        if curr_position + steps == 100:
            return 100
        else:
            return self.board_service.move_position(self.board, curr_position, steps)




from board_manager import BoardManager
from services.dice import Dice

class Driver(object):
    def __init__(self):
        self.board_manager = BoardManager()
        self.dice = Dice()

    def play_game(self):
        while True:
            for player in self.board_manager.players:
                steps = self.roll_dice()
                previous_position = self.board_manager.get_player_position(player)
                new_position = self.board_manager.play_turn(player, steps)
                self.board_manager.update_player_position(player, new_position)
                print("%s rolled a %d and moved from %d to %d" % (player, steps, previous_position, new_position))
                if new_position == 100:
                    print("%s wins the game" % (player))
                    return


    def roll_dice(self):
        return self.dice.roll()

    def add_player(self, player_name):
        self.board_manager.add_player(player_name)

    def create_board(self, snakes, ladders):
        self.board_manager.add_board(snakes, ladders)

    def main(self):
        num_snakes = int(input())
        snakes = []
        for i in range(num_snakes):
            snake = list(map(int,input().split()))
            snakes.append(snake)
        num_ladders = int(input())
        ladders = []
        for i in range(num_ladders):
            ladder = list(map(int,input().split()))
            ladders.append(ladder)
        self.create_board(snakes, ladders)
        num_players = int(input())
        for i in range(num_players):
            name = input()
            self.add_player(name)
        self.play_game()

driver_obj = Driver()
driver_obj.main()
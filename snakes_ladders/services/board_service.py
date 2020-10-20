

class BoardService(object):
    def move_position(self, board, position, steps):
        new_position = position + steps
        if new_position > 100:
            return position
        while (new_position in board.snakes or new_position in board.ladders) and new_position <= 100:
            if new_position == 100:
                return new_position
            prev_position = new_position
            if prev_position in board.snakes:
                new_position = board.snakes[new_position]
            elif new_position in board.ladders:
                new_position = board.ladders[new_position]

        if new_position > 100:
            return prev_position
        return new_position





class Board(object):
    def __init__(self, snakes, ladders, cells=100):
        self.cells = cells
        self.snakes = {}
        for snake in snakes:
            self.snakes[snake[0]] = snake[1]
        self.ladders = {}
        for ladder in ladders:
            self.ladders[ladder[0]] = ladder[1]


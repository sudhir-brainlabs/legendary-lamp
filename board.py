PATH_BOARD_LAYOUT = 'scrabble_board.csv'

class Location:

    HORIZONTAL = 'HORIZONTAL'
    VERTICAL = 'VERTICAL'

    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation


class Board:

    def __init__(self):
        self.layout = []
        with open(PATH_BOARD_LAYOUT) as f:
            for row in csv.reader(f):
                self.layout.append(row)

    

    
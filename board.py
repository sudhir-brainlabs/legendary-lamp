import csv




class Location:

    HORIZONTAL = 'HORIZONTAL'
    VERTICAL = 'VERTICAL'
   
    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation

    def positionsFor(self, word):
        x_step = 1 if self.orientation == self.HORIZONTAL else 0
        y_step = 1 if self.orientation == self.VERTICAL else 0

        x = self.x
        y = self.y

        for char in word:
            yield char, (x, y)
            x += x_step
            y += y_step


class Board:

    DOUBLE_WORD = 'DW'
    TRIPLE_WORD = 'TW'

    DOUBLE_LETTER = 'DL'
    TRIPLE_LETTER = 'TL'

    def __init__(self, path, scorer):
        self.scorer = scorer

        self.layout = []
        with open(path) as f:
            for row in csv.reader(f):
                self.layout.append(row)

    def score_word(self, word, location):
        score = 0
        multiplier = 1

        for char, position in location.positionsFor(word):
            tile_type = self[position]
            char_score = self.scorer[char]
            
            if tile_type == self.DOUBLE_WORD:
                score += char_score
                multiplier *= 2
            elif tile_type == self.TRIPLE_WORD:
                score += char_score
                multiplier *= 3
            elif tile_type == self.DOUBLE_LETTER:
                score += (char_score * 2)
            elif tile_type == self.TRIPLE_LETTER:
                score += (char_score * 3)
            else:
                score += char_score

        return score * multiplier

            
    def __getitem__(self, position):
        x, y = position
        return self.layout[y][x]
    

    
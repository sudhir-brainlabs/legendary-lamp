import csv


class Location():

    HORIZONTAL = 'HORIZONTAL'
    VERTICAL = 'VERTICAL'
   
    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation

    def __str__(self):
        return "{} at ({},{})".format(self.orientation, self.x, self.y)

    def positionsFor(self, word):
        x_step = 1 if self.orientation == self.HORIZONTAL else 0
        y_step = 1 if self.orientation == self.VERTICAL else 0

        x = self.x
        y = self.y

        for char in word:
            yield char, (x, y)
            x += x_step
            y += y_step


class Board():

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

    def __getitem__(self, position):
        x, y = position
        return self.layout[y][x]

    @property
    def width(self):
        return len(self.layout[0])

    @property
    def height(self):
        return len(self.layout)

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

    def find_optimal_locations(self, word):
        best_score = 0
        best_locations = []
        for location in self.possible_locations(word):
            score = self.score_word(word, location)
            if score > best_score:
                best_score = score
                best_locations = [location]
            elif score == best_score:
                best_locations.append(location)
        return best_locations

    def possible_locations(self, word):       
        for x in range(0, self.width - len(word) + 1):
            for y in range(0, self.height):
                yield Location(x, y, Location.HORIZONTAL)

        for y in range(0, self.height - len(word) + 1):
            for x in range(0, self.width):
                yield Location(x, y, Location.VERTICAL)
import csv
import enchant

def play():
    dictionary, letter_scores, board_layout = setup()

    word = get_input(dictionary)
    word_score = get_score(letter_scores, word)
    print(f'"{word}" scores {word_score} points.')

###############################################################################

def setup():
    dictionary = enchant.Dict("en_UK")
    letter_scores_file_path = 'scrabble_score.csv'
    letter_scores = get_letter_scores(letter_scores_file_path)
    
    board_file_path = 'scrabble_board.csv'
    board_layout = read_board_layout(board_file_path)

    return dictionary, letter_scores, board_layout

def get_letter_scores(letter_scores_file_path):  
    letter_scores = {} 
    with open(letter_scores_file_path) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            letter_scores[row[0]] = int(row[1])
    return letter_scores

def get_input(dictionary):
    is_a_word = False
    while not is_a_word:
        word = input('Enter your word: ')
        if (not word or word.isnumeric()):
            print('That is not a string!')
            continue
        is_a_word = dictionary.check(word)
        if (not is_a_word):
            print('Did you mean:', dictionary.suggest(word))
    return word

def get_score(letter_scores, word):
    word = word.lower()
    word_score = 0
    for letter in word:
        word_score += letter_scores[letter]
    return word_score

def read_board_layout(board_file_path):
    board_layout = []
    with open(board_file_path) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            board_layout.extend([row])
    return board_layout



# # check for invalid starting position
# position = input('Enter position of starting square in the form [0, 0]: ')

# # check orientation is ONLY down or right
# orientation = input('Enter \'down\' or \'right\': ')

###############################################################################

if __name__ == '__main__':
    play()
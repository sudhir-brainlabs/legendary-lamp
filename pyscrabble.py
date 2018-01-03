import os
import csv

import enchant

from board import Board, Location

PATH_BOARD_LAYOUT = 'scrabble_board.csv'
PATH_LETTER_SCORES = 'scrabble_score.csv';



def play():
    dictionary = enchant.Dict("en_UK")
    
    letter_scores = get_letter_scores(PATH_LETTER_SCORES) 

    word = get_word(dictionary)
    word_score = get_score(letter_scores, word)
    print(f'"{word}" scores {word_score} points.')


def get_letter_scores(path):  
    letter_scores = {} 
    with open(path) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            letter_scores[row[0]] = int(row[1])
    return letter_scores


def get_word(dictionary):
    while True:
        word = input('Enter your word: ')
        if dictionary.check(word):
            return word
        suggestions = dictionary.suggest(word)[:5]
        print('That word is not in the dictionary.')
        if suggestions:
            print('Suggestions: {}'.format(', '.join(suggestions)))


def get_score(letter_scores, word):
    word = word.lower()
    word_score = 0
    for letter in word:
        word_score += letter_scores[letter]
    return word_score

def ex2():
    dictionary = enchant.Dict("en_UK")
    word = get_word(dictionary)

    scorer = get_letter_scores(PATH_LETTER_SCORES)

    board = Board(PATH_BOARD_LAYOUT, scorer)
    score = board.score_word(
        word,
        Location(3, 3, Location.VERTICAL)
    )
    print(score)


# # check for invalid starting position
# position = input('Enter position of starting square in the form [0, 0]: ')

# # check orientation is ONLY down or right
# orientation = input('Enter \'down\' or \'right\': ')

###############################################################################

if __name__ == '__main__':
    ex2()
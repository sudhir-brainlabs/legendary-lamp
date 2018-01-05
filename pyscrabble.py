import os
import csv

import enchant

from board import Board, Location

PATH_BOARD_LAYOUT = 'scrabble_board.csv'
PATH_LETTER_SCORES = 'scrabble_score.csv'


def load_scorer(path):
    scorer = {}
    with open(path) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            char, score = row
            scorer[char] = int(score)
    return scorer


def get_word(dictionary):
    while True:
        word = input('Enter your word: ').lower()
        if dictionary.check(word):
            return word
        suggestions = dictionary.suggest(word)[:5]
        print('That word is not in the dictionary.')
        if suggestions:
            print('Suggestions: {}'.format(', '.join(suggestions)))


def get_score(word, scorer):
    score = 0
    for char in word:
        score += scorer[char]
    return score


def ex1():
    dictionary = enchant.Dict("en_UK")
    word = get_word(dictionary)

    scorer = load_scorer(PATH_LETTER_SCORES)

    score = get_score(word, scorer)
    print(score)

def ex2():
    dictionary = enchant.Dict("en_UK")
    word = get_word(dictionary)

    scorer = load_scorer(PATH_LETTER_SCORES)

    board = Board(PATH_BOARD_LAYOUT, scorer)
    score = board.score_word(
        word,
        Location(3, 3, Location.VERTICAL)
    )
    print(score)

def ex3():
    dictionary = enchant.Dict("en_UK")
    word = get_word(dictionary)

    scorer = load_scorer(PATH_LETTER_SCORES)

    board = Board(PATH_BOARD_LAYOUT, scorer)
    locations = board.find_optimal_locations(word)

    for location in locations:
        print(location)
    print("Scoring {}".format(board.score_word(word, location)))


###############################################################################

if __name__ == '__main__':
    ex3()
import os
import csv

import enchant

from board import Board, Location

PATH_BOARD_LAYOUT = 'scrabble_board.csv'
PATH_LETTER_SCORES = 'scrabble_score.csv'
PATH_WORD_LIST = 'english_word_list.txt'

ORIENTATION_NAMES = {
    'h': Location.HORIZONTAL,
    'v': Location.VERTICAL
}

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

def get_location():
    x, y = map(int, input('Enter x-y coordinates in form x,y: ').replace(' ', '').split(','))
    orientation_input = input('Enter v for vertical or h for horizontal only: ').strip()
    orientation = ORIENTATION_NAMES[orientation_input]

    return Location(x, y, orientation)

def ex1():
    dictionary = enchant.Dict("en_UK")
    word = get_word(dictionary)

    scorer = load_scorer(PATH_LETTER_SCORES)

    score = get_score(word, scorer)
    print(score)

def ex2():
    dictionary = enchant.Dict("en_UK")
    word = get_word(dictionary)
    location = get_location()

    scorer = load_scorer(PATH_LETTER_SCORES)

    board = Board(PATH_BOARD_LAYOUT, scorer)
    score = board.score_word(
        word,
        location
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
    print("Scoring {}".format(board.score_word(word, locations[0])))

def find_highest_scoring_word():
    scorer = load_scorer(PATH_LETTER_SCORES)
    board = Board(PATH_BOARD_LAYOUT, scorer)
    dictionary = enchant.Dict("en_UK")
    highest_score = 0
    best_word = ""

    with open(PATH_WORD_LIST) as word_list:
        for i, word in enumerate(word_list):
            if i % 1000 == 0:
                print(i, best_word, highest_score)
 
            word = word.lower().strip()

            if not dictionary.check(word): 
                continue

            try: 
                locations = board.find_optimal_locations(word)
                word_score = board.score_word(word, locations[0])
            except IndexError:
                continue

            if word_score > highest_score:
                highest_score = word_score
                best_word = word

    print('Highest scoring word was "{}" with score {}'.format(best_word, highest_score))

###############################################################################

if __name__ == '__main__':
    find_highest_scoring_word()
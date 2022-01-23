'''
  This module gives functions to help you to solve WORDLE.
'''

from json import load
from os.path import abspath
from re import search

import numpy as np


class WordleHelper():
    '''The Helper Class'''

    def __init__(self, datafile_name='.././data/words_dictionary.json', word_len=5):
        self._word_len = word_len
        self.load_words(datafile_name, inplace=True)
        self.filter_len(word_len, inplace=True)

    def __repr__(self) -> str:
        return str(self._words[:20])

    def set_words(self, words) -> None:
        '''Sets the directory array.'''
        self._words: np.ndarray = words

    def get_words(self) -> np.ndarray:
        '''Returns the dictionary.'''
        return self._words

    def load_words(self, datafile_name, inplace=False) -> np.ndarray:
        '''Loads the dictionary json file.'''
        path = abspath(datafile_name)
        with open(path, encoding='utf-8') as words_file:
            loaded_words = np.array(list(load(words_file).keys()))
        if inplace:
            self.set_words(loaded_words)
        return loaded_words

    def filter_len(self, word_len, inplace=False) -> np.ndarray:
        '''Filters the dictionary based on given length.'''
        filtered_list: np.array = np.empty(0)
        for word in self.get_words():
            if len(word) == word_len:
                filtered_list = np.append(filtered_list, word)
        if inplace:
            self.set_words(filtered_list)
        return filtered_list

    def filter_regexp(self, regex: str, inplace=False):
        '''Filtering based on regular expression.'''
        filtered_list: np.array = np.empty(0)
        for word in self.get_words():
            if search(regex, word):
                filtered_list = np.append(filtered_list, word)
        if inplace:
            self.set_words(filtered_list)
        return filtered_list

    def filter_contains(self, characters: str, inplace=False):
        '''Filter based on containing the given character.'''
        filtered_list: np.array = np.empty(0)
        for word in self.get_words():
            if all(x in word for x in characters):
                filtered_list = np.append(filtered_list, word)
        if inplace:
            self.set_words(filtered_list)
        return filtered_list

    def filter_not_contains(self, characters: str, inplace=False):
        '''Filter based on not containing any of the given characters.'''
        filtered_list: np.array = np.empty(0)
        for word in self.get_words():
            if all(x not in word for x in characters):
                filtered_list = np.append(filtered_list, word)
        if inplace:
            self.set_words(filtered_list)
        return filtered_list

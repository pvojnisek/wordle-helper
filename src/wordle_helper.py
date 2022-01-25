'''
  This module gives functions to help you to solve WORDLE.
'''

from re import search
import numpy as np
from data_loader import load_english_words_from_github


class WordleHelper():
    '''The Helper Class'''

    def __init__(self):
        self._words = load_english_words_from_github()

    def __repr__(self) -> str:
        sample = np.random.choice(self._words, 10)
        return f'10 sample: {str(sample)}, all words: {len(self._words)}'

    def set_words(self, words) -> None:
        '''Sets the directory array.'''
        self._words: np.ndarray = np.unique(words)

    def get_words(self) -> np.ndarray:
        '''Returns the dictionary.'''
        return self._words

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

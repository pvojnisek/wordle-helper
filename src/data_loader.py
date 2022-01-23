'''
    Module loads data from external github repository https://github.com/dwyl/english-words.
    Functions:
       - loading dictionary from the repository
       - fitlering out 5 character long words
       - caching
'''


from requests import get

import numpy as np
import caching

WORD_LENGTH = 5
WORDS_GIT_DICTIONARY_URL = 'https://github.com/dwyl/english-words/raw/master/words_dictionary.json'
WORDS_FROM_GIT = 'words-from-git'


def load_from_cache() -> list:
    '''Loads word list from local cache.'''
    return caching.load_from_cache(WORDS_FROM_GIT)


def save_to_cache(lst: np.ndarray) -> None:
    '''Saves list to local cache.'''
    caching.save_to_cache(WORDS_FROM_GIT, lst)


def filter_length(words: np.ndarray) -> np.ndarray:
    '''Filters the words list by length.'''
    filtered_list: np.array = np.empty(0)
    for word in words:
        if len(word) == WORD_LENGTH:
            filtered_list = np.append(filtered_list, word)
    return filtered_list


def load_english_words_from_github() -> list:
    '''
        Loads English words from this repo: https://github.com/dwyl/english-words/
    '''
    words = load_from_cache()
    if len(words) == 0:
        words = np.array(list(get(WORDS_GIT_DICTIONARY_URL).json().keys()))
        words = filter_length(words)
        save_to_cache(words)
        print(f'{len(words)} words loaded from {WORDS_GIT_DICTIONARY_URL}')
    else:
        print(f'{len(words)} words loaded from the cache')
    return words

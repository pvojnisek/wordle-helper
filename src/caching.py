'''
    This module handles the json file cache.
'''


from os.path import isfile, join

import json
import numpy as np


FILESTORE_PATH = '.'


def save_to_cache(cache_id: str, data: np.ndarray):
    '''Saves the data into a file determined by the cache_id'''
    with open(__get_cache_filename(cache_id), 'w', encoding='utf-8') as jsonfile:
        json.dump(data.tolist(), jsonfile)
    print('cache saved: ' + __get_cache_filename(cache_id))


def load_from_cache(cache_id: str) -> np.ndarray:
    '''Loads data from a file based on cache_id.'''
    filename = __get_cache_filename(cache_id)
    if isfile(filename):
        with open(filename, encoding='utf-8') as words_file:
            lst = np.array(list(json.load(words_file)))
            print(f'cache loaded: {filename} - {len(lst)} words')
            return lst
    else:
        return np.empty(0)


def __get_cache_filename(cache_id: str):
    '''Generates a filename from the cache_id.'''
    return join(FILESTORE_PATH, str(cache_id) + '.json')

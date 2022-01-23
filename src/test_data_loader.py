'''
    Testing functions for loading data from external resources.
'''


import unittest
import data_loader as dl


class TestDataLoaderFunctions(unittest.TestCase):
    '''To test the loader functions.'''

    def test_json_loader(self):
        '''Basic loader tests.'''
        lst = dl.load_english_words_from_github()
        self.assertIsNotNone(lst)
        self.assertGreater(len(lst), 1000)
        print(lst)

    def test_caching(self):
        '''
            TODO: write tests to check if caching is OK.
        '''

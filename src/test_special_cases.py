'''
    Testing special cases.
'''


import unittest
import numpy as np
from solver import Solver

from wordle_helper import WordleHelper


class FakeWordleHelper(WordleHelper):
    def __init__(self, words: np.ndarray):
        self._words = words


class FakeSolver(Solver):
    def __init__(self, words: np.ndarray) -> None:
        self._wh = FakeWordleHelper(words)


class SpecialCasesTest(unittest.TestCase):
    '''Special cases'''

    def test_repeated_letters_in_suggestion(self):
        '''
            Repeated characters in hint. This case refers to https://github.com/pvojnisek/wordle-helper/issues/1
            The solution is `SUGAR`, hint is `SPAES`.
            No exception should be raised. The Wordle game returns `gbybb`
        '''
        words = np.array(['asdfg', 'aassd', 'sugar', 'satre', 'speas'])
        solver = FakeSolver(words)

        solver.process_pattern('ttttt', 'bbbbb')
        self.assertEqual(len(solver.get_words()), 4, 'Words containting `t` must be filtered out!')
        self.assertTrue('satre' not in solver.get_words(), '`satre` had to filtered out, because it contains letter `t`!')
        self.assertTrue('sugar' in solver.get_words(), '`sugar` has to be in the filtered word list!')

        solver.process_pattern('speas', 'gbybb')
        self.assertListEqual(['sugar'], solver.get_words().tolist(), 'word `sugar` has to be the only solution!')

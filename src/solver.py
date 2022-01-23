'''
    Main module for the cli functions.
'''

import numpy as np
from wordle_helper import WordleHelper


class Solver():
    '''The class handles pattern and next word recommendation functions.'''

    def __init__(self) -> None:
        self._wh = WordleHelper()

    def pick_suggestion(self) -> str:
        '''Returns with a random word from the active directory.'''
        return np.random.choice(self._wh.get_words())

    def process_pattern(self, word: str, pattern: str):
        '''
            Filters the dictionary based on the pattern. The pattern should look like this:
            "bbbyg" - 3 x black, yellow, green
            black - letter not in the word
            yellow - letter is in the word but on wrong place
            green - hit. Right letter at the right position
        '''
        for i in range(0, 5):
            if pattern[i] == 'b':
                self._wh.filter_not_contains(word[i], inplace=True)
            elif pattern[i] == 'y':
                self._wh.filter_contains(word[i], inplace=True)
                regex = '.' * i + f'[^{word[i]}]' + '.' * (4-i)
                self._wh.filter_regexp(regex, inplace=True)
            elif pattern[i] == 'g':
                regex = '.' * i + word[i] + '.' * (4-i)
                self._wh.filter_regexp(regex, inplace=True)

    def __repr__(self) -> str:
        return str(self._wh)


def main():
    '''Main function for cli mode'''

    print('Welcome to Wordle Solver!')
    print('Please visit the url for the game: https://www.powerlanguage.co.uk/wordle/')
    print('Initializing..')

    solver: Solver = Solver()
    userinput: str = ''

    while userinput not in ['x', 'exit', 'quit', ' ']:
        word = solver.pick_suggestion()
        print(f'Suggestion: {word}')
        userinput = input(f'  Enter results pattern (b-black, y-yellow, g-green):\n  {word}\n->')
        if len(userinput) == 5:
            print('   Filtering..')
            solver.process_pattern(word, userinput)
            print(f'  {solver}')


if __name__ == '__main__':
    main()

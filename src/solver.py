from wordle_helper import WordleHelper
import numpy as np


class Solver():

    def __init__(self, datafile) -> None:
        self._wh = WordleHelper(datafile)

    def pick_a_random_word(self) -> str:
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

    print('Welcome to Wordle Solver!')
    print('Please visit the url for the game: https://www.powerlanguage.co.uk/wordle/')
    print('Initializing..')

    solver: Solver = Solver('./data/words_dictionary.json')
    userinput: str = ''

    while not userinput in ['x', 'exit', 'quit', ' ']:
        word = solver.pick_a_random_word()
        print(f'word: {word}')
        userinput = input(f'  Please write the results pattern (b-black, y-yellow, g-green):\n  {word}\n->')
        if len(userinput) == 5:
            print('   Filtering..')
            solver.process_pattern(word, userinput)
            print(f'  Results (top20): {solver}')


if __name__ == '__main__':
    main()
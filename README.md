# WORDLE Helper

There is a pupular game around [WORDLE](https://www.powerlanguage.co.uk/wordle/)

The game could be hard for non-English speaking people so I started to think of a helper for them to solve the game.

WORDLE Helper lists words from [English Words](https://github.com/dwyl/english-words/) database.

## 1. download dictionary

```
$ cd data
$ wget https://github.com/dwyl/english-words/raw/master/words_dictionary.json
```

## 2. start python in terminal

The scripts are written in Python 3.10.0

```
$ python --version
Python 3.10.0
```

## 3. install requirements

```
$ pip install -r requirements.txt
```

# Usage

## 1. Solve in cli

You can use the Solver from cli. Just start the solver.py from the project directory:
```
$ python ./src/solver.py
```

And follow the instructions. If the word given by the solver is not accepted by the game, just hit enter for the next word.

Have a nie time

## 2. Jupyter Notebook

You can initialize and filter the helper from the cells of the notebook. See `example.ipynb` in the src directory.

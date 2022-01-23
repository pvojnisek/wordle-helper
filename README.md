# WORDLE Helper and Solver

There is a pupular game around [WORDLE](https://www.powerlanguage.co.uk/wordle/)

The game could be hard for non-English speaking people so I started to think of a helper for them to solve the game.

WORDLE Helper uses words from [English Words](https://github.com/dwyl/english-words/) database. It loads them automatically and stores them in the project directory. During next initialization of the Helper it will load from the local file system. So the first start can be longer depending on the speed of your internet connection.

This is just a Saturday afternoon project to have some fun. The code is not optimized, nor tested (however I usually do tdd). Please handle this project this way. I also take any responibility about any demages this software does.. :) If you have any suggestions, please create a new issue or/and contribute!

# Installation and getting to work

After cloning the repository, you need to make sure the followings:

- you have python 3.10 installed
- install requirements

## 1. Checking Python

The scripts are written and tested in Python 3.10.0. They might work with different versions also. Please give a feedback if you try it with older or newer versions.

```
$ python --version
Python 3.10.0
```

## 3. install requirements

```
$ pip install -r requirements.txt
```

# Using the Helper

## 1. Solve wordle in cli

You can use the Solver from cli. Just start the solver.py from the project directory:
```
$ python ./src/solver.py
```

And follow the instructions. If the word given by the solver is not accepted by the game, just hit enter for the next word.

Have a nie time

## 2. Jupyter Notebook

You can initialize and filter the helper from the cells of the notebook. See `example.ipynb` in the src directory.

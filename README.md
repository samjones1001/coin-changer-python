# Coin Changer Kata ![travis build staus](https://travis-ci.com/samjones1001/coin-changer-python.svg?branch=master)[![codecov](https://codecov.io/gh/samjones1001/coin-changer-python/branch/master/graph/badge.svg)](https://codecov.io/gh/samjones1001/coin-changer-python)

A simple Python application for calculating the fewest number of coins with which a particular value of change can be reached.

### Setup

This project uses [pipenv](https://github.com/pypa/pipenv) to manage dependencies.

- If not already present on your system, install pipenv using `pip install pipenv`
- Intall dependencies using `pip install`

### Tests

Run the test suite using `pytest` from the command line.

### Execution

At present, this project can be run as a command line script using `python main.py [amount]` where amount represent the change you wish to calculate.

Output will be printed to the command line as a list of integers representing coins.a

For example:

```shell
$ python main.py 24
$ [20, 2, 2]
```


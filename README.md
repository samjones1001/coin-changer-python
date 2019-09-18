# Coin Changer Kata ![travis build status](https://travis-ci.com/samjones1001/coin-changer-python.svg?branch=master)  [![codecov](https://codecov.io/gh/samjones1001/coin-changer-python/branch/master/graph/badge.svg)](https://codecov.io/gh/samjones1001/coin-changer-python)

A simple Python application for calculating the fewest number of coins with which a particular value of change can be reached.

### Setup

This project uses [pipenv](https://github.com/pypa/pipenv) to manage dependencies.

- Clone this repository and navigate to its root directory in the command line
- If not already present on your system, install pipenv using `pip install pipenv`
- Install dependencies using `pipenv sync -d`

### Tests

In order to run the test suite, navigate to the projects root directory in the command line and run `pytest`.

### Execution

At present, this project can be run as a command line script.

Navigate to the project's root directory, then use `python main.py [amount]` where amount represents the change you wish to calculate.

Output will be printed to the command line as a list of integers representing coins.

For example:

```shell
$ python main.py 24
$ [20, 2, 2]
```


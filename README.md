py4ai logging
====

[![PyPI](https://img.shields.io/pypi/v/py4ai-logging.svg)](https://pypi.python.org/pypi/py4ai-logging)
[![Python version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://pypi.python.org/pypi/py4ai-logging)
[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://py4ai.github.io/py4ai-logging/)
![Python package](https://github.com/NicolaDonelli/py4ai-logging/workflows/CI%20-%20Build%20and%20Test/badge.svg)

--------------------------------------------------------------------------------


A Python library of utilities to handle loggers. 


## What is it ?
**py4ai-logging** is the Python package of the py4ai framework that provides utilities to handle loggers. 

## Features
The main features of this package are:
* the `py4ai.logging.WithLogging` class that is widely inherited throughout the py4ai framework as it provides its 
successors the handy `logger` property and `logResult` method that allows logging facilities natively integrated in 
our classes and easily configured with yaml configuration files.
* the `py4ai.logging.configFromFiles` function that automate the configuration of loggers based from yaml configuration 
files allowing the user to select whether or not to catch the warning and even specify which logger to use to catch 
exceptions. 

## Installation
From pypi server
```
pip install py4ai-logging
```

From source
```
git clone https://github.com/NicolaDonelli/py4ai-logging
cd py4ai-logging
make install
```

## Tests 
```
make tests
```

## Checks 
To run predefined checks (unit-tests, linting checks, formatting checks and static typing checks):
```
make checks
```

## How to contribute ? 

We are very much willing to welcome any kind of contribution whether it is bug report, bug fixes, contributions to the 
existing codebase or improving the documentation. 

### Where to start ? 
Please look at the [Github issues tab](https://github.com/NicolaDonelli/py4ai-logging/issues) to start working on open 
issues 

### Contributing to py4ai-logging 
Please make sure the general guidelines for contributing to the code base are respected
1. [Fork](https://docs.github.com/en/get-started/quickstart/contributing-to-projects) the py4ai-logging repository. 
2. Create/choose an issue to work on in the [Github issues page](https://github.com/NicolaDonelli/py4ai-logging/issues). 
3. [Create a new branch](https://docs.github.com/en/get-started/quickstart/github-flow) to work on the issue. 
4. Commit your changes and run the tests to make sure the changes do not break any test. 
5. Open a Pull Request on Github referencing the issue.
6. Once the PR is approved, the maintainers will merge it on the main branch.
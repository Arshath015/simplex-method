# Simplex Method Implementation
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/simplex-method)](https://pypi.org/project/simplex-method)

A numerical implementation of the Simplex method for linear programming, from first principles.

## Table of Contents
* [Overview](#overview)
* [Tech Stack](#tech-stack)
* [Architecture](#architecture)
* [Theoretical Background](#theoretical-background)
* [Installation](#installation)
* [Usage](#usage)
* [API Reference](#api-reference)
* [Case Study](#case-study)
* [Testing](#testing)
* [Limitations](#limitations)
* [Roadmap](#roadmap)
* [License](#license)

## Overview
The Simplex method is a widely used algorithm for solving linear programming problems. It is an iterative method that starts with a basic feasible solution and improves it at each step until an optimal solution is found.

## Tech Stack
* Python 3.8+
* NumPy
* SciPy

## Architecture
```text
simplex-method/
|--- notebooks/
|    |--- exploration.py
|--- src/
|    |--- simplex.py
|    |--- tableau.py
|    |--- utils.py
|--- tests/
|    |--- test_simplex.py
|    |--- test_tableau.py
|--- results/
|    |--- findings.md
```

## Theoretical Background
The Simplex method is based on the concept of a tableau, which is a matrix representation of the linear programming problem. The tableau is used to store the coefficients of the variables and the constraints, and to perform the necessary calculations to find the optimal solution.

The Simplex method consists of two main phases: the Phase I and Phase II. In Phase I, the method finds a basic feasible solution by minimizing the artificial variables. In Phase II, the method finds the optimal solution by maximizing the objective function.

## Installation
To install the Simplex method implementation, run the following commands:
```bash
pip install -r requirements.txt
 git clone https://github.com/user/simplex-method.git
```

## Usage
To use the Simplex method implementation, create an instance of the `Simplex` class and call the `solve` method:
```python
from src.simplex import Simplex

# Define the coefficients of the objective function and the constraints
c = np.array([3, 4])
b = np.array([7, 11, 8])
A = np.array([[1, 2], [3, 2], [2, 1]])

# Create an instance of the Simplex class and solve the problem
simplex = Simplex(c, A, b)
result = simplex.solve()
print(result)
```

## API Reference
* `Simplex(c, A, b)`: Creates an instance of the `Simplex` class.
* `solve()`: Solves the linear programming problem using the Simplex method.

## Case Study
See the [findings.md](results/findings.md) file for a written analysis of the results.

## Testing
To run the tests, execute the following command:
```bash
pytest tests/
```

## Limitations
The current implementation only supports problems with a small number of variables and constraints.

## Roadmap
* Improve the performance of the implementation for large problems.
* Add support for more advanced features, such as integer programming.

## License
This implementation is licensed under the MIT License.


## Requirements

```
pip install -r requirements.txt
```

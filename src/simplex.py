from typing import Tuple
import numpy as np

class Simplex:
    def __init__(self, c: np.ndarray, A: np.ndarray, b: np.ndarray):
        self.c = c
        self.A = A
        self.b = b
        self.tableau = None

    def create_tableau(self):
        # Create the initial tableau
        self.tableau = np.zeros((self.A.shape[0] + 1, self.A.shape[1] + 1))
        self.tableau[:self.A.shape[0], :self.A.shape[1]] = self.A
        self.tableau[:self.A.shape[0], -1] = self.b
        self.tableau[-1, :self.A.shape[1]] = -self.c

    def solve(self) -> Tuple[np.ndarray, float]:
        self.create_tableau()
        # Perform the Simplex method
        while True:
            # Find the pivot element
            pivot_row, pivot_col = self.find_pivot()

            # If no pivot element is found, the solution is optimal
            if pivot_row == -1:
                break

            # Perform the pivot operation
            self.pivot(pivot_row, pivot_col)

        # Extract the solution from the tableau
        x = np.zeros(self.c.shape)
        for i in range(self.c.shape[0]):
            x[i] = self.tableau[i, -1]
        return x, np.dot(self.c, x)

    def find_pivot(self) -> Tuple[int, int]:
        # Find the pivot element
        min_val = np.inf
        pivot_row = -1
        pivot_col = -1
        for i in range(self.tableau.shape[0] - 1):
            for j in range(self.tableau.shape[1] - 1):
                if self.tableau[i, j] < min_val:
                    min_val = self.tableau[i, j]
                    pivot_row = i
                    pivot_col = j
        return pivot_row, pivot_col

    def pivot(self, row: int, col: int):
        # Perform the pivot operation
        self.tableau[row, :] /= self.tableau[row, col]
        for i in range(self.tableau.shape[0] - 1):
            if i != row:
                self.tableau[i, :] -= self.tableau[i, col] * self.tableau[row, :]

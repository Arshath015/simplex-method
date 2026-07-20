import numpy as np

class Tableau:
    def __init__(self, A: np.ndarray, b: np.ndarray, c: np.ndarray):
        self.A = A
        self.b = b
        self.c = c
        self.tableau = None

    def create_tableau(self):
        # Create the initial tableau
        self.tableau = np.zeros((self.A.shape[0] + 1, self.A.shape[1] + 1))
        self.tableau[:self.A.shape[0], :self.A.shape[1]] = self.A
        self.tableau[:self.A.shape[0], -1] = self.b
        self.tableau[-1, :self.A.shape[1]] = -self.c

    def get_tableau(self) -> np.ndarray:
        return self.tableau

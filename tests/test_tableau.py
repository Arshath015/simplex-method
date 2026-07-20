import pytest
import numpy as np
from src.tableau import Tableau

# Test case 1: Creating a tableau from a simple linear programming problem
@pytest.mark.parametrize('A, b, c', [
    (np.array([[1, 2], [3, 2]]), np.array([7, 11]), np.array([3, 4]))
])
def test_create_tableau(A, b, c):
    tableau = Tableau(A, b, c)
    tableau.create_tableau()
    expected_tableau = np.array([[1, 2, 7], [3, 2, 11], [-3, -4, 0]])
    assert np.allclose(tableau.get_tableau(), expected_tableau)

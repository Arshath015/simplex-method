import pytest
import numpy as np
from src.simplex import Simplex

# Test case 1: A simple linear programming problem
@pytest.mark.parametrize('c, A, b', [
    (np.array([3, 4]), np.array([[1, 2], [3, 2]]), np.array([7, 11]))
])
def test_solve(c, A, b):
    simplex = Simplex(c, A, b)
    x, obj_val = simplex.solve()
    assert np.allclose(x, np.array([1, 2]))
    assert np.isclose(obj_val, 11)

# Test case 2: An edge case with an infeasible solution
@pytest.mark.parametrize('c, A, b', [
    (np.array([3, 4]), np.array([[1, 2], [3, 2]]), np.array([-7, 11]))
])
def test_infeasible(c, A, b):
    simplex = Simplex(c, A, b)
    with pytest.raises(ValueError):
        simplex.solve()

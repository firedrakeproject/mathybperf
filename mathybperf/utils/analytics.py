from mathybperf.utils.petsc_utils import petsc_to_py
from firedrake import *
import numpy as np


class Analytics(object):

    def __init__(self, tensor):
        self.A = tensor
        assembled = assemble(tensor, mat_type='aij')
        self.A_np = petsc_to_py(assembled.M.handle)

    def singular(self):
        # test if diagonal contain zeros
        assert not abs(np.diag(self.A_np)).min() == 0, "Diagonal contains zeros."

    def spd(self):
        assert np.allclose(self.A_np, self.A_np.T), "Matrix is not symmetric."
        assert np.all(np.linalg.eigvals(self.A_np) > 0), "Matrix is not positive definite."

    def condition_number(self):
        return np.linalg.cond(self.A_np)

    def eigenvalues(self):
        w, _ = np.linalg.eig(self.A_np)
        return w, np.min(w), np.max(w)

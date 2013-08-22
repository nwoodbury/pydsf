import pytest
import numpy as np

from control.matlab import ss

from pydsf.dsf import dsf


class TestDSFParams:
    """
    Test the parameter calls and types into :func:`pydsf.dsf.dsf`.
    """

    def test_accept_sys(self):
        """
        Tests if passing a StateSpace as ``sys`` raises no errors.
        """

        [A, B, C, D] = self.__build_standard_abcd()
        sys = ss(A, B, C, D)
        dsf(sys=sys)

    def test_sys_typecheck(self):
        """
        Tests if passing an invalid type as ``sys`` raises a TypeError.
        """

        with pytest.raises(TypeError):
            bad_sys = 12
            dsf(sys=bad_sys)

        with pytest.raises(TypeError):
            bad_sys = True
            dsf(sys=bad_sys)

    def test_accepts_abc(self):
        """
        Tests if accepts (A, B, C) nested lists.
        """

        A, B, C, D = self.__build_standard_abcd()
        dsf(A=A, B=B, C=C)

    def test_accepts_abcd(self):
        """
        Tests if accepts (A, B, C, D) nested lists.
        """

        A, B, C, D = self.__build_standard_abcd()
        dsf(A=A, B=B, C=C, D=D)

    def test_accepts_matrix_abc(self):
        """
        Tests if accepts (A, B, C) matrices.
        """

        A, B, C, D = self.__build_matrix_abcd()
        dsf(A=A, B=B, C=C)

    def test_accepts_matrix_abcd(self):
        """
        Tests if accepts (A, B, C, D) matrices.
        """

        A, B, C, D = self.__build_matrix_abcd()
        dsf(A=A, B=B, C=C, D=D)

    def test_require_a(self):
        """
        Tests if at least A is required.
        """
        A, B, C, D = self.__build_standard_abcd()

        with pytest.raises(ValueError):
            dsf(C=C)
        with pytest.raises(ValueError):
            dsf(B=B)
        with pytest.raises(ValueError):
            dsf(B=B, C=C)

    def __build_standard_abcd(self):
        A = [[1, 0], [0, 2]]
        B = [[1, 0], [0, 1]]
        C = [[1, 0], [0, 1]]
        D = [[1, 0], [0, 1]]

        return [A, B, C, D]

    def __build_matrix_abcd(self):
        A, B, C, D = self.__build_standard_abcd()

        return [
            np.matrix(A),
            np.matrix(B),
            np.matrix(C),
            np.matrix(D)
        ]

import copy

import numpy as np

from control.matlab import ss
from control.statesp import StateSpace


def dsf(sys=None, A=None, B=None, C=None, D=None):
    if sys is None:
        sys = __build_sys(A, B, C, D)
    elif not isinstance(sys, StateSpace):
        raise TypeError('sys must be a StateSpace')
    pass


def __build_sys(A, B, C, D):
    """
    If a :mod:`control.statesp.StateSpace` instance is not given, in dsf,
    this takes the A, B, and C (required) and D (optional) parameters
    and returns a ``StateSpace`` instance.
    """
    if (A is None) or (B is None) or (C is None):
        raise ValueError('Must either pass a StateSpace instance or (A, B, C)')

    if isinstance(A, list):
        A = np.matrix(A)

    if isinstance(B, list):
        B = np.matrix(B)

    if isinstance(C, list):
        C = np.matrix(C)

    print B

    if D is None:
        D = np.zeros_like(B)
    elif isinstance(D, list):
        D = np.matrix(D)

    print D

    return ss(A, B, C, D)

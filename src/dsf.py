import copy

import control as ctrl


def dsf(sys=None, A=None, B=None, C=None, D=None):
    if sys is None:
        sys = __build_sys(A, B, C, D)

    pass


def __build_sys(A, B, C, D):
    """
    If a :mod:`control.statesp.StateSpace` instance is not given, in dsf,
    this takes the A, B, and C (required) and D (optional) parameters
    and returns a ``StateSpace`` instance.
    """
    if A is None or B is None or C is None:
        raise Exception('Must either pass a sys or (A, B, C)')

    if D is None:
        D = copy.deepcopy(B).fill(0)

    return ctrl.ss(A, B, C, D)

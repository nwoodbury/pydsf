import copy

import numpy as np

from control.matlab import ss
from control.statesp import StateSpace
from control.lti import Lti


def dsf(**kwargs):
    return DynamicalStructureFunction(**kwargs)

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

    if D is None:
        D = np.zeros_like(B)
    elif isinstance(D, list):
        D = np.matrix(D)

    return ss(A, B, C, D)


class DynamicalStructureFunction(Lti):

    def __init__(self, **kwargs):

        print kwargs
        print kwargs.get('sys', 'not retrieved')

        sys = kwargs.get('sys', None)
        if sys is None:
            sys = self.__build_sys(**kwargs)
        if not isinstance(sys, StateSpace):
            raise TypeError('System sys must be a StateSpace instance')

    def __build_sys(self, **kwargs):
        if 'A' not in kwargs:
            raise ValueError('Must pass either a StateSpace instance or A')

        A = np.matrix(kwargs['A'])
        if A.shape[0] != A.shape[1]:
            # TODO Verify that A must be square, or if this can be relaxed
            raise ValueError('A must be square.')
        size = A.shape[0]

        B = np.matrix(kwargs.get('B', np.identity(size)))
        C = np.matrix(kwargs.get('C', np.identity(size)))
        D = np.matrix(kwargs.get('D', np.zeros((size, size))))

        #print 'A = ', A
        #print 'B = ', B
        #print 'C = ', C
        #print 'D = ', D

        return ss(A, B, C, D)

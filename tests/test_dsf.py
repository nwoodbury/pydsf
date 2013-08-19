import pytest
import pydsf.dsf as dsf


def test_no_param():
    caught = False
    try:
        dsf.dsf()
    except Exception:
        caught = True

    assert caught



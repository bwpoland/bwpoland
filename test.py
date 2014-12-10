__author__ = 'bwpoland'
import pytest

def f():
    return 3

def test_function():
    assert f() == 4



def test_function3():
    assert f() == 3

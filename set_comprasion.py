<<<<<<< HEAD
__author__ = 'bwpoland'
import pytest

def test_set_comparison():
    set1 = set("1308")
    set2 = set("8035")
=======
__author__ = 'bwpoland'
import pytest

def test_set_comparison_false():
    set1 = set("1308")
    set2 = set("8035")
    assert set1 == set2

def test_set_comparison_true():
    set1 = set("150")
    set2 = set("150")
>>>>>>> refs/remotes/origin/master
    assert set1 == set2
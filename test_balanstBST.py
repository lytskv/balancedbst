import numpy as np
import pytest

from balancedBST import BalancedBST


def median_test(bbst, median):
    assert bbst.median() == median


def add_element_and_test_median(bbst, element, new_median):
    bbst.add_element(element)
    median_test(bbst, new_median)


def test_add_element_to_empty():
    bbst = BalancedBST()
    bbst.add_element(13)


def test_add_element_to_existing():
    bbst = BalancedBST([1, 2, 3])
    bbst.add_element(13)


def test_create_with_single_element():
    bbst = BalancedBST([11])
    median_test(bbst, 11)


@pytest.fixture()
def elements_and_median_simple():
    return [1, 2, 3], 2


def test_create_with_elements_simple(elements_and_median_simple):
    elements, median = elements_and_median
    bbst = BalancedBST(elements)
    median_test(bbst, median)


@pytest.fixture()
def elements_and_median():
    elements = np.random.permutation(10)
    median = np.median(elements)
    return elements, median


def test_create_with_elements(elements_and_median):
    elements, median = elements_and_median
    bbst = BalancedBST(elements)
    median_test(bbst, median)

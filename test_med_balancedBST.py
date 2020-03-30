import numpy as np
import pytest

from medianBalancedBST import MedianBalancedBST


def median_test(bbst, median):
    assert bbst.median() == median


def add_element_and_test_median(bbst, element, new_median):
    bbst.add_element(element)
    median_test(bbst, new_median)


def test_add_element_to_empty():
    bbst = MedianBalancedBST()
    bbst.add_element(13)


def test_add_element_to_existing():
    bbst = MedianBalancedBST([1, 2, 3])
    bbst.add_element(13)


def test_create_with_single_element():
    bbst = MedianBalancedBST([11])
    median_test(bbst, 11)


@pytest.fixture()
def elements_and_median_simple():
    return [1, 2, 3], 2


def test_create_with_elements_simple(elements_and_median_simple):
    elements, median = elements_and_median_simple
    bbst = MedianBalancedBST(elements)
    median_test(bbst, median)


def test_pop_most_left_elements():
    np.random.seed(1337)
    elements = np.random.permutation(32)
    bbst = MedianBalancedBST(elements)
    assert bbst.pop_most_left() == min(elements)


def test_pop_most_right_elements():
    np.random.seed(1337)
    elements = np.random.permutation(32)
    bbst = MedianBalancedBST(elements)
    assert bbst.pop_most_right() == max(elements)


def test_get_most_right_elements():
    np.random.seed(1337)
    elements = np.random.permutation(32)
    bbst = MedianBalancedBST(elements)
    assert bbst.get_most_right() == max(elements)


@pytest.fixture(scope='module')
def elements_sets():
    np.random.seed(1337)
    return [
        np.random.permutation(10),
        np.random.permutation(100),
        np.random.permutation(1000)
    ]


def test_create_with_elements(elements_sets):
    for elements in elements_sets:
        bbst = MedianBalancedBST(elements)
        median_test(bbst, np.median(elements))


def test_create_and_add_elements(elements_sets):
    elements = elements_sets[0]
    bbst = MedianBalancedBST(elements)
    np.random.seed(1337)
    add_elements = np.random.permutation(11) + 10
    for element in add_elements:
        bbst.add_element(element)
    median_test(bbst, np.median(np.concatenate([elements, add_elements])))


@pytest.fixture(scope='module')
def elements_and_balance_factor():
    np.random.seed(1337)
    return [
        (np.random.permutation(10), 1),
        (np.random.permutation(11), 0)
    ]


def test_median_balancing(elements_and_balance_factor):
    for elements, balance_factor in elements_and_balance_factor:
        bbst = MedianBalancedBST(elements)
        assert bbst._balance_factor == balance_factor

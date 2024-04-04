import pytest


@pytest.fixture
def sort_input1():
    return [5, 1, 4, 2, 8, 9, 3, 7, 6, 0]


@pytest.fixture
def sort_input2():
    return [
        5,
        1,
        4,
        2,
        8,
        9,
        3,
        7,
        6,
        0,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        0,
        -3,
        -6,
        4,
        1,
        9,
        6,
        10,
    ]
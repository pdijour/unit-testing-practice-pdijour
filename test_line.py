# test_line.py

import pytest

@pytest.mark.parametrize("point1, point2, expected",[
                         ((1, 1), (2, 2), 1),
                         ((-1, 3), (1, 4), 0.5)])

def test_find_m(point1, point2, expected):
    from line import find_m
    # point1 = (1,1)
    # point2 = (2,2)
    # expected = 1
    answer = find_m(point1, point2)
    assert expected == answer

@pytest.mark.parametrize("point1, m, expected",[
                         ((1, 1), 1, 0),
                         ((-1, 3), 0.5,  3.5)])

def test_find_b(point1, m, expected):
    from line import find_b
    # point1 = (1,1)
    # m = 1
    # expected = 0
    answer = find_b(point1, m)
    assert expected == answer

@pytest.mark.parametrize("m, x, b, expected",[
                         (1, 3, 0, 3),
                         (0.5, 3, 3.5, 5)])

def test_find_y(m, x, b, expected):
    from line import find_y
    # m = 1
    # x = 3
    # b = 0
    # expected = 3
    answer = find_y(m, x, b)
    assert expected == answer

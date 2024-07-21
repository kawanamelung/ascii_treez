from treez.make_trees import AsciiCanvas
import pytest
import numpy as np


def test_blank():

    # assert AsciiCanvas(10, 10).shape == (10, 10)
    c = AsciiCanvas(10, 1)
    assert AsciiCanvas(10, 1).shape == (1, 10)

def test_add_element():
    element = AsciiCanvas(2, 2)
    element.fill('x')
    canvas = AsciiCanvas(3, 3)
    canvas.add_element(element)

    expected = np.array([ ['x', 'x', ' '], ['x', 'x', ' '], [' ', ' ', ' '] ])

    np.testing.assert_array_equal(canvas, expected)

    element = AsciiCanvas(3, 3)
    element.fill('x')
    canvas = AsciiCanvas(2, 2)
    canvas.add_element(element)

    expected = np.array([ ['x', 'x'], ['x', 'x'] ])

    np.testing.assert_array_equal(canvas, expected)
def test_add_identical_element():
    element = AsciiCanvas(2, 3)
    element.fill('x')
    canvas = AsciiCanvas(2, 3)
    canvas.add_element(element)

    expected = np.array([ ['x', 'x'], ['x', 'x'], ['x', 'x'] ])

    np.testing.assert_array_equal(canvas, expected)

    element = AsciiCanvas(1, 3)
    element.fill('x')
    canvas = AsciiCanvas(1, 3)
    canvas.add_element(element)

    expected = np.array([ ['x'], ['x'], ['x'] ])

    np.testing.assert_array_equal(canvas, expected)

def test_add_element_offset():
    element = AsciiCanvas(2, 2)
    element.fill('x')
    canvas = AsciiCanvas(3, 3)
    canvas.add_element(element, (1, 0))

    expected = np.array([ [' ', 'x', 'x'], [' ', 'x', 'x'], [' ', ' ', ' '] ])
    np.testing.assert_array_equal(canvas, expected)

    element = AsciiCanvas(2, 2)
    element.fill('x')
    canvas = AsciiCanvas(3, 4)
    canvas.add_element(element, (1, 1))

    expected = np.array([ [' ', ' ', ' '], [' ', 'x', 'x'], [' ', 'x', 'x'], [' ', ' ', ' '] ])
    np.testing.assert_array_equal(canvas, expected)
    element = AsciiCanvas(1, 3)
    element.fill('x')
    canvas = AsciiCanvas(1, 3)
    canvas.add_element(element, (0, 1))

    expected = np.array([
        [' '],
        ['x'],
        ['x']
    ])

    np.testing.assert_array_equal(canvas, expected)


def test_add_element_sliced():
    element = AsciiCanvas(2, 2)
    element.fill('x')
    canvas = AsciiCanvas(3, 3)
    canvas.add_element(element)

    expected = np.array([ ['x', 'x', ' '], ['x', 'x', ' '], [' ', ' ', ' '] ])

    np.testing.assert_array_equal(canvas, expected)

    element = AsciiCanvas(3, 3)
    element.fill('x')
    canvas = AsciiCanvas(3, 3)
    canvas.add_element(element)

    expected = np.array([ ['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x'] ])

    np.testing.assert_array_equal(canvas, expected)

    element = AsciiCanvas(1, 3)
    element.fill('x')
    canvas = AsciiCanvas(1, 3)
    canvas.add_element(element)

    expected = np.array([ ['x'], ['x'], ['x'] ])

    np.testing.assert_array_equal(canvas, expected)

def test_add_element_sliced_offset():
    element = AsciiCanvas(2, 4)
    element.fill('x')
    canvas = AsciiCanvas(2, 4)
    canvas.add_element(element, (1, 0))
    expected = np.array([ [' ', 'x'], [' ', 'x'], [' ', 'x'], [' ', 'x'] ])

    np.testing.assert_array_equal(canvas, expected)

    element = AsciiCanvas(2, 4)
    element.fill('x')
    canvas = AsciiCanvas(3, 6)
    canvas.add_element(element, (0, 2))
    expected = np.array([ [' ', ' ', ' '], [' ', ' ', ' '], ['x', 'x', ' '], ['x', 'x', ' '], ['x', 'x', ' '], ['x', 'x', ' '] ])

    np.testing.assert_array_equal(canvas, expected)


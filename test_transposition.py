import unittest
from matrix_calc import MatrixCalc
from matrix_exceptions import MatrixDoNotMatchException


class TestMatrixTransposition(unittest.TestCase):
    def test_one_by_one(self):
        matrix = [[1]]
        expected_result = [[1]]
        self.assertEqual(expected_result, MatrixCalc.transposition(matrix))

    def test_two_by_five(self):
        matrix = [
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5]
        ]
        expected_result = [
            [1, 1],
            [2, 2],
            [3, 3],
            [4, 4],
            [5, 5]
        ]
        self.assertEqual(expected_result, MatrixCalc.transposition(matrix))

    def test_three_by_three(self):
        matrix = [
            [1, 2, 3],
            [2, 1, 2],
            [3, 3, 4],
        ]
        expected_result = [
            [1, 2, 3],
            [2, 1, 3],
            [3, 2, 4],
        ]
        self.assertEqual(expected_result, MatrixCalc.transposition(matrix))

    def test_incorrect_size(self):
        matrix = [
            [1, 2, 3],
            [1, 2],
            [1, 2, 3, 4]
        ]
        with self.assertRaises(MatrixDoNotMatchException):
            MatrixCalc.transposition(matrix)

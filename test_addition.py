import unittest
from matrix_calc import MatrixCalc
from matrix_exceptions import MatrixDoNotMatchException


class TestMatrixAddition(unittest.TestCase):
    def test_two_by_two(self):
        matrix1 = [
            [1, 2],
            [3, 4],
        ]
        matrix2 = [
            [4, 3],
            [2, 1],
        ]
        expected_result = [
            [5, 5],
            [5, 5]
        ]
        self.assertEqual(expected_result, MatrixCalc.addition(matrix1, matrix2))

    def test_three_by_three(self):
        matrix1 = [
            [1, 2, 3],
            [2, 1, 2],
            [3, 3, 4],
        ]
        matrix2 = [
            [1, 2, 3],
            [2, 1, 2],
            [3, 3, 4],
        ]
        expected_result = [
            [2, 4, 6],
            [4, 2, 4],
            [6, 6, 8],
        ]
        self.assertEqual(expected_result, MatrixCalc.addition(matrix1, matrix2))

    def test_different_sizes(self):
        matrix1 = [
            [1, 2, 3],
            [2, 1, 2],
            [3, 3, 4],
        ]
        matrix2 = [
            [4, 3],
            [2, 1],
        ]
        with self.assertRaises(MatrixDoNotMatchException):
            MatrixCalc.addition(matrix1, matrix2)

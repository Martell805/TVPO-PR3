import unittest

from matrix_calc import MatrixCalc
from matrix_exceptions import MatrixDoNotMatchException


class TestMatrixDeterminant(unittest.TestCase):
    def test_two_by_two(self):
        matrix = [
            [1, 2],
            [3, 4],
        ]
        self.assertEqual(-2, MatrixCalc.determinant(matrix))

    def test_three_by_three(self):
        matrix = [
            [1, 2, 3],
            [2, 1, 2],
            [3, 3, 4],
        ]
        self.assertEqual(3, MatrixCalc.determinant(matrix))

    def test_non_square(self):
        matrix = [
            [1, 2, 3],
            [2, 1, 2],
        ]

        with self.assertRaises(MatrixDoNotMatchException):
            MatrixCalc.determinant(matrix)

from matrix_exceptions import MatrixDoNotMatchException


class MatrixCalc:
    @staticmethod
    def multiply(matrix1, matrix2):
        ...

    @staticmethod
    def __get_sub_matrix(i, j, matrix):
        return [
            [
                matrix[q][w] for w in range(len(matrix)) if w != j
            ] for q in range(len(matrix)) if q != i
        ]

    @staticmethod
    def determinant(matrix):
        rows, cols = len(matrix), len(matrix[0])
        if cols != rows:
            raise MatrixDoNotMatchException()

        if rows == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        result = 0

        for j, element in enumerate(matrix[0]):
            multiplier = 1 if j % 2 == 0 else -1
            result += multiplier * element * MatrixCalc.determinant(MatrixCalc.__get_sub_matrix(0, j, matrix))

        return result

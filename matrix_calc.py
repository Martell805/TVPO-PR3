from matrix_exceptions import MatrixDoNotMatchException


class MatrixCalc:
    @staticmethod
    def multiply(matrix1, matrix2):
        rows1, cols1 = len(matrix1), len(matrix1[0])
        rows2, cols2 = len(matrix2), len(matrix2[0])

        if cols1 != rows2:
            raise MatrixDoNotMatchException()

        result = [[0] * cols2 for _ in range(rows1)]

        for i in range(rows1):
            for j in range(cols2):
                for k in range(cols1):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]

        return result

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

    @staticmethod
    def addition(matrix1, matrix2):
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise MatrixDoNotMatchException()

        result = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix1[0])):
                row.append(matrix1[i][j] + matrix2[i][j])
            result.append(row)

        return result

    @staticmethod
    def number_multiplication(matrix, number):
        result = []
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix[0])):
                row.append(matrix[i][j] * number)
            result.append(row)
        return result
Feature: Multiply the matrix by a number
  Scenario: Multiply the matrix by a positive number
    Given [[1, 2, 3],[4, 5, 6],[7, 8, 0],] with 2
    Then multiply matrix and number
    Then result of multiplication is equal to [[2, 4, 6],[8, 10, 12],[14, 16, 0],]

  Scenario: Multiply the matrix by a negative number
    Given [[1, -2, 3],[4, -5, 6],[7, -8, 0],] with -2
    Then multiply matrix and number
    Then result of multiplication is equal to [[-2, 4, -6],[-8, 10, -12],[-14, 16, 0],]

  Scenario: Multiply the matrix by zero
    Given [[1, -2, 3],[4, -5, 6],[7, -8, 0],] with 0
    Then multiply matrix and number
    Then result of multiplication is equal to [[0, 0, 0],[0, 0, 0],[0, 0, 0],]
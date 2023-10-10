Feature: Multiply the matrix by a number
  Scenario: Multiply the matrix by a positive number
    Given [[1, 2, 3],[4, 5, 6],[7, 8, 0],] and 2
    Then multiply them
    Then result matrix is equal to [[2, 4, 6],[8, 10, 12],[14, 16, 0],]

  Scenario: Multiply the matrix by a negative number
    Given [[1, -2, 3],[4, -5, 6],[7, -8, 0],] and -2
    Then multiply them
    Then result matrix is equal to [[-2, 4, -6],[-8, 10, -12],[-14, 16, 0],]

  Scenario: Multiply the matrix by a real number
    Given [[1, -2, 3],[4, -5, 6],[7, -8, 0],] and 0.2
    Then multiply them
    Then result matrix is equal to [[0.2, -0.4, 0.6],[0.8, -1, 1.2],[1.4, -1.6, 0],]

  Scenario: Multiply the matrix by zero
    Given [[1, -2, 3],[4, -5, 6],[7, -8, 0],] and 0
    Then multiply them
    Then result matrix is equal to [[0, 0, 0],[0, 0, 0],[0, 0, 0],]
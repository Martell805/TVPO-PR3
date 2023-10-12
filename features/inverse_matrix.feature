Feature: Calculating the inverse matrix
  Scenario: Normal square matrix two by two
    Given square [[2, -5],[1, -3]]
    Then calculating the inverse matrix
    Then result of calculating is equal to [[3, -5],[1, 2]]

  Scenario: Normal square matrix three by three
    Given square [[2, 5, 7], [6, 3, 4], [5, -2, -3]]
    Then calculating the inverse matrix
    Then result of calculating is equal to [[1, -1, -1], [-38, -41, -34], [27, -29, -24]]

  Scenario: Non-square matrix
    Given square [[1, -2, 3],[4, -5, 6],[7, -8, 0], [7, -8, 0]]
    Then calculating the inverse matrix
    Then exception MatrixDoNotMatchException is thrown

  Scenario: A matrix with a zero determinant
    Given square [[6, 1, 12],[-3, -5, -6],[1, 4, 2]]
    Then calculating the inverse matrix
    Then exception MatrixDoNotMatchException is thrown
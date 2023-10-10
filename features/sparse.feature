Feature: Multiply matrices
  Scenario: Sparse three by three matrices
    Given [[1, 0, 0],[0, 2, 0],[0, 0, 3],] and [[1, 0, 0],[0, 1, 0],[0, 0, 1],]
    Then multiply them
    Then result matrix is equal to [[1, 0, 0],[0, 2, 0],[0, 0, 3],]

  Scenario: Normal three by three matrices
    Given [[1, 2, 0],[0, 2, 5],[0, 4, 3],] and [[1, 7, 0],[0, 2, 0],[6, 0, 1],]
    Then multiply them
    Then result matrix is equal to [[1, 11, 0],[30, 4, 5],[18, 8, 3],]

  Scenario: Normal two by four and four by two matrices
    Given [[1, 2, 0, 0],[0, 2, 5, 0],] and [[1, 7],[0, 2],[6, 0],[0, 0],]
    Then multiply them
    Then result matrix is equal to [[1, 11],[30, 4],]

  Scenario: Unsuitable matrices
    Given [[1, 2, 0, 0],[0, 2, 5, 0],] and [[1, 7],[0, 2],[6, 0],]
    Then multiply them
    Then exception MatrixDoNotMatchException is thrown

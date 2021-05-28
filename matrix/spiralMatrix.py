'''
Given an m x n matrix, return all elements of the matrix in spiral order.
'''


def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    result = []
    if (not matrix or len(matrix) == 0):
        return result
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    matrixSize = len(matrix) * len(matrix[0])

    while (len(result) != matrixSize):
        for i in range(left, right + 1):
            if (len(result) != matrixSize):
                result.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            if (len(result) != matrixSize):
                result.append(matrix[i][right])
        right -= 1

        for i in range(right, left - 1, -1):
            if (len(result) != matrixSize):
                result.append(matrix[bottom][i])
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            if (len(result) != matrixSize):
                result.append(matrix[i][left])
        left += 1

    return result


def main():
    assert (spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5])
    assert (spiralOrder([[1, 2, 3, 4],
                         [5, 6, 7, 8],
                         [9, 10, 11, 12],
                         [13, 14, 15, 16]])
            == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10])
    assert (spiralOrder([[1, 2], [3, 4]]) == [1, 2, 4, 3])
    assert (spiralOrder([]) == [])


main()

'''
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.
'''


def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    isCol = False

    for x in range(rows):
        if (matrix[x][0] == 0):
            isCol = True
        for y in range(1, cols):
            if (matrix[x][y] == 0):
                matrix[x][0] = 0
                matrix[0][y] = 0

    for x in range(1, rows):
        for y in range(1, cols):
            if (matrix[x][0] == 0 or matrix[0][y] == 0):
                matrix[x][y] = 0

    if matrix[0][0] == 0:
        for y in range(cols):
            matrix[0][y] = 0

    if isCol:
        for x in range(rows):
            matrix[x][0] = 0


def main():
    matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    setZeroes(matrix1)
    assert (matrix1 == [[1, 0, 1], [0, 0, 0], [1, 0, 1]])

    matrix2 = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
    setZeroes(matrix2)
    assert (matrix2 == [[0, 0, 3, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

    matrix3 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    setZeroes(matrix3)
    assert (matrix3 == [[1, 1, 1], [2, 2, 2], [3, 3, 3]])

    matrix4 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    setZeroes(matrix4)
    assert (matrix4 == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])


main()

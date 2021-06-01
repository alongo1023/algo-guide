'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
'''


def rotateMatrix(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)

    # transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reflect
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]


def main():
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotateMatrix(matrix1)
    assert (matrix1 == [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    rotateMatrix(matrix2)
    assert (matrix2 == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])

    matrix3 = [[1]]
    rotateMatrix(matrix3)
    assert (matrix3 == [[1]])


main()

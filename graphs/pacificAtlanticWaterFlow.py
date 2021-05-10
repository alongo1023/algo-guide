'''
You are given an m x n integer matrix heights representing the height of each unit cell in a continent.
The Pacific ocean touches the continent's left and top edges, and the Atlantic ocean touches the continent's
right and bottom edges.

Water can only flow in four directions: up, down, left, and right.
Water flows from a cell to an adjacent one with an equal or lower height.

Return a list of grid coordinates where water can flow to both the Pacific and Atlantic oceans.
'''

def pacificAtlantic(heights):
    """
    :type heights: List[List[int]]
    :rtype: List[List[int]]
    """

    def dfs(heights, row, col, prev, ocean):
        if (row < 0 or col < 0 or col > len(heights[0]) - 1 or row > len(heights) - 1):
            return
        if (ocean[row][col]):
            return
        if (heights[row][col] < prev):
            return
        ocean[row][col] = True
        curr = heights[row][col]
        dfs(heights, row - 1, col, curr, ocean)
        dfs(heights, row + 1, col, curr, ocean)
        dfs(heights, row, col - 1, curr, ocean)
        dfs(heights, row, col + 1, curr, ocean)

    result = []

    rows = len(heights)
    cols = len(heights[0])
    pacific = [[False for y in range(cols)] for x in range(rows)]
    atlantic = [[False for y in range(cols)] for x in range(rows)]

    # initialize edges
    for x in range(rows):
        dfs(heights, x, 0, 0, pacific)
        dfs(heights, x, cols - 1, 0, atlantic)

    for y in range(cols):
        dfs(heights, 0, y, 0, pacific)
        dfs(heights, rows - 1, y, 0, atlantic)

    # find result
    for x in range(rows):
        for y in range(cols):
            if (pacific[x][y] and atlantic[x][y]):
                result.append([x, y])

    return result


def main():
    heights1 = [[1, 2, 3, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    expected1 = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    assert (pacificAtlantic(heights1) == expected1)

    heights2 = [[2, 1], [1, 2]]
    expected2 = [[0, 0], [0, 1], [1, 0], [1, 1]]
    assert (pacificAtlantic(heights2) == expected2)


main()

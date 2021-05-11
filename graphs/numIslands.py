'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
'''
def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if (not grid or len(grid) == 0):
        return 0

    def dfs(grid, row, col):
        if (row < 0 or col < 0 or row > len(grid) - 1 or col > len(grid[0]) - 1 or grid[row][col] == "0"):
            return 0

        grid[row][col] = "0"
        dfs(grid, row + 1, col)
        dfs(grid, row - 1, col)
        dfs(grid, row, col - 1)
        dfs(grid, row, col + 1)
        return 1

    rows = len(grid)
    cols = len(grid[0])
    result = 0
    for row in range(rows):
        for col in range(cols):
            if (grid[row][col] == "1"):
                result = result + dfs(grid, row, col)

    return result


def main():
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    grid3 = [["0", "0"], ["0", "0"]]

    grid4 = []

    assert (numIslands(grid1) == 1)
    assert (numIslands(grid2) == 3)
    assert (numIslands(grid3) == 0)
    assert (numIslands(grid4) == 0)


main()

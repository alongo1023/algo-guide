'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally
or vertically neighboring. The same letter cell may not be used more than once.
'''


def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    m = len(board[0])
    n = len(board)
    for i in range(n):
        for j in range(m):
            if (board[i][j] == word[0] and search(i, j, board, word, 0)):
                return True
    return False


def search(i, j, board, word, count):
    if (len(word) == count):
        return True
    if (i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[count] != board[i][j]):
        return False

    temp = board[i][j]
    board[i][j] = ""
    found = (search(i + 1, j, board, word, count + 1) or
             search(i - 1, j, board, word, count + 1) or
             search(i, j + 1, board, word, count + 1) or
             search(i, j - 1, board, word, count + 1))
    board[i][j] = temp
    return found

def main():
    board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word1 = "ABCCED"
    assert(exist(board1, word1))

    board2 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word2 = "ABCB"
    assert(not exist(board2, word2))

    board3 = [["a"]]
    word3 = "a"
    assert(exist(board3, word3))

main()
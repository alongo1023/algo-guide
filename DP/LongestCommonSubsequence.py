def longestCommonSubsequence(str1, str2):
    '''
    :param str1: string
    :param str2: string
    :return:  longest common subsequence between str1 and str2
    example: str1 = ABCDEF str2 = "BDEF" -> return 4
    '''
    len1 = len(str1) + 1
    len2 = len(str2) + 1
    grid = [[0 for x in range(len1)] for y in range(len2)]
    for x in range(1, len2):
        for y in range(1, len1):
            if(str1[y-1] == str2[x-1]):
                grid[x][y] = 1 + grid[x-1][y-1]
            else:
                grid[x][y] = max(grid[x-1][y], grid[x][y-1])

    return grid[len2-1][len1-1]

def main():
    assert(longestCommonSubsequence("ABCDEF", "ACEF") == 4)
    assert(longestCommonSubsequence("bsbinim", "jmjkbkjkv") == 1)
    assert(longestCommonSubsequence("LMNOPPQRSZN", "MPQ") == 3)



main()
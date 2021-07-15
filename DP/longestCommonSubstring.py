def LCS(str1, str2):
    m = len(str1)
    n = len(str2)
    lookup = [[0 for i in range(n+1)] for j in range(m+1)]
    max = 0
    end = m
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1]==str2[j-1]:
                lookup[i][j] = lookup[i-1][j-1] + 1
                if(lookup[i][j] > max):
                    max = lookup[i][j]
                    end = i
    return str1[end-max:end]

def main():
    assert(LCS("ABCD", "BCD") == "BCD")
    assert(LCS("XYZABCBAB", "MNOPZABCVV") == "ZABC")
    assert(LCS("AB", "B") == "B")

main()

'''
You are given a string s and an integer k. You can choose any character of the string and change it to any
other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the
above operations.
'''


def characterReplacement(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    i = 0
    n = len(s)
    if n <= 1:
        return n
    letterCount = {}
    letterCount[s[i]] = 1
    maxLength = 0
    for j in range(1, n):
        if (s[j] in letterCount):
            letterCount[s[j]] += 1
        else:
            letterCount[s[j]] = 1

        currLength = j - i + 1
        while (i < j and currLength - max(letterCount.values()) > k):
            letterCount[s[i]] -= 1
            i += 1
            currLength -= 1

        maxLength = max(maxLength, currLength)
    return maxLength

def main():
    assert(characterReplacement("ABAB", 2) == 4)
    assert(characterReplacement("AABABBA", 1) == 4)
    assert(characterReplacement("ABAA", 0) == 2)
    assert(characterReplacement("", 0) == 0)
main()
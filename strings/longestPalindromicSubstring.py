def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if not s or len(s) < 1: return ""
    start, end = 0, 0
    for i in range(len(s)):
        len1 = expandFromMiddle(s, i, i)
        len2 = expandFromMiddle(s, i, i + 1)
        length = max(len1, len2)
        if (length > end - start):
            start = i - (length - 1) // 2
            end = i + (length) // 2
    return s[start:end + 1]


def expandFromMiddle(s, left, right):
    if not s or left > right: return 0
    while (left >= 0 and right < len(s) and s[left] == s[right]):
        left -= 1
        right += 1
    return right - left - 1

def main():
    assert(longestPalindrome("babad") == "aba")
    assert(longestPalindrome("cbbd") == "bb")
    assert(longestPalindrome("a") == "a")
    assert(longestPalindrome("ab") == "b")
    assert(longestPalindrome("") == "")


main()
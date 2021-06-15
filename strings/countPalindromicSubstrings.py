'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
'''
def countSubstrings(s):
    """
    :type s: str
    :rtype: int
    """
    result = []
    for i in range(len(s)):
        expandFromMiddle(i, i, s, result)
        expandFromMiddle(i, i + 1, s, result)
    return len(result)


def expandFromMiddle(left, right, s, result):
    while (left >= 0 and right < len(s) and left <= right and s[left] == s[right]):
        result.append(s[left:right + 1])
        left -= 1
        right += 1


def main():
    assert (countSubstrings("abc") == 3)
    assert (countSubstrings("aaa") == 6)
    assert (countSubstrings("") == 0)
    assert (countSubstrings("racecar") == 10)


main()

'''Given two strings s and t of lengths m and n respectively,
return the minimum window substring of s such that every character
in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.'''
from collections import Counter


def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if not t or not s:
        return ""
    tMap = Counter(t)
    requiredLen = len(tMap)
    l, r = 0, 0
    formed = 0
    windowCounts = {}

    res = float("inf"), None, None

    while r < len(s):
        character = s[r]
        windowCounts[character] = windowCounts.get(character, 0) + 1
        if (character in tMap and windowCounts[character] == tMap[character]):
            formed += 1

        while (l <= r and formed == requiredLen):
            character = s[l]
            if (r - l + 1 < res[0]):
                res = (r - l + 1, l, r)
            windowCounts[character] -= 1
            if (character in tMap and windowCounts[character] < tMap[character]):
                formed -= 1
            l += 1
        r += 1
    return "" if res[0] == float("inf") else s[res[1]:res[2] + 1]


def main():
    assert (minWindow("ADOBECODEBANC", "ABC") == "BANC")
    assert (minWindow("a", "a") == "a")
    assert (minWindow("a", "aa") == "")
    assert (minWindow("", "") == "")


main()

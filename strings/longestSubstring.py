'''Given a string s, find the length of the longest substring without repeating characters.'''


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    i, j = 0, 1
    seen = set()
    maxLength = 0
    n = len(s)
    if (n <= 1):
        return n
    seen.add(s[i])
    while (j < n):
        if (s[j] not in seen):
            seen.add(s[j])
            j += 1
            maxLength = max(maxLength, len(seen))
        else:
            seen.remove(s[i])
            i += 1

    return maxLength


def main():
    assert (lengthOfLongestSubstring("pwwkew") == 3)
    assert (lengthOfLongestSubstring("abcabcbb") == 3)
    assert (lengthOfLongestSubstring(" ") == 1)
    assert (lengthOfLongestSubstring("") == 0)
    assert (lengthOfLongestSubstring("bbbbb") == 1)


main()

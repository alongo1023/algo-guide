'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.'''
from collections import Counter
def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    sMap = Counter(s)
    tMap = Counter(t)
    if (len(t) != len(s)):
        return False
    for i in t:
        if (tMap[i] != sMap[i]):
            return False

    return True

def main():
    assert(not isAnagram("cat", "car"))
    assert(isAnagram("anagram","nagaram"))
    assert(not isAnagram("ab", "a"))
    assert(isAnagram("", ""))

main()
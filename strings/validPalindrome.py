'''Given a string s, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.'''
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    start, end = 0, len(s) - 1
    s = s.lower()
    while (start < end):
        if not s[start].isalpha() and not s[start].isnumeric():
            start += 1
        elif not s[end].isalpha() and not s[end].isnumeric():
            end -= 1
        elif s[start] == s[end]:
            start += 1
            end -= 1
        else:
            return False

    return True

def main():
    assert(isPalindrome("A man, a plan, a canal: Panama"))
    assert(not isPalindrome("0p"))
    assert(not isPalindrome("race a car"))

main()
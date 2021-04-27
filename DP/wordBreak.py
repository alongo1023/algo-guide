def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool returns true if string, s, can be broken into the words in wordDict
    """
    table = [False] * (len(s))
    for j in range(len(s)):
        for i in range(j, -1, -1):
            currWord = s[i:j + 1]
            isLeftBreakable = table[i - 1] if i > 0 else True
            if currWord in wordDict and isLeftBreakable:
                table[j] = True
                break

    return table[len(s) - 1]

def main():
    assert(wordBreak("applepineapple", ["pine", "apple"]))
    assert(wordBreak("catDogRabbit", ["cat", "Dog", "Rabbit"]))
    assert(not wordBreak("sunraysun", ["suns", "ray"]))
    assert(not wordBreak("sandCastle", ["and", "Castle"]))


main()
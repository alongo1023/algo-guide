from trees.Trie import TrieNode
'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that
matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
'''

class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        children = self.root.charMap
        for i in range(len(word)):
            ch = word[i]
            t = None
            if ch in children:
                t = children[ch]
            else:
                t = TrieNode()
                children[ch] = t
            children = t.charMap
            if i == len(word) - 1:
                t.isEnd = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.dfsSearch(self.root.charMap, word, 0)

    def dfsSearch(self, children, word, start):
        if start == len(word):
            if len(children) == 0:
                return True
            else:
                return False
        ch = word[start]
        if ch in children:
            if start == len(word) - 1 and children[ch].isEnd:
                return True
            return self.dfsSearch(children[ch].charMap, word, start + 1)
        elif ch == ".":
            result = False
            for key in children.keys():
                if start == len(word) - 1 and children[key].isEnd:
                    return True
                if (self.dfsSearch(children[key].charMap, word, start + 1)):
                    result = True
            return result
        else:
            return False

def main():
    wordDict = WordDictionary()
    wordDict.addWord("a")
    wordDict.addWord("a")
    assert(wordDict.search("."))
    assert(wordDict.search("a"))
    assert(not wordDict.search(".a"))
    assert(not wordDict.search("aa"))
    assert(not wordDict.search("a."))

    wordDict2 = WordDictionary()
    wordDict2.addWord("bad")
    wordDict2.addWord("mad")
    wordDict2.addWord("dad")
    assert(not wordDict2.search("pad"))
    assert(wordDict2.search("bad"))
    assert(wordDict2.search(".ad"))
    assert(wordDict2.search("b.."))

main()
'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and
retrieve keys in a dataset of strings. There are various applications of this data structure, such as
autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
1. void insert(String word) Inserts the string word into the trie.
2. boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before),
and false otherwise.
3. boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has
the prefix prefix, and false otherwise.
'''

class TrieNode(object):
    def __init__(self):
        self.charMap = {}
        self.isEnd = False


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        curr = self.root
        for ch in word:
            if not ch in curr.charMap:
                curr.charMap[ch] = TrieNode()
            curr = curr.charMap[ch]
        curr.isEnd = True

    def searchPrefix(self, word):
        curr = self.root
        for ch in word:
            if ch in curr.charMap:
                curr = curr.charMap[ch]
            else:
                return None
        return curr

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        lastNode = self.searchPrefix(word)
        return lastNode and lastNode.isEnd

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        lastNode = self.searchPrefix(prefix)
        return lastNode

def main():
    trie = Trie()
    trie.insert("apple")
    assert(trie.search("apple"))
    assert(trie.startsWith("app"))
    assert(not trie.search("app"))
    trie.insert("app")
    assert(trie.search("app"))

main()
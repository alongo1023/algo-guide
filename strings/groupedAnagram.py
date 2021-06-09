'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
'''
def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    if(len(strs) == 0) :
        return [[""]]
    anagramMap = {}
    for curr in strs:
        sortedCurr = ''.join(sorted(curr))
        if sortedCurr not in anagramMap:
            anagramMap[sortedCurr] = []
        anagramMap.get(sortedCurr).append(curr)
    return anagramMap.values()

def main():
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(groupAnagrams([]))
    print(groupAnagrams(["a"]))

main()
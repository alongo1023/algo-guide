'''
Given an integer array nums and an integer k,
return the k most frequent elements. You may return the answer in any order.
'''
import heapq
from collections import Counter


def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    freqMap = Counter(nums)
    return heapq.nlargest(k, freqMap.keys(), key=freqMap.get)


def main():
    assert(topKFrequent([1,1,1,1,3,3,2,2,2], 2) == [1, 2])
    assert(topKFrequent([1], 1) == [1])
    assert(topKFrequent([4, 4, 1, 5, 6], 4) == [4, 1, 5, 6])
    assert(topKFrequent([10, 9, 2, 3, 7,7, 8, 3, 4, 7], 1) == [7])
main()
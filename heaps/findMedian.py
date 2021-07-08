import heapq
"""
The median is the middle value in an ordered integer list. If the size of the list is even, 
there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the 
actual answer will be accepted.
"""

class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.small, -1 * num)
        if (self.small and self.large and (-1 * self.small[0] > self.large[0])):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, val)

    def findMedian(self):
        """
        :rtype: float
        """
        if (len(self.small) > len(self.large)):
            return -1 * self.small[0]
        if (len(self.large) > len(self.small)):
            return self.large[0]
        sumVal = (-1 * self.small[0] + self.large[0])
        return sumVal / 2

def main():
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    assert(medianFinder.findMedian() == 1.5)
    medianFinder.addNum(3)
    assert(medianFinder.findMedian() == 2)

    medianFinder2 = MedianFinder()
    medianFinder2.addNum(1)
    assert(medianFinder2.findMedian() == 1)

    medianFinder3 = MedianFinder()
    medianFinder3.addNum(100)
    medianFinder3.addNum(-2)
    assert(medianFinder3.findMedian() == 49)
    medianFinder3.addNum(-10)
    assert(medianFinder3.findMedian() == -2)

main()
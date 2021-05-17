'''
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you
need to remove to make the rest of the intervals non-overlapping.
'''


def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    intervals.sort(key=lambda x: x[0] and x[1])
    currInterval = intervals[0]
    numRemoved = 0

    for interval in intervals[1:]:
        if (interval[0] < currInterval[1]):
            numRemoved += 1
        else:
            currInterval = interval

    return numRemoved


def main():
    assert (eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1)
    assert (eraseOverlapIntervals([[1, 2], [0, 4], [1, 3], [5, 10], [3, 4]]) == 3)
    assert (eraseOverlapIntervals([[1, 2]]) == 0)
    assert (eraseOverlapIntervals([[1, 2], [2, 10]]) == 0)


main()

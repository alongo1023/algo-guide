'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''


def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """

    if (len(intervals) <= 1):
        return intervals

    intervals = sorted(intervals, key=lambda interval: interval[0])
    result = []
    currInterval = intervals[0]
    result.append(currInterval)

    for interval in intervals:
        if (interval[0] <= currInterval[1]):
            currInterval[1] = max(currInterval[1], interval[1])
        else:
            currInterval = interval
            result.append(currInterval)

    return result


def main():
    assert (merge([[1, 4], [0, 4]]) == [[0, 4]])
    assert (merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]])
    assert (merge([[5, 3], [2, 6], [0, 8]]) == [[0, 8]])
    assert (merge([[0, 2]]) == [[0, 2]])


main()

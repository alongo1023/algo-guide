'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.
'''


def insert(intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    result = []
    inserted = False

    for interval in intervals:
        if (inserted):
            result.append(interval)
        elif (newInterval[0] > interval[1]):
            result.append(interval)
        elif (newInterval[1] < interval[0]):
            inserted = True
            result.append(newInterval)
            result.append(interval)
        else:
            newInterval[0] = min(newInterval[0], interval[0])
            newInterval[1] = max(newInterval[1], interval[1])

    if (not inserted):
        result.append(newInterval)
    return result


def main():
    assert (insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]])
    assert (insert([], [5, 7]) == [[5, 7]])
    assert (insert([[1, 5]], [2, 3]) == [[1, 5]])
    assert (insert([[1, 5]], [2, 7]) == [[1, 7]])
    assert (insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]])


main()

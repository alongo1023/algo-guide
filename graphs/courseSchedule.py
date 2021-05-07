'''There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must
take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.'''


def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    preMap = {i: [] for i in range(numCourses)}
    visited = []
    for pre in prerequisites:
        preMap[pre[0]].append(pre[1])

    def dfs(course):
        if (course in visited):
            return False

        visited.append(course)
        for pre in preMap[course]:
            if not dfs(pre):
                return False

        visited.remove(course)
        preMap[course] = []
        return True

    for course in range(numCourses):
        if not dfs(course):
            return False

    return True

def main():
    assert(not canFinish(2, [[0, 1], [1, 0]]))
    assert(canFinish(2, [[1, 0]]))
    assert(canFinish(5, [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]))

main()
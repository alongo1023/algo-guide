from collections import deque

from trees.TreeNode import TreeNode

'''Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).'''


def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    result = []
    q = deque()
    if root:
        q.append(root)
    while len(q) > 0:
        size = len(q)
        currList = []
        for i in range(size):
            curr = q.popleft()
            currList.append(curr.data)
            if (curr.left):
                q.append(curr.left)
            if (curr.right):
                q.append(curr.right)
        result.append(currList)
    return result


def main():
    t1 = TreeNode(4)
    for n in [0, 3, 1, 5, 6, 2, 7]:
        t1.insert(n)
    assert(levelOrder(t1) == [[4], [3, 5], [1, 6], [2, 7]])

    t2 = TreeNode(1)
    assert(levelOrder(t2) == [[1]])

    t3 = TreeNode(5)
    for i in [2, 6, 7, 1, 8]:
        t3.insert(i)
    assert(levelOrder(t3) == [[5], [2, 6], [1, 7], [8]])

main()


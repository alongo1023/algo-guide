'''
Given the root of a binary search tree, and an integer k,
return the kth (1-indexed) smallest element in the tree.
'''
from collections import deque

from trees.TreeNode import TreeNode


def kthSmallest(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    stack = deque()
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.data
        root = root.right

def main():
    t1 = TreeNode(6)
    for i in [4, 9, 3, 1, 10]:
        t1.insert(i)
    assert(kthSmallest(t1, 4) == 6)

    t2 = TreeNode(5)
    for i in [3, 4, 6, 2, 1]:
        t2.insert(i)
    assert(kthSmallest(t2, 1) == 1)
    assert (kthSmallest(t2, 3) == 3)

    t3 = TreeNode(10)
    for i in [12, 15, 20]:
        t3.insert(i)
    assert(kthSmallest(t3, 4) == 20)
main()
'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
'''
from trees.TreeNode import TreeNode


def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if (not p and not q):
        return True
    if (not p or not q or (p.data != q.data)):
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


def main():
    p1 = TreeNode(4)
    q1 = TreeNode(4)
    for i in [2, 9, 10, 6]:
        q1.insert(i)
        p1.insert(i)
    assert(isSameTree(p1, q1))

    p2 = TreeNode(4)
    q2 = TreeNode(4)
    for i in [2, 11, 7]:
        q2.insert(i)
    for i in [0, 5, 6]:
        p2.insert(i)
    assert ( not isSameTree(p2, q2))

    p3= TreeNode()
    q3 = TreeNode(4)
    for i in [1, 2, 3, 5, 6]:
        q3.insert(i)
    assert(not isSameTree(p3, q3))
    assert(not isSameTree(q3, p3))

    p4 = TreeNode()
    q4 = TreeNode()
    assert isSameTree(p4, q4)


main()
'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same
structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
The tree tree could also be considered as a subtree of itself.
'''
from trees.TreeNode import TreeNode


def isSubtree(root, subRoot):
    """
    :type root: TreeNode
    :type subRoot: TreeNode
    :rtype: bool
    """
    if not root:
        return False
    elif isSameTree(root, subRoot):
        return True
    else:
        return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


def isSameTree(root, subRoot):
    if not root or not subRoot:
        return not root and not subRoot
    return root.data == subRoot.data and isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)


def main():
    t1 = TreeNode(4)
    for i in [3, 5, 1]:
        t1.insert(i)
    s1 = TreeNode(4)
    for i in [3, 5]:
        s1.insert(i)
    assert (not isSubtree(t1, s1))

    t2 = TreeNode(1)
    s2 = TreeNode(0)
    assert (not isSubtree(t2, s2))

    t3 = TreeNode(7)
    for i in [3, 6, 1, 10, 8, 12]:
        t3.insert(i)
    s3 = TreeNode(10)
    for i in [8, 12]:
        s3.insert(i)
    assert (isSubtree(t3, s3))


main()

'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p
and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''
from trees.TreeNode import TreeNode


def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if p.data < root.data and q.data < root.data:
        return lowestCommonAncestor(root.left, p, q)
    elif p.data > root.data and q.data > root.data:
        return lowestCommonAncestor(root.right, p, q)
    else:
        return root


def main():
    t1 = TreeNode(6)
    t1Left = TreeNode(3)
    t1Right = TreeNode(8)
    t1RR = TreeNode(10)
    for i in [t1Left, t1Right, t1RR]:
        t1.insertNode(i)
    assert (lowestCommonAncestor(t1, t1Right, t1RR) == t1Right)

    t2 = TreeNode(6)
    t2Left = TreeNode(2)
    t2Right = TreeNode(10)
    t2LR = TreeNode(3)
    t2LL = TreeNode(1)
    for i in [t2Left, t2LL, t2LR]:
        t2.insertNode(i)
    assert (lowestCommonAncestor(t2, t2LL, t2LR) == t2Left)
    assert (lowestCommonAncestor(t2, t2Left, t2Right) == t2)


main()

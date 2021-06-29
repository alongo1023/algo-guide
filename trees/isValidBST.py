'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''

from trees.TreeNode import TreeNode


def isValidBST(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    return isValidBSTHelper(root, None, None)


def isValidBSTHelper(curr, minVal, maxVal):
    if not curr:
        return True
    if ((minVal != None and curr.data <= minVal) or (maxVal != None and curr.data >= maxVal)):
        return False
    return isValidBSTHelper(curr.left, minVal, curr.data) and isValidBSTHelper(curr.right, curr.data, maxVal)

def main():
    t1 = TreeNode(5)
    for i in [1, 8, 10, 7, 3, 0]:
        t1.insert(i)
    assert(isValidBST(t1))

    t2 = TreeNode(5)
    t2.left = TreeNode(8)
    assert(not isValidBST(t2))

    t3 = TreeNode(0)
    t3.left = TreeNode(-1)
    t3.right = TreeNode(6)
    t3.left.left = TreeNode(4)
    assert(not isValidBST(t3))

main()
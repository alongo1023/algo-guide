'''
A binary tree's maximum depth is the number of nodes along the
longest path from the root node down to the farthest leaf node.
'''
from trees.TreeNode import TreeNode


def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

def main():
    tree1 = TreeNode(1)
    for i in [2, 3, 4, 5, 6]:
        tree1.insert(i)
    assert(maxDepth(tree1) == 6)

    tree2 = TreeNode(5)
    for i in [3, 4, 6, 8, 10, 1]:
        tree2.insert(i)
    assert(maxDepth(tree2) == 4)

    tree3 = TreeNode(10)
    assert(maxDepth(tree3) == 1)

main()
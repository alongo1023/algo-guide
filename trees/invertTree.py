from trees.TreeNode import TreeNode

'''Given the root of a binary tree, invert the tree, and return its root.'''

def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root:
        return;
    left = root.left
    right = root.right
    invertTree(left)
    invertTree(right)
    root.left = right
    root.right = left
    return root

def main():
    t1 = TreeNode(4)
    for i in [2,7,1,3,6,9]:
        t1.insert(i)
    t1.__str__()
    invertTree(t1)
    print("=========")
    t1.__str__()

main()


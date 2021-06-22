from trees.TreeNode import TreeNode

'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge 
connecting them. A node can only appear in the sequence at most once. Note that the path does not need to 
pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.
'''
def maxPathSumHelper(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return (0, float('-inf'))

    leftSum, maxLeftPathSum = maxPathSumHelper(root.left)
    rightSum, maxRightPathSum = maxPathSumHelper(root.right)
    maxLeftSum = max(0, leftSum)
    maxRightSum = max(0, rightSum)
    currPathSum = root.data + maxLeftSum + maxRightSum
    maxSum = max(maxLeftPathSum, maxRightPathSum, currPathSum)
    return (root.data + max(maxLeftSum, maxRightSum), maxSum)


def maxPathSum(root):
    return maxPathSumHelper(root)[1]

def main():
    t1 = TreeNode(1)
    for i in [2, 3]:
        t1.insert(i)
    assert(maxPathSum(t1) == 6)

    t2 = TreeNode()
    for i in [-10,9,20,15,7]:
        t2.insert(i)
    assert(maxPathSum(t2) == 51)

main()



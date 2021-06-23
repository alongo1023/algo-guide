'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored
in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same
or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
serialization/deserialization algorithm should work. You just need to ensure that a binary tree can
be serialized to a string and this string can be deserialized to the original tree structure.
'''
from collections import deque
from trees.TreeNode import TreeNode

def serialize(root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    if not root:
        return "X"
    leftSerialize = serialize(root.left)
    rightSerialize = serialize(root.right)
    return str(root.data) + "," + leftSerialize + "," + rightSerialize


def deserialize(data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    nodesLeft = deque()
    dataList = data.split(",")
    for num in dataList:
        nodesLeft.append(num)
    return deserializeHelper(nodesLeft)


def deserializeHelper(nodesLeft):
    if (len(nodesLeft) == 0):
        return
    value = nodesLeft.popleft()
    if ("X" == value): return None
    newNode = TreeNode(value)
    newNode.left = deserializeHelper(nodesLeft)
    newNode.right = deserializeHelper(nodesLeft)
    return newNode

def main():
    t1 = TreeNode(2)
    for i in [1, 4, 3, 5]:
        t1.insert(i)
    ser = serialize(t1)
    print(ser)
    print(deserialize(ser).__str__())

    print("================")

    t2 = TreeNode(2)
    ser = serialize(t2)
    print(ser)
    print(deserialize(ser).__str__())
main()
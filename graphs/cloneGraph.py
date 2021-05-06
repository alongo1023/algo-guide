'''Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.'''

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node):
    '''
    :param node: Node
    :return: Node
    '''
    oldToNew = {}

    def dfs(node):
        if not node:
            return None
        if node in oldToNew:
            return oldToNew[node]
        copy = Node(node.val)
        oldToNew[node] = copy
        for adj in node.neighbors:
            copy.neighbors.append(dfs(adj))
        return copy

    return dfs(node)

def main():
    nodeA = Node(1)
    nodeB = Node(2)
    nodeC = Node(3)
    nodeD = Node(4)
    nodeA.neighbors = [nodeB, nodeD]
    nodeB.neighbors = [nodeA, nodeC]
    nodeC.neighbors = [nodeB, nodeD]
    nodeD.neighbors = [nodeA, nodeC]
    copy = cloneGraph(nodeA)
    assert(nodeA != copy)
    assert(nodeA.neighbors != copy.neighbors)

main()

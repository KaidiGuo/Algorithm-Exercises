"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
"""
The breadth first method uses a queue to travel the graph/tree.
We take the root, add it to the queue, we then take the first element, add its (direct, distance = 1) children to the queue.
these two way are baily the same idea:
1.pop the first element in the queue, add its children to the queue, pop the new first element, add its children... until no node.
2.add the children of first element to the queue, add the children of the second element to the queue, add the children... until no node.

if we proceed the tree by note like this way, we need extra variables to store the level/depth.
The following method takes the second way, add (node,level) as a pare to the queue, thus we know the level/depth of each node.
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        queue=[]
        if root: queue.append((root,1))
        depth=0
        for (node,level) in queue:
            depth=level
            for child in node.children:
                queue.append((child,level+1))
        return depth

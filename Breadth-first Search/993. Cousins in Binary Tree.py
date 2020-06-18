# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Use BFS here to traverse the tree.
Along the traverse, create a dictionary to store the information (level, parent) of each node, with node value as the key
After the traverse, we can compare the node x and y their level and parents: cousins are of same level, different parents.
"""
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root: return False
        dic = {}
        queue = []
        if root:
            queue.append((root, 0))
            dic[root.val] = (0, 0)
        for (node, level) in queue:
            if node.left:
                queue.append((node.left, level + 1))
                dic[node.left.val] = (level + 1, node)
            if node.right:
                queue.append((node.right, level + 1))
                dic[node.right.val] = (level + 1, node)
        if dic[x][0] == dic[y][0] and dic[x][1] != dic[y][1]:
            return True
        return False




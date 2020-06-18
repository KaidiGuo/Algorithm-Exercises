# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Use BFS here to traverse the tree layer by layer (level by level).
Along the traverse, use one queue for current layer, another queue for the next layer.
Traverse the current queue (in the beginning, it should has only one node, the root, as in layer 0)
pop the first node, add its children to the next queue, pop the new first, add its children... until no node in current queue.
save current layer's nodes (their val) in a list, append it to results[].
replace the current queue with the fresh generated "next queue", start over again.
until the "next queue" is be empty.
return the results list reversed.
"""

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = []
        results = []
        if root: queue.append(root)
        while queue:
            layer = []
            next_queue = []
            while queue:
                first_node = queue[0]
                queue.pop(0)
                layer.append(first_node.val)
                if first_node.left: next_queue.append(first_node.left)
                if first_node.right: next_queue.append(first_node.right)
            results.append(layer)
            queue = next_queue
        return results[::-1]
